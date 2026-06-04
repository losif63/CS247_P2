image museum_pacification_wing   = "images/museum/pacification.png"
image museum_pacification_photos = "images/museum/museum-pacification-photos.png"
image museum_pacification_tools  = "images/museum/museum-pacification-tools.png"
image museum_rubber_trade        = "images/museum/rubber.png"
image museum_rubber_ledger       = "images/museum/museum-rubber-ledger.png"
image museum_rubber_tag          = "images/museum/museum-rubber-tag.png"
image museum_mangrove            = "images/museum/mangrove.png"
image museum_closeup             = "images/museum/mangrove-close-up-new .png"
image museum_mother_spring       = "images/museum/mother-spring-remembers.png"

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
            "on_enter":   "museum_on_enter",
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
            "on_enter":   "museum_disappearances_on_enter",
            "children":   [],
            "objects":    [
                {
                    "id":        "museum.disappearances.photographs",
                    "name":      "Resettlement Photographs",
                    "item":      None,
                    "action":    "museum_photographs_action",
                    "msg_first": [
                        "A row of faded photographs shows entire streets of houses, doors standing open.",
                        "The placard explains: {i}During the period of pacification, many households were peacefully resettled for their own protection.{/i}",
                        "\"Resettled.\" The word does a lot of work.",
                        "In photo after photo the homes are intact — furniture, washing on the line — but no people. As if everyone simply stepped out and never came back.",
                        "Half the village still stands empty because of this. If you want to know what really happened to a family, you would have to walk into one of those {place}empty homes{/place} yourself.",
                    ],
                    "msg_done":  "Rows of open doors and empty houses. Nobody chose to leave them.",
                },
                {
                    "id":        "museum.disappearances.implements",
                    "name":      "Instruments of Order",
                    "item":      None,
                    "action":    "museum_implements_action",
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
            "on_enter":   "museum_forced_labor_on_enter",
            "children":   [],
            "objects":    [
                {
                    "id":        "museum.forced_labor.ledger",
                    "name":      "Plantation Ledger",
                    "item":      None,
                    "action":    "museum_ledger_action",
                    "msg_first": [
                        "A thick ledger lies open under glass, every line a worker reduced to a number and a column of figures.",
                        "It seems like documents used for keeping track of local workers who were exploited at the {place}Rubber Plantation{/place}."
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
                    "action":    "museum_tag_action",
                    "msg_first": [
                        "A small metal tag stamped with a five-digit number hangs on a frayed cord.",
                        "The label: {i}Identification issued to plantation labourers.{/i}",
                        "Not a name. A number, like the one stamped into that ledger.",
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
            "on_enter":   "museum_spring_display_on_enter",
            "children":   [],
            "objects":    [
                {
                    "id":        "museum.spring_display.exhibit",
                    "name":      "Spring Display",
                    "item":      None,
                    "action":    "museum_exhibit_action",
                    "msg_first": [
                        "A small exhibit describes the {place}Mangrove Spring{/place} at the village's edge — the place the tour brochures call the Mirror Pool.",
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


default museum_wing_intro_played = set()


# ── Entry point (called from the village map loop) ────────────────────────────

label museum_scene:
    call explore_node("museum") from _call_museum_root
    stop ambience fadeout 1.0
    stop sound fadeout 0.5
    return


# ── Intro labels (called once per node on first visit) ────────────────────────

label museum_intro:
    scene museum at fit_screen
    with Dissolve(0.5)
    play sound "audio/museum/museum-open.mp3"
    play ambience "audio/museum/ambience.mp3" loop fadein 1.0
    "The village museum is small but unsettling."
    "Glass cases display artifacts — masks, farming tools, ceremonial objects — each stripped of their original meaning by sterile labels."
    "Something about this place feels wrong. As if it was built to explain the village away rather than remember it."
    "Three wings branch off the main hall. Each one, you suspect, is hiding more than it shows."
    return

label museum_disappearances_intro:
    play sound "audio/museum/footsteps.mp3"
    $ museum_wing_intro_played.add("disappearances")
    scene museum_pacification_wing at fit_screen
    with Dissolve(0.5)
    "This wing is titled {i}Pacification & Resettlement.{/i}"
    "It tells a tidy story of villages calmly relocated. The photographs on the walls tell a different one."
    return

label museum_forced_labor_intro:
    play sound "audio/museum/footsteps.mp3"
    $ museum_wing_intro_played.add("forced_labor")
    scene museum_rubber_trade at fit_screen
    with Dissolve(0.5)
    "This wing celebrates {i}The Rubber Trade{/i} that once made the colony rich."
    "Polished tools, proud figures, and not one word about who actually bled for it."
    return

label museum_spring_display_intro:
    play sound "audio/museum/footsteps.mp3"
    $ museum_wing_intro_played.add("spring_display")
    scene museum_mangrove at fit_screen
    with Dissolve(0.5)
    "A quieter alcove at the back of the museum is given over to the village's natural landmarks."
    "Most of the space is taken up by a single neglected case near the wall."
    return


# ── on_enter labels (audio + bg restore, called every visit) ─────────────────

label museum_on_enter:
    scene museum at fit_screen
    if not renpy.music.get_playing("ambience"):
        play ambience "audio/museum/ambience.mp3" loop fadein 1.0
    return

label museum_disappearances_on_enter:
    scene museum_pacification_wing at fit_screen
    if "disappearances" in museum_wing_intro_played:
        $ museum_wing_intro_played.discard("disappearances")
    else:
        play sound "audio/museum/footsteps.mp3"
    return

label museum_forced_labor_on_enter:
    scene museum_rubber_trade at fit_screen
    if "forced_labor" in museum_wing_intro_played:
        $ museum_wing_intro_played.discard("forced_labor")
    else:
        play sound "audio/museum/footsteps.mp3"
    return

label museum_spring_display_on_enter:
    scene museum_mangrove at fit_screen
    if "spring_display" in museum_wing_intro_played:
        $ museum_wing_intro_played.discard("spring_display")
    else:
        play sound "audio/museum/footsteps.mp3"
    return


# ── Object action labels ──────────────────────────────────────────────────────

label museum_photographs_action:
    play sound "audio/museum/footsteps.mp3"
    scene museum_pacification_photos at fit_screen
    with Dissolve(0.5)
    "A row of faded photographs shows entire streets of houses, doors standing open."
    "The placard explains: {i}During the period of pacification, many households were peacefully resettled for their own protection.{/i}"
    "\"Resettled.\" The word does a lot of work."
    "In photo after photo the homes are intact — furniture, washing on the line — but no people. As if everyone simply stepped out and never came back."
    "Half the village still stands empty because of this. If you want to know what really happened to a family, you would have to walk into one of those {place}empty homes{/place} yourself."
    return

label museum_implements_action:
    play sound "audio/museum/footsteps.mp3"
    scene museum_pacification_tools at fit_screen
    with Dissolve(0.5)
    "A locked case displays restraints, batons, and surgical-looking tools, all neatly mounted."
    "The label calls them {i}implements used to maintain civil order.{/i}"
    "It does not say that the people taken from those homes were brought somewhere to be questioned — and that almost none of them came home."
    "Those who were 'questioned' ended up in the records at the city hall. Those who died were buried, or worse, sent to the hospital."
    return

label museum_ledger_action:
    play sound "audio/museum/footsteps.mp3"
    scene museum_rubber_ledger at fit_screen
    with Dissolve(0.5)
    "A thick ledger lies open under glass, every line a worker reduced to a number and a column of figures."
    "It seems like documents used for keeping track of local workers who were exploited at the {place}Rubber Plantation{/place}."
    "The placard praises it as {i}a model of modern plantation efficiency.{/i}"
    "There are no names. Only IDs, daily outputs, and curt notes: {i}Quotas unmet. Unfit for labor. Deceased.{/i}"
    "People, kept like inventory. The plantation itself still stands at the edge of the village — and ledgers like this one would still be out there."
    return

label museum_tag_action:
    play sound "audio/museum/footsteps.mp3"
    scene museum_rubber_tag at fit_screen
    with Dissolve(0.5)
    "A small metal tag stamped with a five-digit number hangs on a frayed cord."
    "The label: {i}Identification issued to plantation labourers.{/i}"
    "Not a name. A number — the same kind stamped into that ledger."
    "Whole families were worked to death under tags like this. Their story is written in the records still kept out at the rubber plantation."
    return

label museum_exhibit_action:
    play sound "audio/museum/footsteps.mp3"
    scene museum_closeup at fit_screen
    with Dissolve(0.5)
    "A small exhibit describes the {place}Mangrove Spring{place} at the village's edge — the place the tour brochures call the Mirror Pool."
    "The placard frames it as {i}a scenic curiosity, popular with visitors.{/i}"
    "But the older photographs show villagers leaving offerings there, and a carved marker standing at the water's edge."
    "Whatever that marker once said, it clearly mattered to the people here. The spring itself is still out there, waiting."
    return

label museum_spring_fragments_action:
    play sound "audio/museum/footsteps.mp3"
    scene museum_mother_spring at fit_screen
    with Dissolve(0.5)
    if not signMarksRevealed:
        $ interacted_objects = set(x for x in interacted_objects if x != "museum.spring_display.fragments")
        "The glass case is locked."
        "Inside are three weathered fragments tagged with catalog numbers, but without context, they feel like museum clutter."
        "The label reads: {i}Fragments from an Unidentified Spring Marker.{/i}"
        "You make a note to come back if you find something that makes the labels matter."
        return

    "A glass case near the back wall holds three pieces of carved wood."
    "The label reads: {i}Fragments from an Unidentified Spring Marker.{/i}"
    "{item}Three fragments{/item} sit under glass."
    "The museum label calls them decorative remnants from an unidentified spring structure."
    "Each one has been cataloged by fragment number."

    "The labels match the marks from the sign: {b}S-03{/b}, {b}S-08{/b}, and {b}S-14{/b}."
    "These are not random pieces."
    "They look like broken parts of an older sign — one that existed before this place was renamed Mirror Pool."
    "The museum label says the pieces were recovered during redevelopment and later archived as historical material."
    "But the way they are displayed makes them feel disconnected from the spring itself."
    "Something about this feels wrong."
    "These fragments were not just artifacts. They were part of the spring's original name."

    "Spring Fragment 03."
    "A carved piece of wood. One word remains visible: {b}MOTHER{/b}."

    "Spring Fragment 08."
    "A broken strip of painted board. The word {b}SPRING{/b} is still legible."

    "Spring Fragment 14."
    "A piece of root-warped signage. The final carved word reads: {b}REMEMBERS{/b}."

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
