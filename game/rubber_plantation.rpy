################################################################################
## RUBBER PLANTATION — Colonial Ledger Matching Puzzle
################################################################################

init python:

    # ── Ledger entries (workers listed without names) ─────────────────────────

    LEDGER_ENTRIES = [
        {"id": "100329", "residence": "Northern Rows", "outputs": (12, 8, 0),
        "note": "Unfit for labor."},

        {"id": "100330", "residence": "Southern Rows", "outputs": (55, 0, 0),
        "note": ""},

        {"id": "100331", "residence": "Western Rows", "outputs": (52, 37, 32),
        "note": "Takes frequent breaks to nurse baby."},

        {"id": "100332", "residence": "Southern Rows", "outputs": (66, 34, 32),
        "note": "Decreasing outputs."},

        {"id": "100333", "residence": "Eastern Rows", "outputs": (75, 77, 77),
        "note": "Often paired with other workers during collection rounds."},

        {"id": "100334", "residence": "Eastern Rows", "outputs": (88, 86, 90),
        "note": "Consistently highest output in eastern block. Frequently assigned oversight of adjacent rows."},

        {"id": "100335", "residence": "Western Rows", "outputs": (76, 76, 77),
        "note": "Taken care of by other workers."},

        {"id": "100336", "residence": "Eastern Rows", "outputs": (70, 73, 70),
        "note": "Regular reassignment to lighter tapping rows recorded."},
    ]

    # ── Census entries (shuffled so matching isn't trivially 1-to-1) ──────────

    CENSUS_ENTRIES = [  # sorted by last name

    {
        "name": "Davan Kori",
        "age": 26,
        "sex": "M",
        "race": "Non-White",
        "marital": "Married",
        "family": "Unspecified",
        "labor_status": "Deceased"
    },

    {
        "name": "Komal Kori",
        "age": 25,
        "sex": "F",
        "race": "Non-White",
        "marital": "Widowed",
        "family": "Unspecified",
        "labor_status": "Fit"
    },

    {
        "name": "Banu Korev",
        "age": 69,
        "sex": "M",
        "race": "Non-White",
        "marital": "Widowed",
        "family": "Unspecified / Extended household not recorded",
        "labor_status": "Unfit"
    },

    {
        "name": "Kovi Sela",
        "age": 10,
        "sex": "M",
        "race": "Non-White",
        "marital": "Unmarried",
        "family": "Unspecified / Dependent",
        "labor_status": "Fit (Light Duty)"
    },

    {
        "name": "Aran Sotan",
        "age": 22,
        "sex": "M",
        "race": "Non-White",
        "marital": "Unmarried",
        "family": "Eldest of 3 sons",
        "labor_status": "Fit"
    },

    {
        "name": "Mira Sotan",
        "age": 20,
        "sex": "F",
        "race": "Non-White",
        "marital": "Unmarried",
        "family": "Has 2 siblings",
        "labor_status": "Fit"
    },

    {
        "name": "Nesa Sotan",
        "age": 18,
        "sex": "M",
        "race": "Non-White",
        "marital": "Unmarried",
        "family": "Youngest of 3 sons",
        "labor_status": "Fit"
    },

    {
        "name": "Linh Tavar",
        "age": 24,
        "sex": "F",
        "race": "Non-White",
        "marital": "Married",
        "family": "Husband, infant daughter",
        "labor_status": "Fit"
    },

    ]

    # ── Correct mapping: LEDGER index → CENSUS index ─────────────────────────
    #   100329 [0] → Banu Korev   [2]  ("Unfit for labor" → Unfit, age 69)
    #   100330 [1] → Davan Kori   [0]  (output drops to 0 → Deceased)
    #   100331 [2] → Linh Tavar   [7]  (nurses baby → infant daughter)
    #   100332 [3] → Komal Kori   [1]  (decreasing outputs → widowed, bereaved)
    #   100333 [4] → Mira Sotan   [5]  (paired with workers → has siblings)
    #   100334 [5] → Aran Sotan   [4]  (highest output, oversight → eldest son)
    #   100335 [6] → Kovi Sela    [3]  ("taken care of" → Light Duty, age 10)
    #   100336 [7] → Nesa Sotan   [6]  (lighter rows → youngest son)

    CORRECT_MATCHES = {
        0: 2,  1: 0,  2: 7,  3: 1,
        4: 5,  5: 4,  6: 3,  7: 6,
    }

    # One distinct colour per matched pair
    MATCH_COLORS = [
        "#e74c3c", "#e67e22", "#f0c040", "#2ecc71",
        "#1abc9c", "#3498db", "#9b59b6", "#e91e63",
        "#ff5722", "#a0522d", "#607d8b", "#8bc34a",
        "#00bcd4", "#ff9800",
    ]

    # ── Puzzle state (globals reset at scene start) ───────────────────────────

    plantation_matches  = [None] * 8    # matches[ledger_idx] = census_idx | None
    plantation_selected = None          # ledger index currently highlighted

    def plantation_select_ledger(idx):
        global plantation_selected
        plantation_selected = None if plantation_selected == idx else idx
        renpy.restart_interaction()

    def plantation_assign(census_idx):
        global plantation_matches, plantation_selected
        if plantation_selected is None:
            return
        # Toggle off if re-clicking the currently assigned census entry
        if plantation_matches[plantation_selected] == census_idx:
            plantation_matches[plantation_selected] = None
            plantation_selected = None
            renpy.restart_interaction()
            return
        # Steal from any other ledger entry that had this census assigned
        for i in range(8):
            if plantation_matches[i] == census_idx:
                plantation_matches[i] = None
        plantation_matches[plantation_selected] = census_idx
        plantation_selected = None
        renpy.restart_interaction()

    def plantation_reset():
        global plantation_matches, plantation_selected
        plantation_matches  = [None] * 8
        plantation_selected = None
        renpy.restart_interaction()

    def plantation_check_answers():
        return all(plantation_matches[li] == ci for li, ci in CORRECT_MATCHES.items())

    def plantation_all_matched():
        return all(m is not None for m in plantation_matches)

    def plantation_matched_count():
        return sum(1 for m in plantation_matches if m is not None)


################################################################################
## Styles
################################################################################

style plantation_panel_frame:
    background Frame("gui/paper.jpg", 0, 0, 0, 0)
    padding (0, 0, 0, 0)

style plantation_header_frame:
    background "#00000000"
    xfill True
    padding (16, 18, 16, 18)

style plantation_header_text:
    font "fonts/MonsieurLaDoulaise-Regular.ttf"
    color "#1a0d00"
    size 60
    text_align 0.5

style plantation_entry_button:
    background "#00000000"
    hover_background "#00000011"
    padding (12, 7, 12, 7)
    xfill True

style plantation_dim_text:
    color "#1a0d00"
    font "fonts/Runethia.otf"
    size 18

style plantation_col_header_text:
    font "fonts/Runethia.otf"
    color "#1a0d00"
    size 26

style census_header_text:
    font "fonts/OldLondon.ttf"
    color "#1a0d00"
    size 50
    text_align 0.5

style census_dim_text:
    color "#1a0d00"
    font "fonts/Typewriter.ttf"
    size 20

style census_col_header_text:
    font "fonts/OldLondon.ttf"
    color "#1a0d00"
    size 30

################################################################################
## Screen
################################################################################

screen plantation_puzzle():

    add "#0d0b07"

    # ── Title ─────────────────────────────────────────────────────────────────
    frame:
        xalign 0.5
        ypos 8
        xsize 1760
        background "#1e160a"
        padding (20, 10)
        text "Pelau Siring Rubber Cultivation Authority" xalign 0.5 color "#c8a040" size 24 bold True

    text "Select a ledger entry, then select the matching census name. Click a matched pair again to undo." xalign 0.5 ypos 62 color "#666666" size 15

    # ── Two panels ────────────────────────────────────────────────────────────
    hbox:
        xalign 0.5
        ypos 90
        spacing 20

        # LEFT — Ledger
        frame:
            style "plantation_panel_frame"
            xysize (840, 870)

            vbox:
                xpos 30
                frame:
                    style "plantation_header_frame"
                    text "Pelau Siring Rubber Cultivation Authority":
                        style "plantation_header_text"

                viewport:
                    xysize (840, 830)
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 15

                        # Header row
                        hbox:
                            spacing 12
                            frame:
                                xsize 120
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Worker" style "plantation_col_header_text"
                            frame:
                                xsize 120
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Residence" style "plantation_col_header_text"
                            frame:
                                xsize 100
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Month 1" style "plantation_col_header_text"
                            frame:
                                xsize 100
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Month 2" style "plantation_col_header_text"
                                
                            frame:
                                xsize 100
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Month 3" style "plantation_col_header_text"
                                
                            frame:
                                xsize 160
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Notes" style "plantation_col_header_text"

                        # Data rows
                        for i in range(8):
                            $ _e = LEDGER_ENTRIES[i]
                            $ _eid = _e["id"]
                            $ _out1, _out2, _out3 = _e["outputs"]
                            $ _eres  = _e["residence"]
                            $ _enote = _e["note"]
                            $ _matched = plantation_matches[i]
                            $ _sel = (plantation_selected == i)
                            $ _col = MATCH_COLORS[_matched] if _matched is not None else ("#8b4513" if _sel else "#3a2010")
                            $ _bg = (MATCH_COLORS[_matched] + "2a") if _matched is not None else ("#8b45132a" if _sel else "#00000000")

                            hbox:
                                spacing 12
                                button:
                                    background _bg
                                    xsize 120
                                    ysize 20
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action Function(plantation_select_ledger, i)
                                    text "[_eid]" style "plantation_dim_text"
                                button:
                                    background _bg
                                    xsize 120
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action Function(plantation_select_ledger, i)
                                    text "[_eres]" style "plantation_dim_text"
                                button:
                                    background _bg
                                    xsize 100
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action Function(plantation_select_ledger, i)
                                    text "[_out1]kg" style "plantation_dim_text"
                                button:
                                    background _bg
                                    xsize 100
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action Function(plantation_select_ledger, i)
                                    text "[_out2]kg" style "plantation_dim_text"
                                button:
                                    background _bg
                                    xsize 100
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action Function(plantation_select_ledger, i)
                                    text "[_out3]kg" style "plantation_dim_text"
                                button:
                                    background _bg
                                    xsize 160
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action Function(plantation_select_ledger, i)
                                    text "[_enote]" style "plantation_dim_text"

        # RIGHT — Census
        frame:
            style "plantation_panel_frame"
            xysize (880, 870)
            vbox:
                xpos 20
                frame:
                    style "plantation_header_frame"
                    text "Residential Survey of Inhabitants of Pelau Siring - 1897" style "census_header_text"
                viewport:
                    xysize (880, 830)
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 10

                        # Header row
                        hbox:
                            spacing 15
                            frame:
                                xsize 160
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Name" style "census_col_header_text"
                            frame:
                                xsize 35
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Age" style "census_col_header_text"
                            frame:
                                xsize 30
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Sex" style "census_col_header_text"
                            frame:
                                xsize 55
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Race" style "census_col_header_text"
                            frame:
                                xsize 75
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Marital" style "census_col_header_text"
                            frame:
                                xsize 280
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Notes" style "census_col_header_text"
                            frame:
                                xsize 120
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Status" style "census_col_header_text"

                        # Data rows
                        for j in range(8):
                            $ _p        = CENSUS_ENTRIES[j]
                            $ _pname    = _p["name"]
                            $ _page     = _p["age"]
                            $ _psex     = _p["sex"]
                            $ _prace    = _p["race"]
                            $ _pmarital = _p["marital"]
                            $ _pnotes   = _p["family"]
                            $ _plabor   = _p["labor_status"]
                            $ _asgn  = next((ii for ii in range(8) if plantation_matches[ii] == j), None)
                            $ _pcol  = MATCH_COLORS[_asgn] if _asgn is not None else ("#2a1500" if plantation_selected is not None else "#6a5040")
                            $ _pbg   = (MATCH_COLORS[_asgn] + "2a") if _asgn is not None else "#00000000"
                            $ _act   = Function(plantation_assign, j) if plantation_selected is not None else NullAction()

                            hbox:
                                spacing 15
                                button:
                                    background _pbg
                                    xsize 160
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action _act
                                    text "[_pname]" style "census_dim_text"
                                button:
                                    background _pbg
                                    xsize 35
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action _act
                                    text "[_page]" style "census_dim_text"
                                button:
                                    background _pbg
                                    xsize 30
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action _act
                                    text "[_psex]" style "census_dim_text"
                                button:
                                    background _pbg
                                    xsize 55
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action _act
                                    text "[_prace]" style "census_dim_text"
                                button:
                                    background _pbg
                                    xsize 75
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action _act
                                    text "[_pmarital]" style "census_dim_text"
                                button:
                                    background _pbg
                                    xsize 280
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action _act
                                    text "[_pnotes]" style "census_dim_text"
                                button:
                                    background _pbg
                                    xsize 120
                                    hover_background "#00000011"
                                    padding (0, 0)
                                    action _act
                                    text "[_plabor]" style "census_dim_text"

    # ── Footer ────────────────────────────────────────────────────────────────
    hbox:
        xalign 0.5
        ypos 974
        spacing 40

        $ _count = plantation_matched_count()
        text "[_count]/8 matched" color "#666666" size 17 yalign 0.5

        if plantation_all_matched():
            textbutton "Submit Answers":
                style "map_button_button"
                action Return("check")
        else:
            null width 180

        textbutton "Reset All":
            style "map_button_button"
            action Function(plantation_reset)


################################################################################
## Scene
################################################################################

label rubber_plantation_scene:
    scene black
    with Dissolve(0.5)

    "You arrive at the rubber plantation at the edge of the village."
    "The smell of latex and jungle humidity hangs heavy in the air."
    "Rows of rubber trees stretch as far as the eye can see, their bark scarred with diagonal cuts."

    "Near the foreman's hut, you find a strongbox. The lock was broken open long ago."
    "Inside, there is a colonial production ledger, and tucked behind it, a residential census with margin notes in a different ink."

    m "The ledger doesn't use names, just numbered workers, their residence, and their monthly output."
    m "But someone annotated this census. Someone was trying to match them."
    m "Let me finish what they started."

    $ plantation_reset()

    label .puzzle_loop:
        call screen plantation_puzzle
        if _return == "check":
            if plantation_check_answers():
                jump rubber_plantation_solved
            else:
                m "Some of these don't add up. I need to look more carefully."
                jump .puzzle_loop

image marcus_haggling = "images/marcus-haggling.png"

transform fullscreen:
    xysize (1920, 1080)
    fit "cover"
    xalign 0.5
    yalign 0.5

label rubber_plantation_solved:

    # ── Journal entries ────────────────────────────────────────────────────────
    $ journal_add_item(
        "Colonial Ledger",
        "Rubber Plantation",
        "A numbered production ledger from the Pelau Siring Rubber Cultivation Authority. "
        "Eight workers recorded by ID, residence block, and monthly rubber output — no names."
    )
    $ journal_add_item(
        "Residential Census (1897)",
        "Rubber Plantation",
        "A residential survey of Pelau Siring inhabitants. Eight names with ages and family notes. "
        "Someone had begun annotating it in a different ink, trying to match names to ledger numbers."
    )
    $ journal_add_clue(
        "The colonial ledger stripped workers of their names, recording them only as numbers and outputs. "
        "Someone was already working to restore those names before us.",
        "Rubber Plantation"
    )
    $ journal_update_friend("marcus", note="His compulsion to work mirrors the colonial extraction of labor — the same erasure of rest and personhood recorded in the plantation ledger.", solved=True)

    # ── Flashback ──────────────────────────────────────────────────────────────
    scene marcus_haggling at fullscreen
    with Dissolve(1.0)

    "A memory surfaces."
    "Marcus, at the market."
    "He was shopping at a local art market, looking at trinkets and crafts made by the villagers."
    "He came across a handwoven blanket and haggled over the price."
    "The artisan let it go for a fraction of the original price, though that was already quite cheap by your standards."

    # ── Back to present ────────────────────────────────────────────────────────
    scene black
    with Dissolve(1.0)

    "You lay the two documents side by side."
    "The numbers become people."

    m "Banu. Davan. Linh. Komal."
    m "Mira. Aran. Kovi. Nesa."
    m "Eight names. Eight people the ledger reduced to outputs and tallies."

    "You photograph both documents and slip them into your bag."
    "Back home, Marcus sits down for the first time in days."

    menu:
        "Leave the plantation":
            pass
    return
