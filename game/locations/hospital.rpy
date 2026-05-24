################################################################################
## Hospital — Exploration Tree
##
## Tree structure:
##   hospital
##   ├── hospital.basement
##   ├── hospital.ground_floor
##   ├── hospital.2f
##   └── hospital.3f
##
## To add a child to an existing node: add its ID to the parent's "children"
## list and add a new entry to EXPLORE_NODES. To add a puzzle, set "puzzle"
## to a label name and define that label below.
################################################################################


init python:
    EXPLORE_NODES.update({

        "hospital": {
            "name":       "Hospital",
            "parent":     None,
            "intro":      "hospital_intro",
            "children":   [
                "hospital.basement",
                "hospital.ground_floor",
                "hospital.2f",
                "hospital.3f",
            ],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "hospital.basement": {
            "name":       "Basement",
            "parent":     "hospital",
            "intro":      "hospital_basement_intro",
            "children":   [
                "hospital.basement.morgue"
            ],
            "objects":    [
                {
                    "id":        "hospital.basement.lostnfound",
                    "name":      "Lost & Found box",
                    "item":      None,
                    "action":    None,
                    "msg_first": ["There is a lost and found box.", "You notice there are three pairs of shoes - but overall nothing interesting."],
                    "msg_done":  "There is nothing interesting in the lost & found box.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "hospital.basement.morgue": {
            "name":       "Morgue",
            "parent":     "hospital.basement",
            "intro":      "hospital_basement_morgue_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "hospital.basement.morgue.mateo",
                    "name":      "Mateo Salvador",
                    "item":      None,
                    "action":    None,
                    "msg_first": ["You approach a unit named Mateo Salvador.", "There seems to be nothing in it."],
                    "msg_done":  "There is nothing in the unit.",
                },
                {
                    "id":        "hospital.basement.morgue.ari",
                    "name":      "Ari Wirakusuma",
                    "item":      None,
                    "action":    None,
                    "msg_first": ["You approach a unit named Ari Wirakusuma.", "There seems to be nothing in it."],
                    "msg_done":  "There is nothing in the unit.",
                },
                {
                    "id":        "hospital.basement.morgue.emilia",
                    "name":      "Emilia Gonzalez",
                    "item":      "hospital.basement.morgue.emilia.photo",
                    "action":    None,
                    "msg_first": ["You approach a unit named Emlia Gonzalez.", "There seems to be a {color=#ff0000}{b}piece of a photo{/b}{/color} inside the unit.", "The piece shows a woman smiling."],
                    "msg_done":  "There is nothing in the unit.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "hospital.ground_floor": {
            "name":       "Ground Floor",
            "parent":     "hospital",
            "intro":      "hospital_ground_floor_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "hospital.2f": {
            "name":       "2F",
            "parent":     "hospital",
            "intro":      "hospital_2f_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "hospital.3f": {
            "name":       "3F",
            "parent":     "hospital",
            "intro":      "hospital_3f_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

    })

    ITEM_CATALOG.update({
        "hospital.basement.morgue.emilia.photo": {
            "name": "Photo Piece 2",
            "location": "Hospital - Morgue",
            "description": "A piece of a torn photo. The piece shows a woman smiling."
        }
    })


# ── Entry point (called from the village map loop) ────────────────────────────

label hospital_scene:
    call explore_node("hospital") from _call_hospital_root
    return


# ── Intro labels (called once per node on first visit) ────────────────────────

label hospital_intro:
    scene black
    with Dissolve(0.5)
    "The hospital is the newest building in the village, though that's not saying much."
    "The corridors are empty and the lights flicker. Supply cabinets hang open, half-emptied."
    "You find a patient log left on the front desk. The last entry is dated three weeks ago."
    return

label hospital_basement_intro:
    "You descend the stairs into the basement."
    "The air is cold and damp. Pipes run along the ceiling, some wrapped in old cloth."
    return

label hospital_basement_morgue_intro:
    "You enter the morgue located at a corner of the basement."
    "The morgue is overall empty. However there are three units that have name tags on them."
    "The bodies aren't stored in the morgue - it seems they removed the bodies but forgot to remove the name tags."
    return

label hospital_ground_floor_intro:
    "The ground floor holds the reception desk and examination rooms."
    "Everything has been left mid-use — a half-filled intake form, an overturned cup."
    return

label hospital_2f_intro:
    "The second floor is lined with patient rooms."
    "Most doors are open. Beds still made, as though the patients simply walked away."
    return

label hospital_3f_intro:
    "The third floor is quieter than the rest."
    "A locked room at the end of the hall has light bleeding under the door."
    return
