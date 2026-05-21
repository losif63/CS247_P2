define m = Character('Me', color="#c8c8ff")
image intro = "intro.png"
image village_map = "images/Map.jpg"
image evelyn = "images/evelyn.png"
image marcus = "images/marcus.png"
image theo   = "images/theo.png"
image yuna   = "images/yuna.png"
image aanya  = "images/aanya.png"

define FANON_BODY = ("\"Colonialism is not satisfied merely with holding a people in its grip "
    "and emptying the native's brain of all form and content. By a kind of perverted logic, "
    "it turns to the past of the oppressed people, and distorts, disfigures, and destroys it.\"")
define FANON_SOURCE = "—FRANTZ FANON, The Wretched of the Earth"


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
    ################ Starting Sequence #################
    $ quick_menu = True
    scene black

    show screen epigraph(FANON_BODY, FANON_SOURCE)
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

style return_map_button:
    background Frame("#00000099", 2, 2)
    hover_background Frame("#ffffff33", 2, 2)
    padding (12, 8)
    xminimum 170

style return_map_button_text:
    color "#ffffff"
    hover_color "#ffffcc"
    size 22


# ─────────────────────────────────────────────
# VILLAGE MAP SCREEN
# ─────────────────────────────────────────────

screen village_map_screen():
    modal True

    # Rubber Plantation — bottom-left cluster
    button:
        xpos 95
        ypos 619
        xsize 267
        ysize 270
        background None
        hover_background "#ffffff22"
        action Confirm("Do you want to move to the Rubber Plantation?", yes=Return("rubber_plantation"))

    # Town Hall — upper-left building
    button:
        xpos 553
        ypos 286
        xsize 178
        ysize 183
        background None
        hover_background "#ffffff22"
        action Confirm("Do you want to move to the Town Hall?", yes=Return("town_hall"))

    # Museum — upper-center columned building
    button:
        xpos 937
        ypos 250
        xsize 151
        ysize 139
        background None
        hover_background "#ffffff22"
        action Confirm("Do you want to move to the Museum?", yes=Return("museum"))

    # Graveyard — upper-right-center gravestones
    button:
        xpos 1197
        ypos 244
        xsize 224
        ysize 193
        background None
        hover_background "#ffffff22"
        action Confirm("Do you want to move to the Graveyard?", yes=Return("graveyard"))

    # Church — far-right steeple
    button:
        xpos 1462
        ypos 243
        xsize 165
        ysize 274
        background None
        hover_background "#ffffff22"
        action Confirm("Do you want to move to the Church?", yes=Return("church"))

    # Empty Home — center small house
    button:
        xpos 1100
        ypos 657
        xsize 161
        ysize 128
        background None
        hover_background "#ffffff22"
        action Confirm("Do you want to move to the Empty Home?", yes=Return("empty_home"))

    # Hospital — right-lower cross building
    button:
        xpos 1494
        ypos 634
        xsize 183
        ysize 229
        background None
        hover_background "#ffffff22"
        action Confirm("Do you want to move to the Hospital?", yes=Return("hospital"))

    # Mangrove Spring — far right tourist stop
    button:
        xpos 1685
        ypos 250
        xsize 223
        ysize 455
        background None
        hover_background "#ffffff22"
        action Confirm("Do you want to move to the Mangrove Spring?", yes=Return("mirror_pool"))


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
    elif map_choice == "mirror_pool":
        call mirror_pool_scene from _call_mirror_pool_scene

    jump village_map


# ─────────────────────────────────────────────
# LOCATION SCENES
# ─────────────────────────────────────────────

# rubber_plantation_scene is defined in rubber_plantation.rpy

# town_hall_scene is defined in locations/city_hall.rpy

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

# church_scene is defined in locations/church.rpy


# hospital_scene is defined in locations/hospital.rpy
