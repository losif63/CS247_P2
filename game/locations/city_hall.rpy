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
            "objects":    [
                {
                    "id":        "city_hall.ground_floor.cabinets",
                    "name":      "Filing Cabinets",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "The cabinets are stuffed with permits — thousands of them, all stamped and counter-stamped.",
                        "A permit to travel to the next village. A permit to hold a wedding. A permit to gather more than five people after dark.",
                        "Under the colonial administration, it seems, simply living required someone's signature.",
                        "Most of the applications are marked with the same word: {i}Denied.{/i}",
                    ],
                    "msg_done":  "Drawers of permits, most of them denied.",
                },
                {
                    "id":        "city_hall.ground_floor.notice_board",
                    "name":      "Public Notice Board",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "Layers of proclamations are pinned over one another, the oldest yellowed almost to nothing.",
                        "A curfew order. A reward offered for information on 'agitators and seditionists.' A decree that all official business be conducted in the colonisers' language.",
                        "Pasted crookedly over them all is a newer bulletin, hand-printed in the local tongue: a single line announcing the village's independence.",
                        "Someone tore the corner of it off. Whether in anger or to keep, you can't tell.",
                    ],
                    "msg_done":  "Old decrees buried under a newer, hopeful one.",
                },
                {
                    "id":        "city_hall.ground_floor.clerks_desk",
                    "name":      "Clerk's Desk",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "A clerk's desk, abandoned mid-task. An official seal lies on its side beside a dried-out ink pad.",
                        "A half-finished form rejects a family's petition to recover a relative 'taken for questioning.'",
                        "The reason for denial is pre-printed. The clerk only had to sign.",
                    ],
                    "msg_done":  "Just an old desk and a seal that once decided lives.",
                },
            ],
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
            "objects":    [
                {
                    "id":        "city_hall.2f.council_table",
                    "name":      "Council Table",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "The long table is still set for a meeting that never resumed. Bound minutes lie at each place.",
                        "You leaf through one. The language is calm, procedural — agenda items and motions carried.",
                        "Item four: a 'labour shortfall' in the groves, resolved by 'reassigning' two neighbouring villages.",
                        "Item seven: a complaint about the smell from the river, tabled for next session.",
                        "Whole communities and a bad smell, weighed on the same page in the same flat hand.",
                    ],
                    "msg_done":  "Council minutes, where atrocities share the page with petty business.",
                },
                {
                    "id":        "city_hall.2f.private_office",
                    "name":      "Private Office",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "An administrator's private office, grander than the rest. A half-written letter sits on the blotter.",
                        "It is addressed home, across the sea. He complains of the heat, of the food, of 'these people and their endless grievances.'",
                        "He misses his children. He has framed their portrait on the desk, facing his chair.",
                        "He signs off promising to be home by spring. You wonder if he ever was.",
                    ],
                    "msg_done":  "A homesick letter from a man who governed a place he despised.",
                },
                {
                    "id":        "city_hall.2f.survey_map",
                    "name":      "Survey Map",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "A vast survey map covers one wall, the village and its surroundings drawn in meticulous detail.",
                        "Every river, hill, and settlement has been given a new name in the colonisers' language.",
                        "Beneath each, in smaller faded lettering, the original local names have been struck through with a single ruled line.",
                        "To remake a place, first you rename it.",
                    ],
                    "msg_done":  "A map that renamed everything it touched.",
                },
            ],
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
                    "msg_first": "The rubber plantation brought the city a lot of profit in 1920.",
                    "msg_done": "You've already viewed this report."
                },
                {
                    "id":        "city_hall.3f.archiveroom_financial.1921",
                    "name":      "1921",
                    "item":      None,
                    "action":    None,
                    "msg_first": "The files in this report seems to be missing for some reason.",
                    "msg_done": "You've already viewed this report."
                },
                {
                    "id":        "city_hall.3f.archiveroom_financial.1922",
                    "name":      "1922",
                    "item":      None,
                    "action":    None,
                    "msg_first": "The city suffered from massive deficits due to a record-breaking flood that year.",
                    "msg_done": "You've already viewed this report."
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
                    "msg_first": [
                        "The plantation produced 67 tons of rubber in 1920.",
                        "...those numbers seem useless."
                    ],
                    "msg_done": "You've already viewed this report."
                },
                {
                    "id":        "city_hall.3f.archiveroom_rubber.1921",
                    "name":      "1921",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "The plantation produced 59 tons of rubber in 1921.",
                        "...those numbers seem useless."
                    ],
                    "msg_done": "You've already viewed this report."
                },
                {
                    "id":        "city_hall.3f.archiveroom_rubber.1922",
                    "name":      "1922",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "The plantation didn't operate in 1922 due to a catastrophic flood."
                    ],
                    "msg_done": "You've already viewed this report."
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
                    "item":      "city_hall.joaquin_page",
                    "action":    "city_hall_joaquin_page_action",
                    "msg_first": "",
                    "msg_done":  "You already took this page."
                },
                {
                    "id":        "city_hall.3f.archiveroom_interrogation_teodora",
                    "name":      "Teodora Salvacion",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "Name: Teodora Salvacion.",
                        "Arrested For: Treason. Acted as a spy for independence rebels.",
                        "Interrogation Method: Physical force. Suspect was bound to a chair and was struck multiple times in the head with a blunt instrument."
                        "Fingernails were extracted using scissors...",
                        "Notes: ... Interrogation unsuccesful. Suspect perished before revealing any info.",
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
                        "Interrogation Method: Water torture. Hang susepct upside down and pour water into his nose while stamping his abdomen.",
                        "Notes: (scribbles)",
                    ],
                    "msg_done": "You already viewed this entry."
                },
                {
                    "id":        "city_hall.3f.archiveroom_interrogation_execution",
                    "name":      "Execution",
                    "item":      "city_hall.execution_page",
                    "action":    "city_hall_execution_page_action",
                    "msg_first": "",
                    "msg_done":  "You already took this page."
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },
    })

    ITEM_CATALOG.update({
        "city_hall.joaquin_page": {
            "name":        "Torn Interrogation Record",
            "location":    "City Hall - Archive Room",
            "description": "A page torn from the colonial interrogation files. Records Joaquin Gonzalez's arrest for instigating independence riots — A number is scrawled in the margin: {b}1938{/b}.",
        },
        "city_hall.execution_page": {
            "name":        "Torn Execution Record",
            "location":    "City Hall - Archive Room",
            "description": "A classified page torn from the execution records. All targets executed on a redacted date. States that Joaquin Gonzalez was buried at the {color=#ffff00}{b}church backyard{/b}{/color}.",
        },
    })


# ── Entry point (called from the village map loop) ────────────────────────────

label town_hall_scene:
    call explore_node("city_hall") from _call_city_hall_root
    return


# ── Intro labels (called once per node on first visit) ────────────────────────

label city_hall_intro:
    scene townhall at fit_screen
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

label city_hall_bayani_note_action:
    if bayaniNoteRead:
        "You've already read Bayani's note."
        return

    $ bayaniNoteRead = True
    $ journal_add_item(
        "city_hall.bayani_margin_note",
        "Bayani's Margin Note",
        "City Hall - Archive Room",
        "A note in Bayani Magtanggol's interrogation record reads: 'Water returns what ink refuses.'"
    )
    "You trace the scribbled note carefully."
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


# ── Object action labels ──────────────────────────────────────────────────────

label city_hall_execution_page_action:
    "CLASSIFIED INFORMATION"
    "All targets were executed on 19__/__/__."
    "Joaquin Gonzalez was buried at the {color=#ffff00}{b}church backyard{/b}{/color}."
    "..."
    "You tear the {color=#ff0000}{b}page{/b}{/color}  from the file and pocket it."
    return


label city_hall_joaquin_page_action:
    "Name: Joaquin Gonzalez."
    "Arrested For: Instigating independence riots."
    "Interrogation Method: Electrocution."
    "Notes: (blahblah)"
    "Confessed: {b}1938{/b}"
    "(scribbles)"
    "The number {b}1938{/b} catches your eye. This seems important."
    "You tear the {color=#ff0000}{b}page{/b}{/color} from the file and pocket it."
    return