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

        "empty_home.living_room.table": {
            "name":       "Table",
            "parent":     "empty_home.living_room",
            "intro":      "empty_home_living_room_table_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.backyard": {
            "name":       "Backyard",
            "parent":     "empty_home",
            "intro":      "empty_home_backyard_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.basement_door": {
            "name":       "Basement Door",
            "parent":     "empty_home",
            "intro":      "empty_home_basement_door_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   "empty_home.basement_door.key",
            "unlock":     "empty_home_basement_unlock",
            "locked_msg": "The door is locked. Perhaps there is a key somewhere?",
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

label empty_home_basement_door_intro:
    "The basement is eerie and cold."
    return

label empty_home_basement_unlock:
    "You fit the key into the lock. It turns with a heavy click."
    "The door swings inward. Cold air rises from below."
    return
