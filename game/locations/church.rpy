################################################################################
## Church — Exploration Tree
##
## Tree structure:
##   church
##   ├── church.main_hall
##   └── church.backyard
##       └── church.backyard.lawn  (requires shovel)
##
## To add a child to an existing node: add its ID to the parent's "children"
## list and add a new entry to EXPLORE_NODES. To add a puzzle, set "puzzle"
## to a label name and define that label below.
################################################################################


init python:
    EXPLORE_NODES.update({

        "church": {
            "name":       "Church",
            "parent":     None,
            "intro":      "church_intro",
            "children":   [
                "church.main_hall",
                "church.backyard",
            ],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "church.main_hall": {
            "name":       "Main Hall",
            "parent":     "church",
            "intro":      "church_main_hall_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "church.backyard": {
            "name":       "Backyard",
            "parent":     "church",
            "intro":      "church_backyard_intro",
            "children":   ["church.backyard.lawn"],
            "objects":    [
                {
                    "id":        "church.backyard.statue",
                    "name":      "Saint Mary's Statue",
                    "item":      None,
                    "action":    None,
                    "msg_first": "A stone statue of Saint Mary stands at the centre of the backyard. Her expression is serene, but the moss creeping up her base gives her an abandoned look.",
                    "msg_done":  "Saint Mary watches over the yard in silence.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "church.backyard.lawn": {
            "name":       "Lawn",
            "parent":     "church.backyard",
            "intro":      "church_backyard_lawn_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "church.backyard.lawn.box",
                    "name":      "Wooden Box",
                    "item":      None,
                    "action":    "church_backyard_box_puzzle",
                    "msg_first": "",
                    "msg_done":  "You already retrieved what was inside the box.",
                },
            ],
            "puzzle":     None,
            "requires":   "graveyard.shovel",
            "unlock":     "church_backyard_lawn_unlock",
            "locked_msg": "The soil here looks recently disturbed. You'd need something to dig with.",
        },

    })

    ITEM_CATALOG.update({
        "church.backyard.lawn.photo_piece": {
            "name": "Photo Piece 1",
            "location": "Church - Backyard",
            "description": "A piece of a torn photo. The piece shows a man smiling.",
        },
    })


# ── Lock screen ───────────────────────────────────────────────────────────────

screen church_box_lock_screen():
    modal True

    default d1 = 0
    default d2 = 0
    default d3 = 0
    default d4 = 0

    add "#000000bb"

    frame:
        xalign 0.5
        yalign 0.5
        xysize (520, 340)
        background "#161412"
        padding (40, 36, 40, 36)

        vbox:
            xfill True
            spacing 24

            text "A wooden box with a 4-digit combination lock.":
                font "fonts/Typewriter.ttf"
                color "#c4b090"
                size 18
                text_align 0.5
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 20

                for _digit_var, _digit_name in [
                    (d1, "d1"), (d2, "d2"), (d3, "d3"), (d4, "d4")
                ]:
                    vbox:
                        xsize 72
                        spacing 6

                        textbutton "▲":
                            xalign 0.5
                            background "#2d2720"
                            hover_background "#4a3c28"
                            padding (16, 8)
                            action SetScreenVariable(_digit_name, (_digit_var + 1) % 10)
                            text_color "#e8d5a0"
                            text_hover_color "#ffffff"
                            text_xalign 0.5

                        text "[_digit_var]":
                            font "fonts/SpecialElite.ttf"
                            color "#e8d5a0"
                            size 36
                            xalign 0.5

                        textbutton "▼":
                            xalign 0.5
                            background "#2d2720"
                            hover_background "#4a3c28"
                            padding (16, 8)
                            action SetScreenVariable(_digit_name, (_digit_var - 1) % 10)
                            text_color "#e8d5a0"
                            text_hover_color "#ffffff"
                            text_xalign 0.5

            hbox:
                xalign 0.5
                spacing 16

                textbutton "Submit":
                    background "#2d2720"
                    hover_background "#4a3c28"
                    padding (24, 10)
                    action Return((d1, d2, d3, d4))
                    text_color "#e8d5a0"
                    text_hover_color "#ffffff"
                    text_font "fonts/Typewriter.ttf"
                    text_size 17

                textbutton "Leave":
                    background "#1a1714"
                    hover_background "#2d2720"
                    padding (24, 10)
                    action Return("Leave")
                    text_color "#7a6a50"
                    text_hover_color "#c4b090"
                    text_font "fonts/Typewriter.ttf"
                    text_size 17


# ── Entry point (called from the village map loop) ────────────────────────────

label church_scene:
    call explore_node("church") from _call_church_root
    return


# ── Puzzle labels ─────────────────────────────────────────────────────────────

label church_backyard_box_puzzle:
    $ _box_solved = False
    while not _box_solved:
        call screen church_box_lock_screen()
        $ _asdf = _return
        if _asdf == "Leave":
            # Player left — remove from interacted_objects so the box stays clickable
            $ interacted_objects = set(x for x in interacted_objects if x != "church.backyard.lawn.box")
            return
        $ _d1, _d2, _d3, _d4 = _asdf
        if (_d1, _d2, _d3, _d4) == (1, 9, 3, 8):
            $ _photo = ITEM_CATALOG["church.backyard.lawn.photo_piece"]
            $ collected_items.add("church.backyard.lawn.photo_piece")
            $ journal_add_item("church.backyard.lawn.photo_piece", _photo["name"], _photo["location"], _photo["description"])
            "The lock clicks open."
            "Inside the box is a torn {color=#ff0000}{b}piece of a photo{/b}{/color} — it shows a man smiling."
            $ _box_solved = True
        else:
            "The lock doesn't budge. That's not the right combination."
    return


# ── Intro / unlock labels ─────────────────────────────────────────────────────

label church_intro:
    scene church at fit_screen
    with Dissolve(0.5)
    "The church looms at the edge of the square, its white walls stained by decades of rain."
    "Inside, rows of wooden pews face a simple altar."
    "Candles have been recently burned — the wax is still soft."
    return

label church_main_hall_intro:
    "You step into the main hall."
    "Pale light filters through the windows, casting long shadows across the pews."
    return

label church_backyard_intro:
    "The backyard stretches behind the church, enclosed by an old iron fence."
    "Headstones line the far wall, some so weathered the names are barely legible."
    return

label church_backyard_lawn_unlock:
    "You drive the shovel into the soil. The ground here is softer than it looks."
    "After a few scoops, the blade strikes something solid."
    return

label church_backyard_lawn_intro:
    "A patch of freshly turned soil. Half-buried in the dirt is a small wooden box."
    return
