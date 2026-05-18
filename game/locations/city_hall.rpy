################################################################################
## City Hall — Exploration Tree
##
## Tree structure:
##   city_hall
##   ├── city_hall.ground_floor
##   ├── city_hall.2f
##   └── city_hall.3f
##
## To add a child to an existing node: add its ID to the parent's "children"
## list and add a new entry to EXPLORE_NODES. To add a puzzle, set "puzzle"
## to a label name and define that label below.
################################################################################


init python:
    EXPLORE_NODES.update({

        "city_hall": {
            "name":       "City Hall",
            "parent":     None,
            "intro":      "city_hall_intro",
            "children":   [
                "city_hall.ground_floor",
                "city_hall.2f",
                "city_hall.3f",
            ],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "city_hall.ground_floor": {
            "name":       "Ground Floor",
            "parent":     "city_hall",
            "intro":      "city_hall_ground_floor_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "city_hall.2f": {
            "name":       "2F",
            "parent":     "city_hall",
            "intro":      "city_hall_2f_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "city_hall.3f": {
            "name":       "3F",
            "parent":     "city_hall",
            "intro":      "city_hall_3f_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

    })


# ── Entry point (called from the village map loop) ────────────────────────────

label town_hall_scene:
    call explore_node("city_hall") from _call_city_hall_root
    return


# ── Intro labels (called once per node on first visit) ────────────────────────

label city_hall_intro:
    scene black
    with Dissolve(0.5)
    "You push open the heavy doors of the city hall."
    "Dusty portraits of colonial administrators line the walls, staring down with cold, flat eyes."
    "Old ledgers and records are scattered across the main desk."
    return

label city_hall_ground_floor_intro:
    "The ground floor holds the main hall and public offices."
    "Filing cabinets line the walls, most left open. Papers are scattered across every desk."
    return

label city_hall_2f_intro:
    "The second floor is quieter — private offices and meeting rooms."
    "A long table dominates the central room, chairs still arranged as though a meeting was just interrupted."
    return

label city_hall_3f_intro:
    "The third floor is restricted access, according to the sign at the stairwell."
    "The sign has been torn halfway off. No one is here to stop you."
    return
