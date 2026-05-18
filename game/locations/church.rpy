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
                    "id":        "church.backyard.lawn.photo",
                    "name":      "Something Buried",
                    "item":      "church.backyard.lawn.photo_piece",
                    "action":    None,
                    "msg_first": "You dig into the loose soil. The shovel strikes something hard — a small tin box. Inside is a torn piece of a photo. The piece shows a man smiling.",
                    "msg_done":  "There is nothing else buried here.",
                },
            ],
            "puzzle":     None,
            "requires":   "empty_home.basement.shovel",
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


# ── Entry point (called from the village map loop) ────────────────────────────

label church_scene:
    call explore_node("church") from _call_church_root
    return


# ── Intro labels (called once per node on first visit) ────────────────────────

label church_intro:
    scene black
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
    return

label church_backyard_lawn_intro:
    "A patch of lawn sits in the corner of the backyard, the soil visibly disturbed."
    return
