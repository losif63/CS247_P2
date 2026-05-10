define m = Character('Me', color="#c8c8ff")
image intro = "intro.png"
image village_map = "images/village_map.png"

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

    "Last month, I visited this place for my summer vacation with 5 of my friends - Evelyn, Mark, Jessica, Darvin, and Stephen."

    "After returning from the vacation, strange symptoms have appeared. I was the only one unaffected."

    "The doctors couldn't identify what's wrong with them. Something tells me that the secret lies in this village..."

    jump village_map


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
    style_prefix "map_button"

    textbutton "Rubber Plantation":
        xpos 50
        ypos 820
        action Return("rubber_plantation")

    textbutton "Town Hall":
        xpos 320
        ypos 390
        action Return("town_hall")

    textbutton "Museum":
        xpos 700
        ypos 150
        action Return("museum")

    textbutton "Graveyard":
        xpos 1010
        ypos 150
        action Return("graveyard")

    textbutton "Church":
        xpos 1330
        ypos 330
        action Return("church")

    textbutton "Empty Home":
        xpos 830
        ypos 580
        action Return("empty_home")

    textbutton "Hospital":
        xpos 1310
        ypos 620
        action Return("hospital")


# ─────────────────────────────────────────────
# MAIN MAP LOOP
# ─────────────────────────────────────────────

label village_map:
    scene village_map at fit_screen
    with Dissolve(1.0)

    call screen village_map_screen
    $ map_choice = _return

    if map_choice == "rubber_plantation":
        call rubber_plantation_scene
    elif map_choice == "town_hall":
        call town_hall_scene
    elif map_choice == "museum":
        call museum_scene
    elif map_choice == "graveyard":
        call graveyard_scene
    elif map_choice == "church":
        call church_scene
    elif map_choice == "empty_home":
        call empty_home_scene
    elif map_choice == "hospital":
        call hospital_scene

    jump village_map


# ─────────────────────────────────────────────
# LOCATION SCENES
# ─────────────────────────────────────────────

label rubber_plantation_scene:
    scene black
    with Dissolve(0.5)
    "You arrive at the rubber plantation at the edge of the village."
    "The smell of latex and jungle humidity hangs heavy in the air."
    "Rows of rubber trees stretch as far as the eye can see, their bark scarred with diagonal cuts."
    menu:
        "Finish Investigation":
            pass
    return

label town_hall_scene:
    scene black
    with Dissolve(0.5)
    "You push open the heavy doors of the town hall."
    "Dusty portraits of colonial administrators line the walls, staring down with cold, flat eyes."
    "Old ledgers and records are scattered across the main desk."
    menu:
        "Finish Investigation":
            pass
    return

label museum_scene:
    scene black
    with Dissolve(0.5)
    "The village museum is small but unsettling."
    "Glass cases display artifacts — masks, farming tools, ceremonial objects — each stripped of their original meaning by sterile labels."
    "Something about this place feels wrong."
    menu:
        "Finish Investigation":
            pass
    return

label graveyard_scene:
    scene black
    with Dissolve(0.5)
    "The graveyard is older than the village itself, some say."
    "You walk between the crumbling headstones, many worn smooth — names erased by time."
    "A fresh wreath of flowers sits at one of the graves. Someone was here recently."
    menu:
        "Finish Investigation":
            pass
    return

label church_scene:
    scene black
    with Dissolve(0.5)
    "The church looms at the edge of the square, its white walls stained by decades of rain."
    "Inside, rows of wooden pews face a simple altar."
    "Candles have been recently burned — the wax is still soft."
    menu:
        "Finish Investigation":
            pass
    return

label empty_home_scene:
    scene black
    with Dissolve(0.5)
    "The door to the empty home swings open at your touch — it wasn't locked."
    "A layer of dust coats everything. Furniture still in place, as if the occupants simply vanished."
    "A child's drawing is pinned to the wall. You don't want to look at it too long."
    menu:
        "Finish Investigation":
            pass
    return

label hospital_scene:
    scene black
    with Dissolve(0.5)
    "The hospital is the newest building in the village, though that's not saying much."
    "The corridors are empty and the lights flicker. Supply cabinets hang open, half-emptied."
    "You find a patient log left on the front desk. The last entry is dated three weeks ago."
    menu:
        "Finish Investigation":
            pass
    return
