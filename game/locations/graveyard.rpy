################################################################################
## Graveyard — Exploration Tree
##
## Tree structure:
##   graveyard
##   ├── graveyard.old_graves
##   ├── graveyard.fresh_grave
##   └── graveyard.toolshed   (holds the shovel)
##
## To add a child to an existing node: add its ID to the parent's "children"
## list and add a new entry to EXPLORE_NODES. To add a puzzle, set "puzzle"
## to a label name and define that label below.
################################################################################


init python:
    EXPLORE_NODES.update({

        "graveyard": {
            "name":       "Graveyard",
            "parent":     None,
            "intro":      "graveyard_intro",
            "children":   [
                "graveyard.old_graves",
                "graveyard.fresh_grave",
                "graveyard.toolshed",
            ],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "graveyard.old_graves": {
            "name":       "Old Graves",
            "parent":     "graveyard",
            "intro":      "graveyard_old_graves_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "graveyard.old_graves.weathered_stone",
                    "name":      "Weathered Headstone",
                    "item":      None,
                    "action":    None,
                    "msg_first": "You crouch by one of the oldest stones. The name has long since worn away — only a faint date survives: {b}1921{/b}. The same year the city hall records simply stop.",
                    "msg_done":  "The weathered stone gives nothing more.",
                },
                {
                    "id":        "graveyard.old_graves.mass_marker",
                    "name":      "Iron Marker",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "A rusted iron marker leans where a row of headstones should be.",
                        "There are no individual names — only a single line stamped into the metal:",
                        "\"Interred by order of the colonial administration. Names withheld.\"",
                        "Beneath the official lettering, someone has scratched three words by hand: {b}MOTHER. SPRING. REMEMBERS.{/b}",
                    ],
                    "msg_done":  "The iron marker stands over the unnamed.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "graveyard.fresh_grave": {
            "name":       "Fresh Grave",
            "parent":     "graveyard",
            "intro":      "graveyard_fresh_grave_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "graveyard.fresh_grave.wreath",
                    "name":      "Wreath of Flowers",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "The flowers are real and recently cut. A narrow ribbon is threaded through them.",
                        "On the ribbon, in careful handwriting: \"We did not forget you. We were not allowed to remember.\"",
                        "There is no name. Whoever leaves these has been coming for a long time.",
                    ],
                    "msg_done":  "The wreath lies undisturbed where someone left it.",
                },
                {
                    "id":        "graveyard.fresh_grave.headstone",
                    "name":      "Unmarked Headstone",
                    "item":      None,
                    "action":    None,
                    "msg_first": "The headstone is new, the stone still pale and unweathered — but it bears no name and no date. Only a small carving of a swing.",
                    "msg_done":  "The unmarked stone keeps its silence.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "graveyard.toolshed": {
            "name":       "Gravedigger's Shed",
            "parent":     "graveyard",
            "intro":      "graveyard_toolshed_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "graveyard.toolshed.rack",
                    "name":      "Tool Rack",
                    "item":      "graveyard.shovel",
                    "action":    None,
                    "msg_first": "A wooden rack leans against the back wall, holding a few old tools caked with dried earth. A {item}shovel{/item} hangs from one of the pegs — you take it.",
                    "msg_done":  "The rack is empty now.",
                },
                {
                    "id":        "graveyard.toolshed.logbook",
                    "name":      "Burial Logbook",
                    "item":      None,
                    "action":    None,
                    "msg_first": [
                        "A water-stained logbook hangs open on a nail, its pages a ledger of burials.",
                        "Most entries are neat and dated. But the last several years are different — names crossed out, plots left blank, whole pages torn away.",
                        "One recent line is unfinished, the ink trailing off: \"Plot left open by request. To be filled when she is brought home—\"",
                    ],
                    "msg_done":  "The logbook's later pages are too damaged to read further.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

    })

    ITEM_CATALOG.update({
        "graveyard.shovel": {
            "name":        "Shovel",
            "location":    "Graveyard - Gravedigger's Shed",
            "description": "An old shovel taken from the tool rack in the graveyard's shed. The blade is still caked with dried earth.",
        },
    })


# ── Entry point (called from the village map loop) ────────────────────────────

label graveyard_scene:
    call explore_node("graveyard") from _call_graveyard_root
    return


# ── Intro labels (called once per node on first visit) ────────────────────────

label graveyard_intro:
    scene graveyard at fit_screen
    with Dissolve(0.5)
    "The graveyard is older than the village itself, some say."
    "You walk between the crumbling headstones, many worn smooth — names erased by time."
    "A fresh wreath of flowers sits at one of the graves. Someone was here recently."
    return

label graveyard_old_graves_intro:
    "This is the oldest corner of the yard, where the stones lean at angles and the grass grows tall between them."
    "Whole rows stand without names — only weather, moss, and the occasional date."
    return

label graveyard_fresh_grave_intro:
    "One grave stands apart from the rest, the soil dark and freshly tended."
    "Unlike everything around it, this one has been cared for."
    return

label graveyard_toolshed_intro:
    "A low wooden shed sits at the edge of the yard, its door hanging half off the hinge."
    "Inside, the air is thick with the smell of soil and rust."
    return
