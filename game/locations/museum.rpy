################################################################################
## Museum — Exploration Tree
##
## The museum is the village's "hint hub." Each wing presents a sanitised
## colonial-era exhibit that, read against the grain, points the player toward
## one of the investigation locations:
##
##   museum
##   ├── museum.disappearances   → hints at the EMPTY HOME (people taken; homes
##   │                              left abandoned; tortured/executed elsewhere)
##   ├── museum.forced_labor     → hints at the RUBBER PLANTATION (locals enslaved,
##   │                              reduced to numbers and quotas)
##   └── museum.spring_display   → hints at the MANGROVE SPRING / mirror pool
##                                  (also holds the Spring Fragments clue)
##
## To add a child to an existing node: add its ID to the parent's "children"
## list and add a new entry to EXPLORE_NODES. To add a display, append an object
## to the relevant node's "objects" list.
################################################################################


init python:
    EXPLORE_NODES.update({

        "museum": {
            "name":       "Museum",
            "parent":     None,
            "intro":      "museum_intro",
            "children":   [
                "museum.disappearances",
                "museum.forced_labor",
                "museum.spring_display",
            ],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        # ── Wing 1: points toward the EMPTY HOME ──────────────────────────────
        "museum.disappearances": {
            "name":       "Resettlement Wing",
            "parent":     "museum",
            "intro":      "museum_disappearances_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "museum.disappearances.photographs",
                    "name":      "Resettlement Photographs",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "A row of faded photographs shows entire streets of houses, doors standing open.",
                        "The placard explains: {i}During the period of pacification, many households were peacefully resettled for their own protection.{/i}",
                        "\"Resettled.\" The word does a lot of work.",
                        "In photo after photo the homes are intact — furniture, washing on the line — but no people. As if everyone simply stepped out and never came back.",
                        "Half the village still stands empty because of this. If you want to know what really happened to a family, you would have to walk into one of those {color=#ffff00}{b}empty homes{/b}{/color} yourself.",
                    ],
                    "msg_done":  "Rows of open doors and empty houses. Nobody chose to leave them.",
                },
                {
                    "id":        "museum.disappearances.implements",
                    "name":      "Instruments of Order",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "A locked case displays restraints, batons, and surgical-looking tools, all neatly mounted.",
                        "The label calls them {i}implements used to maintain civil order.{/i}",
                        "It does not say that the people taken from those homes were brought somewhere to be questioned — and that almost none of them came home.",
                        "Those who were 'questioned' ended up in the records at the city hall. Those who died were buried, or worse, sent to the hospital.",
                    ],
                    "msg_done":  "The tools of 'order' gleam behind glass, their true use politely unlabelled.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        # ── Wing 2: points toward the RUBBER PLANTATION ───────────────────────
        "museum.forced_labor": {
            "name":       "The Rubber Trade",
            "parent":     "museum",
            "intro":      "museum_forced_labor_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "museum.forced_labor.ledger",
                    "name":      "Plantation Ledger",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "A thick ledger lies open under glass, every line a worker reduced to a number and a column of figures.",
                        "It seems like documents used for keeping track of local workers who were exploited at the {color=#ffff00}{b}Rubber Plantation{/b}{/color}."
                        "The placard praises it as {i}a model of modern plantation efficiency.{/i}",
                        "There are no names. Only IDs, daily outputs, and curt notes: {i}Quotas unmet. Unfit for labor. Deceased.{/i}",
                        "People, kept like inventory. The plantation itself still stands at the edge of the village — and ledgers like this one would still be out there.",
                    ],
                    "msg_done":  "The ledger lists people the way you would list crates of rubber.",
                },
                {
                    "id":        "museum.forced_labor.tag",
                    "name":      "Worker's Tag",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "A small metal tag stamped with a five-digit number hangs on a frayed cord.",
                        "The label: {i}Identification issued to plantation labourers.{/i}",
                        "Not a name. A number — the same kind stamped into that ledger.",
                        "Whole families were worked to death under tags like this. Their story is written in the records still kept out at the rubber plantation.",
                    ],
                    "msg_done":  "A number where a name should be.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        # ── Wing 3: points toward the MANGROVE SPRING (mirror pool) ────────────
        "museum.spring_display": {
            "name":       "The Mangrove Spring",
            "parent":     "museum",
            "intro":      "museum_spring_display_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "museum.spring_display.exhibit",
                    "name":      "Spring Display",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "A small exhibit describes the {color=#ffff00}{b}Mangrove Spring{/b}{/color} at the village's edge — the place the tour brochures call the Mirror Pool.",
                        "The placard frames it as {i}a scenic curiosity, popular with visitors.{/i}",
                        "But the older photographs show villagers leaving offerings there, and a carved marker standing at the water's edge.",
                        "Whatever that marker once said, it clearly mattered to the people here. The spring itself is still out there, waiting.",
                    ],
                    "msg_done":  "The mangrove spring — a place of memory, sold to tourists as a postcard.",
                },
                {
                    "id":        "museum.spring_display.fragments",
                    "name":      "Spring Fragments",
                    "item":      None,
                    "action":    "museum_spring_fragments_action",
                    "msg_first": "",
                    "msg_done":  "The three fragments sit under glass: MOTHER, SPRING, REMEMBERS.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

    })


# ── Entry point (called from the village map loop) ────────────────────────────

label museum_scene:
    call explore_node("museum") from _call_museum_root
    return


# ── Intro labels (called once per node on first visit) ────────────────────────

label museum_intro:
    scene museum at fit_screen
    with Dissolve(0.5)
    "The village museum is small but unsettling."
    "Glass cases display artifacts — masks, farming tools, ceremonial objects — each stripped of their original meaning by sterile labels."
    "Something about this place feels wrong. As if it was built to explain the village away rather than remember it."
    "Three wings branch off the main hall. Each one, you suspect, is hiding more than it shows."
    return

label museum_disappearances_intro:
    "This wing is titled {i}Pacification & Resettlement.{/i}"
    "It tells a tidy story of villages calmly relocated. The photographs on the walls tell a different one."
    return

label museum_forced_labor_intro:
    "This wing celebrates {i}The Rubber Trade{/i} that once made the colony rich."
    "Polished tools, proud figures, and not one word about who actually bled for it."
    return

label museum_spring_display_intro:
    "A quieter alcove at the back of the museum is given over to the village's natural landmarks."
    "Most of the space is taken up by a single neglected case near the wall."
    return


# ── Object action labels ──────────────────────────────────────────────────────

label museum_spring_fragments_action:
    if not signMarksRevealed:
        $ interacted_objects = set(x for x in interacted_objects if x != "museum.spring_display.fragments")
        "The case is locked."
        "Inside are three weathered fragments tagged with catalog numbers, but without context, they feel like museum clutter."
        "You make a note to come back if you find something that makes the labels matter."
        return
    "You find a case of stone fragments labeled Spring Marker Fragments."
    "The labels match the marks from the sign: S-03, S-08, and S-14."
    "These are not random pieces."
    "They look like broken parts of an older sign — one that existed before this place was renamed Mirror Pool."
    "Each fragment has part of a word carved into it."
    "The museum label says the pieces were recovered during redevelopment and later archived as historical material."
    "But the way they are displayed makes them feel disconnected from the spring itself."
    "Something about this feels wrong."
    "These fragments were not just artifacts. They were part of the spring's original name."
    "Fragment S-03 shows the word: {b}MOTHER{/b}."
    "Fragment S-08 shows the word: {b}SPRING{/b}."
    "Fragment S-14 shows the word: {b}REMEMBERS{/b}."
    "Together, they read: {b}MOTHER SPRING REMEMBERS{/b}."
    "That must be the name the sign was hiding."
    if not museumFragmentsFound:
        $ museumFragmentsFound = True
        $ journal_add_item(
            "museum.spring_fragments",
            "Museum Fragment Notes",
            "Museum",
            "The numbers on the sign match museum catalog labels. The museum fragments appear to be broken pieces of the original Mother Spring marker. The tourist sign did not create the message — it covered it."
        )
    return
