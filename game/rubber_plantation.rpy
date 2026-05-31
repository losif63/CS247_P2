################################################################################
## RUBBER PLANTATION — Colonial Ledger Matching Puzzle
################################################################################
image rubber_plantation_bg = "images/rubber.png"
image bg black = Solid("#000")

init python:

    # ── Ledger entries (workers listed without names) ─────────────────────────

    LEDGER_ENTRIES = [
        {"id": "100329", "residence": "Tapper", "outputs": (12, 8, 0),
        "note": "Unfit for labor."},

        {"id": "100330", "residence": "Grove B", "outputs": (55, 0, 0),
        "note": ""},

        {"id": "100331", "residence": "Grove A", "outputs": (52, 37, 32),
        "note": "Pay adjusted — nursing"},

        {"id": "100332", "residence": "Field Rotation", "outputs": (66, 24, 22),
        "note": "Quotas unmet."},

        {"id": "100333", "residence": "Transport", "outputs": (75, 77, 77),
        "note": ""},

        {"id": "100334", "residence": "Transport", "outputs": (88, 86, 90),
        "note": "Requests to be assigned with younger sibling."},

        {"id": "100335", "residence": "Grove A", "outputs": (26, 26, 27),
        "note": "Guardian: 100331."},

        {"id": "100336", "residence": "Grove A", "outputs": (70, 73, 70),
        "note": "Contract revised - week 18 (birth in family)."},
    ]

    # ── Census entries  ──────────

    CENSUS_ENTRIES = [  

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
        "family": "Unspecified",
        "labor_status": "Unfit"
    },

    {
        "name": "Kovi Sela",
        "age": 8,
        "sex": "M",
        "race": "Non-White",
        "marital": "Unmarried",
        "family": "Unspecified",
        "labor_status": "Fit"
    },

    {
        "name": "Aran Sotan",
        "age": 24,
        "sex": "M",
        "race": "Non-White",
        "marital": "Unmarried",
        "family": "Eldest of 2 sons",
        "labor_status": "Fit"
    },

    {
        "name": "Mira Sotan",
        "age": 22,
        "sex": "M",
        "race": "Non-White",
        "marital": "Unmarried",
        "family": "One sibling",
        "labor_status": "Fit"
    },

    {
        "name": "Nes Tavar",
        "age": 28,
        "sex": "M",
        "race": "Non-White",
        "marital": "Married",
        "family": "Infant child",
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

    CORRECT_MATCHES = {
        0: 2,  1: 0,  2: 7,  3: 1,
        4: 5,  5: 4,  6: 3,  7: 6,
    }

    # ── Puzzle state (globals reset at scene start) ───────────────────────────

    plantation_matches  = [None] * 8   # matches[ledger_idx] = census_idx | None
    plantation_selected = None          # ledger index currently highlighted
    plantation_names    = [""] * 8      # auto-filled from match; shown under worker ID
    plantation_struck   = set()         # ledger indices marked wrong on last submit

    def plantation_select_ledger(idx):
        global plantation_selected
        plantation_selected = None if plantation_selected == idx else idx
        renpy.restart_interaction()

    def plantation_assign(census_idx):
        global plantation_matches, plantation_selected, plantation_names, plantation_struck
        if plantation_selected is None:
            return
        # Toggle off if re-clicking the already-assigned census entry
        if plantation_matches[plantation_selected] == census_idx:
            plantation_matches[plantation_selected] = None
            plantation_names[plantation_selected] = ""
            plantation_selected = None
            renpy.restart_interaction()
            return
        # Steal from any other ledger entry that had this census assigned
        for i in range(8):
            if plantation_matches[i] == census_idx:
                plantation_matches[i] = None
                plantation_names[i] = ""
        plantation_matches[plantation_selected] = census_idx
        plantation_names[plantation_selected] = CENSUS_ENTRIES[census_idx]["name"]
        plantation_struck.discard(plantation_selected)
        if CORRECT_MATCHES.get(plantation_selected) == census_idx:
            renpy.sound.play("audio/ledger-correct-feedback.wav")
        else:
            renpy.sound.play("audio/ledger-incorrect-feedback.wav")
        plantation_selected = None
        renpy.restart_interaction()

    def plantation_reset():
        global plantation_matches, plantation_selected, plantation_names, plantation_struck
        plantation_matches  = [None] * 8
        plantation_selected = None
        plantation_names    = [""] * 8
        plantation_struck   = set()
        renpy.restart_interaction()

    def plantation_check_answers():
        return all(plantation_matches[li] == ci for li, ci in CORRECT_MATCHES.items())


################################################################################
## Styles
################################################################################

style plantation_panel_frame:
    background Frame("gui/paper_pixel.png", 0, 0, 0, 0)
    padding (0, 0, 0, 0)

style plantation_header_frame:
    background "#00000000"
    xfill True
    padding (16, 18, 16, 18)

style plantation_header_text:
    font "fonts/Blackrush.ttf"
    color "#1a0d00"
    size 75
    text_align 0.5

style plantation_dim_text:
    color "#1a0d00"
    font "fonts/Kopi.otf"
    size 26

style plantation_col_header_text:
    font "fonts/Kopi.otf"
    color "#1a0d00"
    size 26

style census_header_text:
    font "fonts/OldLondon.ttf"
    color "#1a0d00"
    size 65
    text_align 0.5

style census_dim_text:
    color "#1a0d00"
    font "fonts/mom.ttf"
    size 20

style census_col_header_text:
    font "fonts/OldLondon.ttf"
    color "#1a0d00"
    size 28

style ledger_notes_text:
    font "fonts/Kopi.otf"
    color "#1a0d00"
    size 24

style reveal_text_number:
    font "fonts/Kopi.otf"
    size 80
    color "#000000"

style reveal_text_name:
    font "fonts/handwriting.ttf"
    size 80
    color "#000000"

################################################################################
## Screens
################################################################################

transform name_appear(delay):
    alpha 0.0
    pause delay
    linear 1.8 alpha 1.0

transform id_disappear(delay):
    alpha 1.0
    pause delay
    linear 1.8 alpha 0.0


# Ledger panel only — matched names fade in one by one in handwriting
screen ledger_names_reveal():
    add "#0d0b07"

    frame:
        style "plantation_panel_frame"
        xalign 0.5
        yalign 0.45
        xsize 980
        ysize 1000
        vbox:
           
            yalign 0.5
            xalign 0.5
            spacing 54
            for i in range(8):
                $ _e    = LEDGER_ENTRIES[i]
                $ _name = CENSUS_ENTRIES[CORRECT_MATCHES[i]]["name"]
                fixed:
                    xsize 500
                    ysize 40
                    xalign 0.5
                    text _e["id"] style "reveal_text_number" xalign 0.5 yalign 0.5 text_align 0.5 at id_disappear(i * 0.5)
                    text _name style "reveal_text_name" xalign 0.5 yalign 0.5 text_align 0.5 at name_appear(i * 0.5)


screen plantation_puzzle():

    default hovered_ledger = None
    default hovered_census = None

    if plantation_check_answers():
        timer 1.0 action Return("solved")

    add "#0d0b07"

    # ── Title ─────────────────────────────────────────────────────────────────
    frame:
        xalign 0.5
        ypos 8
        xsize 1760
        background "#1e160a"
        padding (20, 10)

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
                                text "Assignment" style "plantation_col_header_text"
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
                            $ _e      = LEDGER_ENTRIES[i]
                            $ _eid    = _e["id"]
                            $ _out1, _out2, _out3 = _e["outputs"]
                            $ _eres   = _e["residence"]
                            $ _enote  = _e["note"]
                            $ _matched    = plantation_matches[i]
                            $ _sel        = (plantation_selected == i)
                            $ _wname      = plantation_names[i]
                            $ _is_struck  = (i in plantation_struck)
                            $ _is_correct = (plantation_matches[i] is not None and CORRECT_MATCHES.get(i) == plantation_matches[i])

                            frame:
                                background ("#fac268ff" if _sel else ("#47853766" if _is_correct else ("#fac26844" if hovered_ledger == i else "#00000000")))
                                xfill True
                                padding (4, 2)
                                vbox:
                                    spacing 2
                                    hbox:
                                        spacing 12
                                        button:
                                            xsize 120
                                            ysize 20
                                            background "#00000000"
                                            hover_background "#00000000"
                                            hovered (NullAction() if _is_correct else SetScreenVariable("hovered_ledger", i))
                                            unhovered SetScreenVariable("hovered_ledger", None)
                                            padding (0, 0)
                                            action (NullAction() if _is_correct else [Play("sound", "audio/map-click.wav"), Function(plantation_select_ledger, i)])
                                            text "[_eid]" style "plantation_dim_text"
                                        frame:
                                            xsize 120
                                            background None
                                            padding (0, 0)
                                            text "[_eres]" style "plantation_dim_text"
                                        frame:
                                            xsize 100
                                            background None
                                            padding (0, 0)
                                            text "[_out1]kg" style "plantation_dim_text"
                                        frame:
                                            xsize 100
                                            background None
                                            padding (0, 0)
                                            text "[_out2]kg" style "plantation_dim_text"
                                        frame:
                                            xsize 100
                                            background None
                                            padding (0, 0)
                                            text "[_out3]kg" style "plantation_dim_text"
                                        frame:
                                            xsize 160
                                            background None
                                            padding (0, 0)
                                            text "[_enote]" style "ledger_notes_text"


        # RIGHT — Census
        frame:
            style "plantation_panel_frame"
            xysize (1080, 870)
            vbox:
                xpos 20
                frame:
                    style "plantation_header_frame"
                    text "Residential Survey of Inhabitants of Pelau Siring - 1897" style "census_header_text"
                viewport:
                    xysize (1080, 830)
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
                                xsize 75
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Race" style "census_col_header_text"
                            frame:
                                xsize 150
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Marital" style "census_col_header_text"
                            frame:
                                xsize 210
                                ysize 20
                                background None
                                padding (0, 0)
                                text "Family" style "census_col_header_text"
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
                            $ _casgn       = next((ii for ii in range(8) if plantation_matches[ii] == j), None)
                            $ _cis_correct = (_casgn is not None and CORRECT_MATCHES[_casgn] == j)
                            $ _cact        = [Play("sound", "audio/map-click.wav"), Function(plantation_assign, j)]

                            frame:
                                background ("#47853766" if _cis_correct else ("#fac26844" if hovered_census == j else "#00000000"))
                                xfill True
                                padding (0, 2)
                                hbox:
                                    spacing 15
                                    button:
                                        xsize 160
                                        background "#00000000"
                                        hover_background "#00000000"
                                        hovered (NullAction() if _cis_correct else SetScreenVariable("hovered_census", j))
                                        unhovered SetScreenVariable("hovered_census", None)
                                        padding (0, 0)
                                        action (NullAction() if _cis_correct else _cact)
                                        text "[_pname]" style "census_dim_text" color "#1a0d00"
                                    frame:
                                        xsize 35
                                        background None
                                        padding (0, 0)
                                        text "[_page]" style "census_dim_text"
                                    frame:
                                        xsize 30
                                        background None
                                        padding (0, 0)
                                        text "[_psex]" style "census_dim_text"
                                    frame:
                                        xsize 75
                                        background None
                                        padding (0, 0)
                                        text "[_prace]" style "census_dim_text"
                                    frame:
                                        xsize 150
                                        background None
                                        padding (0, 0)
                                        text "[_pmarital]" style "census_dim_text"
                                    frame:
                                        xsize 210
                                        background None
                                        padding (0, 0)
                                        text "[_pnotes]" style "census_dim_text"
                                    frame:
                                        xsize 120
                                        background None
                                        padding (0, 0)
                                        text "[_plabor]" style "census_dim_text"

    # ── Footer ────────────────────────────────────────────────────────────────
    hbox:
        xalign 0.5
        ypos 974
        spacing 40

        textbutton "Reset All":
            style "map_button_button"
            action Function(plantation_reset)

        textbutton "Leave":
            style "map_button_button"
            action Return("exit")


################################################################################
## Scene
################################################################################

label rubber_plantation_scene:
    scene rubber_plantation_bg at fit_screen
    with Dissolve(0.5)

    play music "audio/plantation-wind.wav" loop fadein 1.0

    "You arrive at the rubber plantation at the edge of the village."
    "The smell of latex and jungle humidity hangs heavy in the air."
    "Rows of rubber trees stretch as far as the eye can see, their bark scarred with diagonal cuts."

    "Near the foreman's hut, you find a strongbox. The lock was broken open long ago."
    "Inside, there is a colonial production ledger, and tucked behind it, a residential census."

    m "The ledger doesn't use names, just numbered workers, their assignments, and their monthly output."
    m "But it looks like someone was trying to match them to the names in the census."
    m "Let me finish what they started."

    stop music fadeout 1.0
    $ plantation_reset()

    label .puzzle_loop:
        $ journal_blocked = True
        call screen plantation_puzzle
        $ journal_blocked = False
        if _return == "solved":
            jump rubber_plantation_solved
        elif _return == "exit":
            return

image marcus_haggling = "images/Marcus_Haggling_New.png"
image marcus_sitting = "images/marcusasset.png"

transform fullscreen:
    xysize (1920, 1080)
    fit "cover"
    xalign 0.5
    yalign 0.5

label rubber_plantation_solved:

    play music "audio/plantation-solved.wav" fadein 1.0

    # ── Journal entries ────────────────────────────────────────────────────────
    $ journal_add_item(
        id="rubber_plantation.colonial_ledger",
        name="Colonial Ledger",
        location="Rubber Plantation",
        description="A numbered production ledger from the Pelau Siring Rubber Cultivation Authority. Eight workers recorded by ID, residence block, and monthly rubber output, but no names."
    )
    $ journal_add_item(
        id="rubber_plantation.residential_census",
        name="Residential Census (1897)",
        location="Rubber Plantation",
        description="A residential survey of Pelau Siring inhabitants. Eight names with ages and family notes. Someone had begun annotating it in a different ink, trying to match names to ledger numbers."
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

    stop music fadeout 1.0

    show screen plantation_puzzle
    with Dissolve(0.8)

    "You lay the two documents side by side."

    hide screen plantation_puzzle
    show screen ledger_names_reveal
    with Dissolve(0.8)

    "The numbers become people."

    m "Banu. Davan. Linh. Komal."
    m "Mira. Aran. Kovi. Nesa."
    m "Eight names. Eight people the ledger reduced to outputs and tallies."

    hide screen ledger_names_reveal
    with Dissolve(1.0)

    show screen plantation_puzzle
    "You photograph both documents and slip them into your bag."
    hide screen plantation_puzzle
    with Dissolve(1.0)

    scene bg black
    show marcus_sitting 
    with Dissolve(1.0)

    "Back home, Marcus sits down for the first time in days."

    menu:
        "Leave the plantation":
            pass
    return


