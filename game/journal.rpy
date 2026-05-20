##############################################################################
## Investigation Journal
## Three tabs: Inventory | Friends | Clues
## Open via the "Journal" button in the quick menu.
##############################################################################


# ─── Game-state variables ─────────────────────────────────────────────────────

default inventory_items = []
# Each entry: {"id": str, "name": str, "location": str, "description": str}

default inventory_clues = []
# Each entry: {"text": str, "location": str}

default friend_notes = {
    "evelyn": {
        "symptom": "Feels like she's burning up all the time for no reason.",
        "solved": False,
        "notes": [],
    },
    "marcus": {
        "symptom": "Can't stop working. Can't sit down at home.",
        "solved": False,
        "notes": [],
    },
    "theo": {
        "symptom": "Can't get rid of anything. Things he throws away keep reappearing.",
        "solved": False,
        "notes": [],
    },
    "yuna": {
        "symptom": "People can't see her anymore.",
        "solved": False,
        "notes": [],
    },
    "aanya": {
        "symptom": "Can't speak Tamil anymore.",
        "solved": False,
        "notes": [],
    },
}


init python:

    def journal_add_item(id, name, location, description):
        if not any(i["id"] == id for i in inventory_items):
            inventory_items.append({
                "id": id,
                "name": name,
                "location": location,
                "description": description,
            })

    def journal_add_clue(text, location):
        if not any(c["text"] == text for c in inventory_clues):
            inventory_clues.append({"text": text, "location": location})

    def journal_update_friend(name, note=None, solved=False):
        if name in friend_notes:
            if note and note not in friend_notes[name]["notes"]:
                friend_notes[name]["notes"].append(note)
            if solved:
                friend_notes[name]["solved"] = True


# ─── Styles ───────────────────────────────────────────────────────────────────

style jnl_tab_idle:
    background "#1a1714"
    hover_background "#2d2720"
    padding (20, 12, 20, 12)
    xsize 200
    yfill True

style jnl_tab_idle_text:
    font "fonts/OldLondon.ttf"
    color "#7a6a50"
    hover_color "#e8d5a0"
    size 26
    text_align 0.5

style jnl_tab_active is jnl_tab_idle:
    background "#2d2720"

style jnl_tab_active_text is jnl_tab_idle_text:
    color "#e8d5a0"

style jnl_item_frame:
    background "#14120f"
    padding (16, 12, 16, 12)
    xfill True

style jnl_title_text:
    font "fonts/OldLondon.ttf"
    color "#e8d5a0"
    size 26

style jnl_meta_text:
    font "fonts/Typewriter.ttf"
    color "#7a6a50"
    size 15

style jnl_body_text:
    font "fonts/Typewriter.ttf"
    color "#c4b090"
    size 17
    line_spacing 4

style jnl_empty_text:
    font "fonts/Typewriter.ttf"
    color "#5a4e38"
    size 20
    text_align 0.5


# ─── Main screen ──────────────────────────────────────────────────────────────

screen journal_screen():
    modal True
    zorder 100

    default tab = "inventory"

    add "#000000bb"

    frame:
        xalign 0.5
        yalign 0.5
        xysize (1200, 820)
        background "#161412"
        padding (0, 0, 0, 0)

        vbox:
            xfill True
            yfill True

            # ── Header bar ───────────────────────────────────────────────────
            frame:
                xfill True
                ysize 52
                background "#0e0c0a"
                padding (24, 0, 0, 0)

                hbox:
                    xfill True
                    yfill True

                    text "Investigation Journal":
                        font "fonts/OldLondon.ttf"
                        color "#b89050"
                        size 30
                        yalign 0.5

                    null xfill True

                    textbutton "Close":
                        xsize 90
                        yfill True
                        background "#00000000"
                        hover_background "#3a2010"
                        action Function(renpy.hide_screen, "journal_screen")
                        text_color "#7a6a50"
                        text_hover_color "#e8d5a0"
                        text_font "fonts/Typewriter.ttf"
                        text_size 24
                        text_xalign 0.5
                        text_yalign 0.5

            # ── Tab row ───────────────────────────────────────────────────────
            hbox:
                xfill True
                ysize 46
                spacing 2

                textbutton "Inventory":
                    style ("jnl_tab_active" if tab == "inventory" else "jnl_tab_idle")
                    action SetScreenVariable("tab", "inventory")

                textbutton "Friends":
                    style ("jnl_tab_active" if tab == "friends" else "jnl_tab_idle")
                    action SetScreenVariable("tab", "friends")

                textbutton "Clues":
                    style ("jnl_tab_active" if tab == "clues" else "jnl_tab_idle")
                    action SetScreenVariable("tab", "clues")

                null xfill True

            # ── Content area ─────────────────────────────────────────────────
            frame:
                xfill True
                yfill True
                background "#1e1b17"
                padding (20, 16, 20, 16)

                if tab == "inventory":
                    use journal_tab_inventory
                elif tab == "friends":
                    use journal_tab_friends
                elif tab == "clues":
                    use journal_tab_clues


# ─── Evidence tab ─────────────────────────────────────────────────────────────

screen journal_tab_inventory():
    if inventory_items:
        viewport:
            xfill True
            yfill True
            mousewheel True
            draggable True
            vbox:
                xfill True
                spacing 12
                for item in inventory_items:
                    $ _iname = item["name"]
                    $ _iloc  = item["location"]
                    $ _idesc = item["description"]
                    frame:
                        style "jnl_item_frame"
                        vbox:
                            spacing 4
                            text "[_iname]" style "jnl_title_text"
                            text "Found at: [_iloc]" style "jnl_meta_text"
                            null height 3
                            text "[_idesc]" style "jnl_body_text"
    else:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 8
            text "No items collected yet." style "jnl_empty_text" xalign 0.5
            text "Explore the village to find evidence." style "jnl_empty_text" xalign 0.5


# ─── Friends tab ──────────────────────────────────────────────────────────────

screen journal_tab_friends():
    viewport:
        xfill True
        yfill True
        mousewheel True
        draggable True
        vbox:
            xfill True
            spacing 14
            for fname, fdata in friend_notes.items():
                $ _fname   = fname.capitalize()
                $ _fsymptom = fdata["symptom"]
                $ _fsolved  = fdata["solved"]
                $ _fnotes   = fdata["notes"]
                frame:
                    style "jnl_item_frame"
                    background ("#0f180f" if _fsolved else "#14120f")
                    vbox:
                        spacing 4
                        hbox:
                            spacing 10
                            text "[_fname]" style "jnl_title_text" color ("#90d090" if _fsolved else "#e8d5a0")
                            if _fsolved:
                                text "  [Resolved]" style "jnl_meta_text" color "#6ab86a" yalign 1.0
                        text "[_fsymptom]" style "jnl_body_text" color "#a09070"
                        if _fnotes:
                            null height 6
                            for note in _fnotes:
                                $ _note = note
                                text "— [_note]" style "jnl_body_text"


# ─── Clues tab ────────────────────────────────────────────────────────────────

screen journal_tab_clues():
    if inventory_clues:
        viewport:
            xfill True
            yfill True
            mousewheel True
            draggable True
            vbox:
                xfill True
                spacing 10
                for clue in inventory_clues:
                    $ _cloc  = clue["location"]
                    $ _ctext = clue["text"]
                    frame:
                        style "jnl_item_frame"
                        vbox:
                            spacing 3
                            text "[ [_cloc] ]" style "jnl_meta_text"
                            text "[_ctext]" style "jnl_body_text"
    else:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 8
            text "No clues discovered yet." style "jnl_empty_text" xalign 0.5
            text "Investigate the village locations to learn more." style "jnl_empty_text" xalign 0.5
