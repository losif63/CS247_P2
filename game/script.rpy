define m = Character('Me', color="#c8c8ff")
image intro = "intro.png"
image village_map = "images/village_map.png"
image evelyn = "images/evelyn.png"
image marcus = "images/marcus.png"
image theo   = "images/theo.png"
image yuna   = "images/yuna.png"
image aanya  = "images/aanya.png"

define FANON_BODY = ("\"Colonialism is not satisfied merely with holding a people in its grip "
    "and emptying the native's brain of all form and content. By a kind of perverted logic, "
    "it turns to the past of the oppressed people, and distorts, disfigures, and destroys it.\"")
define FANON_SOURCE = "—FRANTZ FANON, The Wretched of the Earth"

define FAULKNER_BODY = "\"The past is never dead. It's not even past.\""
define FAULKNER_SOURCE = "—WILLIAM FAULKNER, Requiem for a Nun"

define SHIRE_BODY = "\"I tried to leave you behind but I am made of everything you ever put me through.\""
define SHIRE_SOURCE = "–WARSAN SHIRE"

transform fit_screen:
    xsize 1920
    ysize 1080
    fit "cover"
    xalign 0.5
    yalign 0.5

style epigraph_quote:
    color "#ffffff"
    size 32
    text_align 0.5
    layout "subtitle"
    line_spacing 12

style epigraph_attribution:
    color "#999999"
    size 24
    text_align 0.5
    italic True

screen epigraph(body, source=""):
    add "#000000"
    vbox:
        xalign 0.5
        yalign 0.45
        xmaximum 1100
        spacing 50
        text body style "epigraph_quote"
        if source:
            text source style "epigraph_attribution"

label start:
    $ quick_menu = True
    scene black

    show screen epigraph(FANON_BODY, FANON_SOURCE)
    with Dissolve(2.0)
    $ renpy.pause(5.0, hard=False)
    hide screen epigraph with Dissolve(2.0)

    show screen epigraph(FAULKNER_BODY, FAULKNER_SOURCE)
    with Dissolve(2.0)
    $ renpy.pause(5.0, hard=False)
    hide screen epigraph with Dissolve(2.0)

    show screen epigraph(SHIRE_BODY, SHIRE_SOURCE)
    with Dissolve(2.0)
    $ renpy.pause(5.0, hard=False)
    hide screen epigraph with Dissolve(2.0)

    $ quick_menu = True

    scene intro at fit_screen

    "An eerie atmosphere creeps in as I approach Pelau Siring."

    m "Well, here I am again. All alone, this time..."

    "Last month, I visited this place for my summer vacation with 5 of my friends - Evelyn, Marcus, Theo, Yuna, and Aanya."

    "After returning from the vacation, strange symptoms have appeared. I was the only one unaffected."

    call friends_flashback from _call_friends_flashback

    "The doctors couldn't identify what's wrong with them. Something tells me that the secret lies in this village..."

    jump village_map


# ─────────────────────────────────────────────
# FRIENDS FLASHBACK
# ─────────────────────────────────────────────

label friends_flashback:

    scene evelyn
    with Dissolve(1.0)
    "Evelyn."
    "She feels like she's burning up all the time for no reason."
    "She sleeps with multiple fans pointed at her and ice packs on her wrists."

    scene marcus
    with Dissolve(1.0)
    "Marcus."
    "He can't stop working. He shows up to work hours early and leaves late at night."
    "At home, he can't sit down. He paces, cleans, organizes, anythiing to keep being productive."

    scene theo
    with Dissolve(1.0)
    "Theo."
    "He can't get rid of anything. The things he throws away appears on his bed."
    "Receipts pile up in his pockets, food wrappers show up on his bed."

    scene yuna
    with Dissolve(1.0)
    "Yuna."
    "She says people can't see her anymore."
    "Delivery drivers can't find her home. Her name disappears from email chains."
    "At the doctor's office, the nurse walks into her room, frowns, and marks her as a no-show."

    scene aanya
    with Dissolve(1.0)
    "Aanya."
    "She can't speak her first language, Tamil, anymore."
    "She can feel the words on her tongue, but they won't come out."

    scene black
    with Dissolve(1.0)
    return


# ─────────────────────────────────────────────
# MAP BUTTON STYLES
# ─────────────────────────────────────────────

style map_button_button:
    background Frame("#00000099", 8, 8)
    hover_background Frame("#555555bb", 8, 8)
    padding (14, 10)

style map_button_button_text:
    color "#ffffff"
    hover_color "#ffdd88"
    size 28


# ─────────────────────────────────────────────
# VILLAGE MAP SCREEN
# ─────────────────────────────────────────────

screen village_map_screen():
    modal True

    # Rubber Plantation — bottom-left cluster
    button:
        xpos 100
        ypos 610
        xsize 330
        ysize 380
        background None
        hover_background "#ffffff22"
        action Confirm("Do you really want to move to the Rubber Plantation?", yes=Return("rubber_plantation"))

    # Town Hall — upper-left building
    button:
        xpos 540
        ypos 276
        xsize 192
        ysize 254
        background None
        hover_background "#ffffff22"
        action Confirm("Do you really want to move to the Town Hall?", yes=Return("town_hall"))

    # Museum — upper-center columned building
    button:
        xpos 920
        ypos 255
        xsize 160
        ysize 197
        background None
        hover_background "#ffffff22"
        action Confirm("Do you really want to move to the Museum?", yes=Return("museum"))

    # Graveyard — upper-right-center gravestones
    button:
        xpos 1197
        ypos 244
        xsize 224
        ysize 193
        background None
        hover_background "#ffffff22"
        action Confirm("Do you really want to move to the Graveyard?", yes=Return("graveyard"))

    # Church — far-right steeple
    button:
        xpos 1420
        ypos 244
        xsize 182
        ysize 330
        background None
        hover_background "#ffffff22"
        action Confirm("Do you really want to move to the Church?", yes=Return("church"))

    # Empty Home — center small house
    button:
        xpos 1045
        ypos 646
        xsize 231
        ysize 192
        background None
        hover_background "#ffffff22"
        action Confirm("Do you really want to move to the Empty Home?", yes=Return("empty_home"))

    # Hospital — right-lower cross building
    button:
        xpos 1450
        ypos 674
        xsize 180
        ysize 200
        background None
        hover_background "#ffffff22"
        action Confirm("Do you really want to move to the Hospital?", yes=Return("hospital"))


# ─────────────────────────────────────────────
# MAIN MAP LOOP
# ─────────────────────────────────────────────

label village_map:
    scene village_map at fit_screen
    with Dissolve(1.0)

    call screen village_map_screen
    $ map_choice = _return

    if map_choice == "rubber_plantation":
        call rubber_plantation_scene from _call_rubber_plantation_scene
    elif map_choice == "town_hall":
        call town_hall_scene from _call_town_hall_scene
    elif map_choice == "museum":
        call museum_scene from _call_museum_scene
    elif map_choice == "graveyard":
        call graveyard_scene from _call_graveyard_scene
    elif map_choice == "church":
        call church_scene from _call_church_scene
    elif map_choice == "empty_home":
        call empty_home_scene from _call_empty_home_scene
    elif map_choice == "hospital":
        call hospital_scene from _call_hospital_scene

    jump village_map


# ─────────────────────────────────────────────
# LOCATION SCENES
# ─────────────────────────────────────────────

# rubber_plantation_scene is defined in rubber_plantation.rpy

label town_hall_scene:
    scene black
    with Dissolve(0.5)
    "You push open the heavy doors of the town hall."
    "Dusty portraits of colonial administrators line the walls, staring down with cold, flat eyes."
    "Old ledgers and records are scattered across the main desk."
    $ finish = False
    while not finish:
        menu:
            "Finish Investigation":
                menu:
                    "Are you sure you want to finish investigating here?"
                    "Yes, return to the map.":
                        $ finish = True
                    "No, keep looking.":
                        pass
    return

label museum_scene:
    scene black
    with Dissolve(0.5)
    "The village museum is small but unsettling."
    "Glass cases display artifacts — masks, farming tools, ceremonial objects — each stripped of their original meaning by sterile labels."
    "Something about this place feels wrong."
    $ finish = False
    while not finish:
        menu:
            "Finish Investigation":
                menu:
                    "Are you sure you want to finish investigating here?"
                    "Yes, return to the map.":
                        $ finish = True
                    "No, keep looking.":
                        pass
    return

label graveyard_scene:
    scene black
    with Dissolve(0.5)
    "The graveyard is older than the village itself, some say."
    "You walk between the crumbling headstones, many worn smooth — names erased by time."
    "A fresh wreath of flowers sits at one of the graves. Someone was here recently."
    $ finish = False
    while not finish:
        menu:
            "Finish Investigation":
                menu:
                    "Are you sure you want to finish investigating here?"
                    "Yes, return to the map.":
                        $ finish = True
                    "No, keep looking.":
                        pass
    return

label church_scene:
    scene black
    with Dissolve(0.5)
    "The church looms at the edge of the square, its white walls stained by decades of rain."
    "Inside, rows of wooden pews face a simple altar."
    "Candles have been recently burned — the wax is still soft."
    $ finish = False
    while not finish:
        menu:
            "Finish Investigation":
                menu:
                    "Are you sure you want to finish investigating here?"
                    "Yes, return to the map.":
                        $ finish = True
                    "No, keep looking.":
                        pass
    return

label empty_home_scene:
    scene black
    with Dissolve(0.5)
    "The door to the empty home swings open at your touch — it wasn't locked."
    "A layer of dust coats everything. Furniture still in place, as if the occupants simply vanished."
    "A child's drawing is pinned to the wall. You don't want to look at it too long."
    $ finish = False
    while not finish:
        menu:
            "Finish Investigation":
                menu:
                    "Are you sure you want to finish investigating here?"
                    "Yes, return to the map.":
                        $ finish = True
                    "No, keep looking.":
                        pass
    return

label hospital_scene:
    scene black
    with Dissolve(0.5)
    "The hospital is the newest building in the village, though that's not saying much."
    "The corridors are empty and the lights flicker. Supply cabinets hang open, half-emptied."
    "You find a patient log left on the front desk. The last entry is dated three weeks ago."
    $ finish = False
    while not finish:
        menu:
            "Finish Investigation":
                menu:
                    "Are you sure you want to finish investigating here?"
                    "Yes, return to the map.":
                        $ finish = True
                    "No, keep looking.":
                        pass
    return
