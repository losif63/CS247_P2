image hospital_2f_nurses_station = "images/hospital2Fnursestation.png"

image hospital_basement_lostnfound = "images/hospitalbasementlostandfound.png"

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
            "on_enter":   "hospital_enter",
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
            "on_enter":   "hospital_basement_enter",
            "children":   [
                "hospital.basement.morgue"
            ],
            "objects":    [
                {
                    "id":        "hospital.basement.lostnfound",
                    "name":      "Lost & Found box",
                    "item":      None,
                    "action":    "hospital_basement_lostnfound_action",
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
            "objects":    [
                {
                    "id":        "hospital.ground_floor.intake_desk",
                    "name":      "Intake Desk",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "A stack of intake forms sits on the reception desk, the top one half-filled.",
                        "Beside the usual fields — name, age, symptoms — there is a printed box marked 'Classification.'",
                        "A note clipped to the stack instructs staff to assign wards 'according to classification,' with native patients directed to a separate wing at the rear.",
                        "Even sickness, it seems, was sorted by who the colony decided you were.",
                    ],
                    "msg_done":  "Intake forms that sorted the sick by 'classification.'",
                },
                {
                    "id":        "hospital.ground_floor.exam_room",
                    "name":      "Examination Room",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "The first examination room is frozen mid-use — an overturned cup, a paper gown still on the table.",
                        "A faded public-health poster hangs crooked on the wall, printed only in the colonisers' language.",
                        "It lectures the villagers on 'modern hygiene' in cheerful, condescending cartoons, as if their own remedies had never kept them alive for centuries.",
                    ],
                    "msg_done":  "An exam room and a poster that talked down to the dying.",
                },
                {
                    "id":        "hospital.ground_floor.supply_cabinet",
                    "name":      "Supply Cabinet",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "The supply cabinet hangs open, all but emptied.",
                        "A rationing ledger is still tacked to the inside of the door.",
                        "Medicine was issued by priority. The first column — 'staff and administration' — is full. The last column, for the general ward, trails off into dashes.",
                    ],
                    "msg_done":  "An empty cabinet and a ledger that rationed mercy.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "hospital.2f": {
            "name":       "2F",
            "parent":     "hospital",
            "intro":      "hospital_2f_intro",
            "on_enter":   "hospital_2f_enter",
            "children":   [],
            "objects":    [
                {
                    "id":        "hospital.2f.ward_signage",
                    "name":      "Ward Signage",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "Two painted signs mark the corridors that branch from the landing.",
                        "One, elegant and gilded, reads 'European Ward,' pointing toward the wide, bright hall.",
                        "The other, stencilled in plain block letters, reads 'Native Ward,' pointing down a narrower passage with lower ceilings and no windows.",
                        "The same building. Two entirely different ideas of who deserved to heal in the light.",
                    ],
                    "msg_done":  "Two wards, divided by paint and by worth.",
                },
                {
                    "id":        "hospital.2f.belongings",
                    "name":      "Patients' Belongings",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "The patient rooms still hold what people left behind — beds made, as though everyone simply walked out.",
                        "A pair of child's slippers tucked under a cot. A worn rosary on a windowsill. A comb, a folded shawl, a half-eaten tin of sweets.",
                        "Small, ordinary things, waiting for owners who never came back to claim them.",
                    ],
                    "msg_done":  "Ordinary belongings, still waiting.",
                },
                {
                    "id":        "hospital.2f.nurses_station",
                    "name":      "Nurses' Station",
                    "item":      None,
                    "action":    "hospital_nurses_station_action",
                    "msg_first": [
                        "The nurses' station is tidy, the duty roster still chalked on the board.",
                        "A nurse's notebook lies open beneath it. The early entries are careful, professional.",
                        "Then the tone changes: 'Told again not to record certain admissions. Told not to ask where they go.'",
                        "The final entry stops mid-sentence: 'I don't think I can keep pretending that I—'",
                    ],
                    "msg_done":  "A nurse's notebook, abandoned mid-confession.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "hospital.3f": {
            "name":       "3F",
            "parent":     "hospital",
            "intro":      "hospital_3f_intro",
            "on_enter":   "hospital_3f_enter",
            "children":   [],
            "objects":    [
                {
                    "id":        "hospital.3f.locked_room",
                    "name":      "Locked Room",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "You try the handle of the room at the end of the hall. It's locked — and not with a missing key, but padlocked shut from the outside and painted over years ago.",
                        "The light beneath the door is only a dead emergency lamp, flickering on its last reserve.",
                        "Through the gap you can make out stacked chairs and equipment under dust sheets. A ward closed down long before the village emptied.",
                        "Whatever this place was, it has been sealed and forgotten. There's no way in, and nothing here waiting for you.",
                    ],
                    "msg_done":  "The room stays sealed. Just an old ward, shut and painted over.",
                },
                {
                    "id":        "hospital.3f.staff_room",
                    "name":      "Staff Room",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "A cramped staff room: a cold kettle, mismatched cups, a calendar years out of date.",
                        "A postcard is pinned above the sink, sent by a nurse who transferred to the capital.",
                        "'Don't envy me the city,' she wrote, 'but I won't pretend I'm sorry to have left. Some places ask you to see too much.'",
                    ],
                    "msg_done":  "A break room and a postcard from someone glad to be gone.",
                },
                {
                    "id":        "hospital.3f.window",
                    "name":      "Corridor Window",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "From the third-floor window the whole village lies spread out below in the failing light.",
                        "The grand colonial buildings cluster along the paved square — the hall, the church, the museum, all stone and symmetry.",
                        "Behind them, the old native quarter sprawls in crooked lanes the planners never bothered to straighten.",
                        "Even from up here, you can read the whole history of this place in how it was built.",
                    ],
                    "msg_done":  "The village below, its history written in its streets.",
                },
            ],
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
    scene hospital at fit_screen
    with Dissolve(0.5)
    "The hospital is the newest building in the village, though that's not saying much."
    "The corridors are empty and the lights flicker. Supply cabinets hang open, half-emptied."
    "You find a patient log left on the front desk. The last entry is dated three weeks ago."
    return

label hospital_basement_intro:
    scene hospital_basement at fit_screen
    with Dissolve(0.5)
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
    scene hospital_2f at fit_screen
    with Dissolve(0.5)
    "The second floor is lined with patient rooms."
    "Most doors are open. Beds still made, as though the patients simply walked away."
    return

label hospital_3f_intro:
    scene hospital_3f at fit_screen
    with Dissolve(0.5)
    "The third floor is quieter than the rest."
    "A locked room at the end of the hall has light bleeding under the door."
    return


# ── On-enter labels (fire every visit to restore the correct floor background) ──

label hospital_enter:
    scene hospital at fit_screen
    with Dissolve(0.3)
    return

label hospital_basement_enter:
    scene hospital_basement at fit_screen
    with Dissolve(0.3)
    return

label hospital_2f_enter:
    scene hospital_2f at fit_screen
    with Dissolve(0.3)
    return

label hospital_3f_enter:
    scene hospital_3f at fit_screen
    with Dissolve(0.3)
    return

label hospital_nurses_station_action:
    show hospital_2f_nurses_station at fit_screen
    with Dissolve(0.5)
    "The nurses' station is tidy, the duty roster still chalked on the board."
    "A nurse's notebook lies open beneath it. The early entries are careful, professional."
    "Then the tone changes: 'Told again not to record certain admissions. Told not to ask where they go.'"
    "The final entry stops mid-sentence: 'I don't think I can keep pretending that I—'"
    hide hospital_2f_nurses_station
    with Dissolve(0.3)
    return

label hospital_basement_lostnfound_action:
    scene hospital_basement_lostnfound at fit_screen
    with Dissolve(0.5)

    "There is a lost and found box."
    "You notice there are three pairs of shoes - but overall nothing interesting."

    scene hospital_basement at fit_screen
    with Dissolve(0.3)
    return 