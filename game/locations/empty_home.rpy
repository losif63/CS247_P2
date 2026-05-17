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
            "name":     "Empty Home",
            "parent":   None,
            "intro":    "empty_home_intro",
            "children": [
                "empty_home.living_room",
                "empty_home.backyard",
                "empty_home.basement_door",
            ],
            "puzzle":   None,
            "requires": None,
        },

        "empty_home.living_room": {
            "name":     "Living Room",
            "parent":   "empty_home",
            "intro":    "empty_home_living_room_intro",
            "children": [],
            "puzzle":   None,
            "requires": None,
        },

        "empty_home.backyard": {
            "name":     "Backyard",
            "parent":   "empty_home",
            "intro":    "empty_home_backyard_intro",
            "children": [],
            "puzzle":   None,
            "requires": None,
        },

        "empty_home.basement_door": {
            "name":     "Basement Door",
            "parent":   "empty_home",
            "intro":    "empty_home_basement_door_intro",
            "children": [],
            "puzzle":   None,
            "requires": None,
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

label empty_home_backyard_intro:
    "The backyard is overgrown, weeds swallowing what was once a tended vegetable garden."
    "A rusted watering can lies on its side by the door. The soil around it is dry and cracked."
    return

label empty_home_basement_door_intro:
    "A low door at the back of the kitchen. The handle is cold."
    "It doesn't budge. Locked from the other side, or jammed shut by something you can't see."
    return
