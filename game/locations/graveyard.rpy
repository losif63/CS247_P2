image graveyard_old_graves    = "images/graveyard/graveyard-old-graves.png"
image graveyard_old_headstone = "images/graveyard/closeup.png"
image graveyard_metal_header  = "images/graveyard/mother-spring-remembers.png"
image graveyard_fresh_grave   = "images/graveyard/graveyard-fresh.png"
image graveyard_wreath_img    = "images/graveyard/graveyard-wreath.png"
image graveyard_unmarked_tomb = "images/graveyard/graveyard-unmarked-tomb.png"
image graveyard_shed          = "images/graveyard/graveyard-shed.png"
image graveyard_shed_inside   = "images/graveyard/graveyard-shed-inside.png"
image graveyard_shed_shovel   = "images/graveyard/graveyard-shed-shovel.png"
image graveyard_burial_log    = "images/graveyard/graveyard-burial-log.png"

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
            "on_enter":   "graveyard_on_enter",
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
            "on_enter":   "graveyard_old_graves_on_enter",
            "children":   [],
            "objects":    [
                {
                    "id":        "graveyard.old_graves.weathered_stone",
                    "name":      "Weathered Headstone",
                    "item":      None,
                    "action":    "graveyard_weathered_stone_action",
                    "msg_first": "You crouch by one of the oldest stones. The name has long since worn away — only a faint date survives: {b}1921{/b}. The same year the city hall records simply stop.",
                    "msg_done":  "The weathered stone gives nothing more.",
                },
                {
                    "id":        "graveyard.old_graves.mass_marker",
                    "name":      "Iron Marker",
                    "item":      None,
                    "action":    "graveyard_mass_marker_action",
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
            "on_enter":   "graveyard_fresh_grave_on_enter",
            "children":   [],
            "objects":    [
                {
                    "id":        "graveyard.fresh_grave.wreath",
                    "name":      "Wreath of Flowers",
                    "item":      None,
                    "action":    "graveyard_wreath_action",
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
                    "action":    "graveyard_headstone_action",
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
            "on_enter":   "graveyard_toolshed_on_enter",
            "children":   [],
            "objects":    [
                {
                    "id":        "graveyard.toolshed.rack",
                    "name":      "Tool Rack",
                    "item":      "graveyard.shovel",
                    "action":    "graveyard_rack_action",
                    "msg_first": "A wooden rack leans against the back wall, holding a few old tools caked with dried earth. A {color=#ff0000}{b}shovel{/b}{/color} hangs from one of the pegs — you take it.",
                    "msg_done":  "The rack is empty now.",
                },
                {
                    "id":        "graveyard.toolshed.logbook",
                    "name":      "Burial Logbook",
                    "item":      None,
                    "action":    "graveyard_logbook_action",
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


default graveyard_wing_intro_played = set()


# ── Entry point (called from the village map loop) ────────────────────────────

label graveyard_scene:
    call explore_node("graveyard") from _call_graveyard_root
    stop ambience fadeout 1.0
    stop sound fadeout 0.5
    return


# ── Intro labels (called once per node on first visit) ────────────────────────

label graveyard_intro:
    scene graveyard at fit_screen
    with Dissolve(0.5)
    play sound "audio/graveyard/graveyard-enter.mp3"
    $ renpy.music.set_volume(0.2, channel="ambience")
    play ambience "audio/graveyard/graveyard-birds.mp3" loop fadein 1.0
    "The graveyard is older than the village itself, some say."
    "You walk between the crumbling headstones, many worn smooth — names erased by time."
    "A fresh wreath of flowers sits at one of the graves. Someone was here recently."
    return

label graveyard_old_graves_intro:
    play sound "audio/graveyard/graveyard-footsteps.mp3"
    $ graveyard_wing_intro_played.add("old_graves")
    scene graveyard_old_graves at fit_screen
    with Dissolve(0.5)
    "This is the oldest corner of the yard, where the stones lean at angles and the grass grows tall between them."
    "Whole rows stand without names — only weather, moss, and the occasional date."
    return

label graveyard_fresh_grave_intro:
    play sound "audio/graveyard/graveyard-footsteps.mp3"
    $ graveyard_wing_intro_played.add("fresh_grave")
    scene graveyard_fresh_grave at fit_screen
    with Dissolve(0.5)
    "One grave stands apart from the rest, the soil dark and freshly tended."
    "Unlike everything around it, this one has been cared for."
    return

label graveyard_toolshed_intro:
    play sound "audio/graveyard/graveyard-footsteps.mp3"
    $ graveyard_wing_intro_played.add("toolshed")
    scene graveyard_shed at fit_screen
    with Dissolve(0.5)
    "A low wooden shed sits at the edge of the yard, its door hanging half off the hinge."
    "Inside, the air is thick with the smell of soil and rust."
    return


# ── on_enter labels (audio + bg restore, called every visit) ─────────────────

label graveyard_on_enter:
    scene graveyard at fit_screen
    if not renpy.music.get_playing("ambience"):
        $ renpy.music.set_volume(0.3, channel="ambience")
        play ambience "audio/graveyard/graveyard-birds.mp3" loop fadein 1.0
    return

label graveyard_old_graves_on_enter:
    scene graveyard_old_graves at fit_screen
    if "old_graves" in graveyard_wing_intro_played:
        $ graveyard_wing_intro_played.discard("old_graves")
    else:
        play sound "audio/graveyard/graveyard-footsteps.mp3"
    return

label graveyard_fresh_grave_on_enter:
    scene graveyard_fresh_grave at fit_screen
    if "fresh_grave" in graveyard_wing_intro_played:
        $ graveyard_wing_intro_played.discard("fresh_grave")
    else:
        play sound "audio/graveyard/graveyard-footsteps.mp3"
    return

label graveyard_toolshed_on_enter:
    scene graveyard_shed_inside at fit_screen
    if "toolshed" in graveyard_wing_intro_played:
        $ graveyard_wing_intro_played.discard("toolshed")
    else:
        play sound "audio/graveyard/graveyard-footsteps.mp3"
    return


# ── Object action labels ──────────────────────────────────────────────────────

label graveyard_weathered_stone_action:
    play sound "audio/graveyard/graveyard-footsteps.mp3"
    scene graveyard_old_headstone at fit_screen
    with Dissolve(0.5)
    "You crouch by one of the oldest stones. The name has long since worn away — only a faint date survives: {b}1921{/b}. The same year the city hall records simply stop."
    return

label graveyard_mass_marker_action:
    play sound "audio/graveyard/graveyard-footsteps.mp3"
    scene graveyard_metal_header at fit_screen
    with Dissolve(0.5)
    "A rusted iron marker leans where a row of headstones should be."
    "There are no individual names — only a single line stamped into the metal:"
    "\"Interred by order of the colonial administration. Names withheld.\""
    "Beneath the official lettering, someone has scratched three words by hand: {b}MOTHER. SPRING. REMEMBERS.{/b}"
    return

label graveyard_wreath_action:
    play sound "audio/graveyard/graveyard-footsteps.mp3"
    scene graveyard_wreath_img at fit_screen
    with Dissolve(0.5)
    "The flowers are real and recently cut. A narrow ribbon is threaded through them."
    "On the ribbon, in careful handwriting: \"We did not forget you. We were not allowed to remember.\""
    "There is no name. Whoever leaves these has been coming for a long time."
    return

label graveyard_headstone_action:
    play sound "audio/graveyard/graveyard-footsteps.mp3"
    scene graveyard_unmarked_tomb at fit_screen
    with Dissolve(0.5)
    "The headstone is new, the stone still pale and unweathered — but it bears no name and no date. Only a small carving of a swing."
    return

label graveyard_rack_action:
    play sound "audio/graveyard/graveyard-footsteps.mp3"
    scene graveyard_shed_shovel at fit_screen
    with Dissolve(0.5)
    "A wooden rack leans against the back wall, holding a few old tools caked with dried earth. A {color=#ff0000}{b}shovel{/b}{/color} hangs from one of the pegs — you take it."
    play sound "audio/graveyard/graveyard-shovel.mp3"
    return

label graveyard_logbook_action:
    play sound "audio/graveyard/graveyard-footsteps.mp3"
    scene graveyard_burial_log at fit_screen
    with Dissolve(0.5)
    "A water-stained logbook hangs open on a nail, its pages a ledger of burials."
    "Most entries are neat and dated. But the last several years are different — names crossed out, plots left blank, whole pages torn away."
    "One recent line is unfinished, the ink trailing off: \"Plot left open by request. To be filled when she is brought home—\""
    return
