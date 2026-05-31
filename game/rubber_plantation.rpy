################################################################################
## RUBBER PLANTATION — Colonial Ledger Matching Puzzle
################################################################################
image rubber_plantation_bg = "images/rubber.png"

init python:

    import pygame

    def _match_hex_to_rgba(hex_color, alpha=210):
        h = hex_color.lstrip('#')
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), alpha)

    class MatchLineOverlay(renpy.Displayable):
        # ── Layout constants (pixels at 1920-wide screen) ──────────────────────
        HBOX_X       = 90     # (1920 - (840+20+880)) / 2
        HBOX_Y       = 90     # ypos of the two-panel hbox
        LEFT_W       = 840    # width of the ledger panel
        GAP          = 20     # spacing between panels

        # Approximate rendered heights of each panel's header frame.
        # If lines are visibly misaligned, tweak these two values.
        LEDGER_HDR_H = 130
        CENSUS_HDR_H = 130

        ROW_H        = 20     # ysize of each data row
        ROW_GAP      = 15     # vbox spacing between rows
        # Y of first data row inside the viewport
        # = header-row height (20) + one spacing gap (15)
        FIRST_ROW_Y  = 35

        def __init__(self, matches, **kwargs):
            super(MatchLineOverlay, self).__init__(**kwargs)
            self.matches = tuple(matches)

        def _ledger_y(self, i):
            vp_top = self.HBOX_Y + self.LEDGER_HDR_H
            return vp_top + self.FIRST_ROW_Y + i * (self.ROW_H + self.ROW_GAP) + self.ROW_H // 2

        def _census_y(self, j):
            vp_top = self.HBOX_Y + self.CENSUS_HDR_H
            return vp_top + self.FIRST_ROW_Y + j * (self.ROW_H + self.ROW_GAP) + self.ROW_H // 2

        def render(self, width, height, st, at):
            rv   = renpy.Render(width, height)
            surf = pygame.Surface((width, height), pygame.SRCALPHA)
            surf.fill((0, 0, 0, 0))

            x0 = self.HBOX_X + self.LEFT_W      # right edge of ledger panel
            x1 = x0 + self.GAP                  # left edge of census panel

            for li, ci in enumerate(self.matches):
                if ci is None:
                    continue
                rgba = _match_hex_to_rgba(MATCH_COLOR_ASSIGNED)
                y0   = self._ledger_y(li)
                y1   = self._census_y(ci)
                pygame.draw.line(surf, rgba, (x0, y0), (x1, y1), 3)
                pygame.draw.circle(surf, rgba, (x0, y0), 5)
                pygame.draw.circle(surf, rgba, (x1, y1), 5)

            rv.blit(surf, (0, 0))
            return rv

        def visit(self):
            return []

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
        "age": 22,
        "sex": "M",
        "race": "Non-White",
        "marital": "Unmarried",
        "family": "Eldest of 2 sons",
        "labor_status": "Fit"
    },

    {
        "name": "Mira Sotan",
        "age": 20,
        "sex": "M",
        "race": "Non-White",
        "marital": "Unmarried",
        "family": "1 sibling",
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

    # ── Correct mapping: LEDGER index → CENSUS index ─────────────────────────
    #   100329 [0] → Banu Korev   [2]  ("Unfit for labor" → Unfit, age 69)
    #   100330 [1] → Davan Kori   [0]  (output drops to 0 → Deceased)
    #   100331 [2] → Linh Tavar   [7]  (nurses baby → infant daughter)
    #   100332 [3] → Komal Kori   [1]  (decreasing outputs → widowed, bereaved)
    #   100333 [4] → Mira Sotan   [5]  (paired with workers → has siblings)
    #   100334 [5] → Aran Sotan   [4]  (highest output, oversight → eldest son)
    #   100335 [6] → Kovi Sela    [3]  ("taken care of" → Light Duty, age 10)
    #   100336 [7] → Nesa Tavar   [6]  (lighter rows → youngest son)

    CORRECT_MATCHES = {
        0: 2,  1: 0,  2: 7,  3: 1,
        4: 5,  5: 4,  6: 3,  7: 6,
    }

    MATCH_COLOR_CORRECT  = "#1a6b3a"   # dark green — correct pair
   
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

    def plantation_mark_wrong():
        global plantation_struck
        plantation_struck = set(
            li for li, ci in CORRECT_MATCHES.items()
            if plantation_matches[li] != ci
        )
        renpy.restart_interaction()


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

style plantation_entry_button:
    background "#00000000"
    hover_background "#00000011"
    padding (12, 7, 12, 7)
    xfill True

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

style ledger_name_text:
    font "fonts/handwriting.ttf"
    color "#b50000"
    size 30

style ledger_name_placeholder_text:
    font "fonts/handwriting.ttf"
    color "#000000"
    size 30

################################################################################
## Screens
################################################################################

screen plantation_name_input(idx):
    default typed_name = plantation_names[idx]

    # Blocks all interaction with the puzzle screen below
    modal True

    # Barely-there tint so the documents stay readable
    add "#00000033"

    frame:
        xalign 0.5
        yalign 0.93
        background "#1e160aee"
        padding (30, 18)
        vbox:
            spacing 10
            text "Who is worker [LEDGER_ENTRIES[idx]['id']]?":
                font "fonts/Kopi.otf"
                color "#c8a060"
                size 50
            input:
                value ScreenVariableInputValue("typed_name")
                length 100
                pixel_width 500
                font "fonts/handwriting.ttf"
                color "#e8dcc8"
                size 40
            textbutton "Confirm":
                xalign 0.5
            
                action [Function(plantation_set_name, idx, typed_name), Hide("plantation_name_input")]

    key "K_RETURN" action [Function(plantation_set_name, idx, typed_name), Hide("plantation_name_input")]


screen plantation_puzzle():

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

                            frame:
                                background ("#fac268ff" if _sel else "#00000000")
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
                                            hover_background "#00000022"
                                            padding (0, 0)
                                            action Function(plantation_select_ledger, i)
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

                                    # Name — auto-filled when matched; strikethrough only after failed submit
                                    frame:
                                        xsize 700
                                        background None
                                        padding (4, 0)
                                        if _wname and _is_struck:
                                            text "{s}[_wname]{/s}" style "ledger_name_text"
                                        elif _wname:
                                            text "[_wname]" style "ledger_name_text"
                                        else:
                                            null

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
                            $ _cact        = Function(plantation_assign, j)

                            hbox:
                                spacing 15
                                button:
                                    xsize 160
                                    background "#00000000"
                                    hover_background "#00000022"
                                    padding (0, 0)
                                    action _cact
                                    if _cis_correct:
                                        text "{s}[_pname]{/s}" style "census_dim_text" color "#1a0d00"
                                    else:
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

        textbutton "Submit":
            style "map_button_button"
            action Return("check")

        textbutton "Reset All":
            style "map_button_button"
            action Function(plantation_reset)

    textbutton "Return to Map":
        style "return_map_button"
        text_style "return_map_button_text"
        xalign 0.97
        yalign 0.04
        action Confirm("Are you sure you want to return to the map?", Return("Leave"))


################################################################################
## Scene
################################################################################

label rubber_plantation_scene:
    scene rubber_plantation_bg at fit_screen
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
    $ plantation_matches[4] = 5
    $ plantation_names[4] = "Mira Sotan"

    label .puzzle_loop:
        $ journal_blocked = True
        call screen plantation_puzzle
        $ journal_blocked = False
        if _return == "Leave":
            return
        if _return == "check":
            if plantation_check_answers():
                jump rubber_plantation_solved
            else:
                $ plantation_mark_wrong()
                jump rubber_plantation_failed

image marcus_haggling = "images/Marcus_Haggling_New.png"

transform fullscreen:
    xysize (1920, 1080)
    fit "cover"
    xalign 0.5
    yalign 0.5

label rubber_plantation_solved:

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

label rubber_plantation_failed:
    scene black
    with Dissolve(0.5)

    m "These don't add up."
    m "I'm matching numbers to names, but I'm missing something."
    m "I need to look more carefully."

    menu:
        "Try again":
            jump rubber_plantation_scene.puzzle_loop
        "Leave the plantation":
            return
