################################################################################
## Empty Home — Exploration Tree
##
## Tree structure:
##   empty_home
##   ├── empty_home.living_room
##   ├── empty_home.backyard
##   └── empty_home.basement_door
##
## To add a child to an existing node: add its ID to the parent's "children"
## list and add a new entry to EXPLORE_NODES. To add a puzzle, set "puzzle"
## to a label name and define that label below.
################################################################################

init python:
    EXPLORE_NODES.update({

        "empty_home": {
            "name":       "Empty Home",
            "parent":     None,
            "intro":      "empty_home_intro",
            "children":   [
                "empty_home.living_room",
                "empty_home.backyard",
                "empty_home.basement_door",
            ],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.living_room": {
            "name":       "Living Room",
            "parent":     "empty_home",
            "intro":      "empty_home_living_room_intro",
            "children":   ["empty_home.living_room.drawer", "empty_home.living_room.couch", "empty_home.living_room.table"],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.living_room.drawer": {
            "name":       "Drawer",
            "parent":     "empty_home.living_room",
            "intro":      "empty_home_living_room_drawer_intro",
            "children":   [],
            "objects": [
                {
                    "id":        "empty_home.living_room.drawer.top",
                    "name":      "Top Drawer",
                    "item":      None,
                    "action":    None,
                    "msg_first": "The top drawer slides open. Nothing but old receipts and a broken pen.",
                    "msg_done":  "Just old receipts.",
                },
                {
                    "id":        "empty_home.living_room.drawer.middle",
                    "name":      "Middle Drawer",
                    "item":      "empty_home.basement_door.key",
                    "action":    None,
                    "msg_first": "You find a small key taped to the back of the drawer.",
                    "msg_done":  "The middle drawer is empty.",
                },
                {
                    "id":        "empty_home.living_room.drawer.bottom",
                    "name":      "Bottom Drawer",
                    "item":      None,
                    "action":    None,
                    "msg_first": "Stuck. The bottom drawer won't budge no matter how hard you pull.",
                    "msg_done":  "Still stuck.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.living_room.couch": {
            "name":       "Couch",
            "parent":     "empty_home.living_room",
            "intro":      "empty_home_living_room_couch_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        # TODO: Add Puzzle
        "empty_home.living_room.table": {
            "name":       "Table",
            "parent":     "empty_home.living_room",
            "intro":      "empty_home_living_room_table_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "empty_home.living_room.table.picture",
                    "name":      "Family Photo",
                    "item":      None,
                    "action":    None,
                    "msg_first": "There is a photo frame lying on top of the table. The photo seems to be torn up - only a single piece remains. Perhaps something may happen if I find the other pieces and reassemble it?",
                    "msg_done":  "There is a photo frame lying on top of the table. The photo seems to be torn up - only a single piece remains. Perhaps something may happen if I find the other pieces and reassemble it?",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.backyard": {
            "name":       "Backyard",
            "parent":     "empty_home",
            "intro":      "empty_home_backyard_intro",
            "children":   ["empty_home.backyard.swing", "empty_home.backyard.garden"],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.backyard.swing": {
            "name":       "Swing",
            "parent":     "empty_home.backyard",
            "intro":      "empty_home_backyard_swing_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "empty_home.backyard.left_swing",
                    "name":      "Left Swing",
                    "item":      "empty_home.backyard.swing.photo",
                    "action":    None,
                    "msg_first": "There seems to be a piece of a photo lying on top of the seat. The piece shows a young girl smiling.",
                    "msg_done":  "There is nothing on the swing.",
                },
                {
                    "id":        "empty_home.backyard.right_swing",
                    "name":      "Right Swing",
                    "item":      None,
                    "action":    None,
                    "msg_first": "There is nothing on the swing.",
                    "msg_done":  "There is nothing on the swing.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.backyard.garden": {
            "name":       "Garden",
            "parent":     "empty_home.backyard",
            "intro":      "empty_home_backyard_garden_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.basement_door": {
            "name":       "Basement",
            "parent":     "empty_home",
            "intro":      "empty_home_basement_door_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "empty_home.basement.bookshelf",
                    "name":      "Bookshelf",
                    "item":      "empty_home.basement.diary",
                    "action":    None,
                    "msg_first": [
                        "There seems to be a bookshelf alongside the back wall of the basement.",
                        "An uncanny book immediately catches your eye - it says Sonia's Diary on the front cover.",
                        "You reach out your hand and turn the pages. It seems like this belonged to a girl a long time ago.",
                        '"April 15th, 1925."',
                        '"It was rainy today. Mommy also looked really sad. Maybe she doesn\'t like rain."',
                        '"I wanted to cheer mommy up, so we played hide and seek together!"',
                        '"Mommy played it. She told me to stay hidden in the basement - and that I should never come out no matter what, even if mommy calls me."',
                        '"So I hid in the basement and stayed there forever! Mommy never found me."',
                        '"I heard a lot of footsteps and shouting upstairs - it seems like mommy invited neighbors to play as well."',
                        '"After a few hours I became hungry, so I came out of the basement. Mommy was missing - and there were policemen around my house."',
                        '"I asked the policement where mommy and daddy is. He told me that daddy is at the city hall, and mommy went to the hospital because she was sick."',
                        '"I am starving. I hope she comes back soon."',
                        "You close the book. Seems like something nasty happened to her parents."
                    ],
                    "msg_done":  "There is nothing on the swing.",
                },
                {
                    "id":        "empty_home.basement.rack",
                    "name":      "Rack",
                    "item":      "empty_home.basement.shovel",
                    "action":    None,
                    "msg_first": "A wooden rack leans against the wall, holding a few old tools. A shovel hangs from one of the pegs — you take it.",
                    "msg_done":  "The rack is empty now.",
                },
            ],
            "puzzle":     None,
            "requires":   "empty_home.basement_door.key",
            "unlock":     "empty_home_basement_unlock",
            "locked_msg": "The door is locked. Perhaps there is a key somewhere?",
        },

    })

    ITEM_CATALOG.update({
        "empty_home.basement_door.key": {
            "name": "Basement Key",
            "location": "Empty Home - Living Room",
            "description": "Key that opens the basement door of the empty home."
        },

        "empty_home.basement.diary": {
            "name": "Sonia's Diary",
            "location": "Empty Home - Basement",
            "description": "Diary of a girl named Sonia. It states that her dad is at the city hall, and her mom is at the hospital."
        },

        "empty_home.backyard.swing.photo": {
            "name": "Photo Piece 3",
            "location": "Empty Home - Backyard",
            "description": "A piece of a torn photo. The piece shows a young girl smiling."
        },

        "empty_home.basement.shovel": {
            "name": "Shovel",
            "location": "Empty Home - Basement",
            "description": "An old shovel taken from a rack in the basement."
        },

    })


# ── Entry point (called from the village map loop) ────────────────────────────

label empty_home_scene:
    call explore_node("empty_home") from _call_empty_home_root
    return


# ── Intro labels (called once per node on first visit) ────────────────────────

label empty_home_intro:
    scene black
    with Dissolve(0.5)
    "The door to the empty home swings open at your touch — it wasn't locked."
    "A layer of dust coats everything. Furniture still in place, as if the occupants simply vanished."
    return

label empty_home_living_room_intro:
    "You step into the living room."
    "A sofa, a low table, a radio on the shelf — all arranged with a care that makes the emptiness worse."
    "A child's drawing is pinned to the wall. You don't want to look at it too long."
    return

label empty_home_living_room_drawer_intro:
    "You investigate the drawer at the corner of the living room."
    return

label empty_home_living_room_couch_intro:
    "You investigate the couch at the center of the living room."
    "It's quite old fashioned and heavily worn out."
    return

label empty_home_living_room_table_intro:
    "A table sits at the center of the living room."
    return

label empty_home_backyard_intro:
    "The backyard is overgrown, weeds swallowing what was once a tended vegetable garden."
    "A rusted watering can lies on its side by the door. The soil around it is dry and cracked."
    return

label empty_home_backyard_swing_intro:
    "There is an empty swing in the middle of the vegetable garden. You make your way through the weeds toward the swing."
    return

label empty_home_backyard_garden_intro:
    "There is a garden in the middle of the backyard - it seems that it hasn't been tended for years."
    "You notice weeds and all sorts of wild plants growing in the garden."
    return

label empty_home_basement_door_intro:
    "The basement is eerie and cold."
    return

label empty_home_basement_unlock:
    "You fit the key into the lock. It turns with a heavy click."
    "The door swings inward. Cold air rises from below."
    return
