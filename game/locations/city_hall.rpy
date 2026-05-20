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
            "children":   ["city_hall.3f.archive_room"],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "city_hall.3f.archive_room": {
            "name":       "Archive Room",
            "parent":     "city_hall.3f",
            "intro":      "city_hall_3f_archiveroom_intro",
            "children":   [
                "city_hall.3f.archive_room.annual_financial_report",
                "city_hall.3f.archive_room.annual_rubber_production",
                "city_hall.3f.archive_room.terrorist_interrogation",
            ],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },
        
        "city_hall.3f.archive_room.annual_financial_report": {
            "name":       "Annual Financial Reports",
            "parent":     "city_hall.3f.archive_room",
            "intro":      "city_hall_3f_archiveroom_financial_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "city_hall.3f.archiveroom_financial.1920",
                    "name":      "1920",
                    "item":      None,
                    "action":    None,
                    "msg_first": "just a lot of numbers...",
                    "msg_done": "just a lot of numbers..."
                },
                {
                    "id":        "city_hall.3f.archiveroom_financial.1921",
                    "name":      "1921",
                    "item":      None,
                    "action":    None,
                    "msg_first": "just a lot of numbers...",
                    "msg_done": "just a lot of numbers..."
                },
                {
                    "id":        "city_hall.3f.archiveroom_financial.1922",
                    "name":      "1922",
                    "item":      None,
                    "action":    None,
                    "msg_first": "just a lot of numbers...",
                    "msg_done": "just a lot of numbers..."
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },
        
        "city_hall.3f.archive_room.annual_rubber_production": {
            "name":       "Annual Rubber Production Status",
            "parent":     "city_hall.3f.archive_room",
            "intro":      "city_hall_3f_archiveroom_interrogation_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "city_hall.3f.archiveroom_rubber.1920",
                    "name":      "1920",
                    "item":      None,
                    "action":    None,
                    "msg_first": "just a lot of numbers...",
                    "msg_done": "just a lot of numbers..."
                },
                {
                    "id":        "city_hall.3f.archiveroom_rubber.1921",
                    "name":      "1921",
                    "item":      None,
                    "action":    None,
                    "msg_first": "just a lot of numbers...",
                    "msg_done": "just a lot of numbers..."
                },
                {
                    "id":        "city_hall.3f.archiveroom_rubber.1922",
                    "name":      "1922",
                    "item":      None,
                    "action":    None,
                    "msg_first": "just a lot of numbers...",
                    "msg_done": "just a lot of numbers..."
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "city_hall.3f.archive_room.terrorist_interrogation": {
            "name":       "Terrorist Interrogation",
            "parent":     "city_hall.3f.archive_room",
            "intro":      "city_hall_3f_archiveroom_interrogation_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "city_hall.3f.archiveroom_interrogation.joaquin",
                    "name":      "Joaquin Gonzalez",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "Name: Joaquin Gonzalez.",
                        "Arrested For: Instigating independence riots.",
                        "Interrogation Method: 3A",
                        "Notes: (blahblah) ~ 1938 ~ (scribbles)",
                        "The number 1938 catches your eye."
                    ],
                    "msg_done": "The number 1938 stands out."
                },
                {
                    "id":        "city_hall.3f.archiveroom_interrogation_teodora",
                    "name":      "Teodora Salvacion",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "Name: Teodora Salvacion.",
                        "Arrested For: Treason. Acted as a spy for independence rebels.",
                        "Interrogation Method: 7G.",
                        "Notes: (scribbles)",
                    ],
                    "msg_done": "You already viewed this entry."
                },
                {
                    "id":        "city_hall.3f.archiveroom_interrogation_bayani",
                    "name":      "Bayani Magtanggol",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "Name: Bayani Magtanggol.",
                        "Arrested For: Assasination of military general.",
                        "Interrogation Method: 1A.",
                        "Notes: (scribbles)",
                    ],
                    "msg_done": "You already viewed this entry."
                },
                {
                    "id":        "city_hall.3f.archiveroom_interrogation_execution",
                    "name":      "Execution",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "CLASSIFIED INFORMATION",
                        "All targets were executed on 19__/__/__.",
                        "Joaquin Gonazlez was buried at the church backyard.",
                        "...",
                    ],
                    "msg_done": "It states Joaquin Gonzalez was buried at the church backyard."
                },
            ],
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

label city_hall_3f_archiveroom_intro:
    "You enter the archive room located at a corner."
    "You are greeted by a pile of documents. It seems the place keeps records for almost all colonial activities."
    "Now, where to look..."
    return

label city_hall_3f_archiveroom_financial_intro:
    "This book seems to have archived the city's financial status during the colonial era."
    return

label city_hall_3f_archiveroom_rubber_intro:
    "This book seems to have archived the city's rubber production status during the colonial era."
    return

label city_hall_3f_archiveroom_interrogation_intro:
    "This book seems to have archived the city's rubber production status during the colonial era."
    return