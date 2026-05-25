define m = Character('Me', color="#c8c8ff")

default map_onboarding_shown = False
default current_day = 1
default locations_today = 0
image intro = "Enter.png"
image village_map = "images/Map.jpg"
image thia = "images/thia.png"
image marcus = "images/marcus_affliction.png"
# image theo   = "images/theo.png"
image yuna   = "images/yuna.png"
# image aanya  = "images/aanya.png"

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

    "Last month, I visited this place for my summer vacation with 5 of my friends - Thia, Marcus, Theo, Yuna, and Aanya."

    "After returning from the vacation, strange symptoms have appeared. I was the only one unaffected."

    call friends_flashback from _call_friends_flashback

    "The doctors couldn't identify what's wrong with them. Something tells me that the secret lies in this village..."

    jump village_map


# ─────────────────────────────────────────────
# FRIENDS FLASHBACK
# ─────────────────────────────────────────────

label friends_flashback:

    scene thia
    with Dissolve(1.0)
    "Thia."
    "She can't get rid of anything."
    "Whatever she throws away comes back. Receipts pile up in her pockets. Food wrappers reappear on her bed."
    "Lately it's gotten physical — her skin smells like mangrove water no matter how much she showers, and she keeps coughing up brackish water."

    scene marcus at fit_screen
    with Dissolve(1.0)
    "Marcus."
    "He can't stop working. He shows up to work hours early and leaves late at night."
    "At home, he can't sit down. He paces, cleans, organizes, anythiing to keep being productive."

    # scene theo
    # with Dissolve(1.0)
    # "Theo."
    # "He can't get rid of anything. The things he throws away appears on his bed."
    # "Receipts pile up in his pockets, food wrappers show up on his bed."

    scene yuna
    with Dissolve(1.0)
    "Yuna."
    "She is plagued by recurring dreams she can't escape."
    "In them, her father is dragged away and tortured to death. Her mother is taken and used as a subject of illegal human experimentation."
    "The dreams come every night. She wakes up screaming. Her sanity is slowly eroding."

    # scene aanya
    # with Dissolve(1.0)
    # "Aanya."
    # "She can't speak her first language, Tamil, anymore."
    # "She can feel the words on her tongue, but they won't come out."

    scene black
    with Dissolve(1.0)
    return


# ─────────────────────────────────────────────
# MAP ONBOARDING OVERLAY
# ─────────────────────────────────────────────

screen map_onboarding_screen():
    modal True
    zorder 200

    add "#000000bb"

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 700
        background "#161412"
        padding (40, 36, 40, 36)

        vbox:
            spacing 20
            xfill True

            text "Investigation Journal":
                font "fonts/SpecialElite.ttf"
                color "#b89050"
                size 34
                xalign 0.5

            text "Use the {b}Journal{/b} button in the quick menu at the bottom of the screen to open your investigation notes at any time.\n\n• {color=#ff0000}{b}Inventory{/b}{/color} — clues and items you've collected\n• {color=#0000ff}{b}Friends{/b}{/color} — your friends' current status":
                font "fonts/SpecialElite.ttf"
                color "#c4b090"
                size 20
                line_spacing 6
                xalign 0.0

            textbutton "Got it":
                xalign 0.5
                background "#2d2720"
                hover_background "#4a3a28"
                padding (24, 12, 24, 12)
                action Return()
                text_font "fonts/SpecialElite.ttf"
                text_color "#e8d5a0"
                text_hover_color "#ffffff"
                text_size 26
                text_xalign 0.5


screen map_time_limit_screen():
    modal True
    zorder 200

    add "#000000bb"

    frame:
        xalign 0.5
        yalign 0.5
        xmaximum 700
        background "#161412"
        padding (40, 36, 40, 36)

        vbox:
            spacing 20
            xfill True

            text "Your Time Is Limited":
                font "fonts/SpecialElite.ttf"
                color "#b89050"
                size 34
                xalign 0.5

            text "You have {b}5 days{/b} before you must leave Pelau Siring.\n\nEach day, you may explore {b}3 locations{/b}. Once you visit a third location, night falls and the day ends.\n\nUse your time wisely.":
                font "fonts/SpecialElite.ttf"
                color "#c4b090"
                size 20
                line_spacing 6
                xalign 0.0

            textbutton "Understood":
                xalign 0.5
                background "#2d2720"
                hover_background "#4a3a28"
                padding (24, 12, 24, 12)
                action Return()
                text_font "fonts/SpecialElite.ttf"
                text_color "#e8d5a0"
                text_hover_color "#ffffff"
                text_size 26
                text_xalign 0.5


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

    # Day / location counter HUD
    frame:
        xpos 20
        ypos 20
        background "#000000aa"
        padding (16, 10, 16, 10)
        vbox:
            spacing 4
            text "Day [current_day] / 5":
                font "fonts/SpecialElite.ttf"
                color "#e8d5a0"
                size 22
            text "Locations today: [locations_today] / 3":
                font "fonts/SpecialElite.ttf"
                color "#a09070"
                size 18

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

    if not map_onboarding_shown:
        $ map_onboarding_shown = True
        call screen map_onboarding_screen
        call screen map_time_limit_screen

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

    $ locations_today += 1

    if locations_today >= 3:
        call night_scene from _call_night_scene
        $ locations_today = 0
        $ current_day += 1
        if current_day > 5:
            jump game_ending

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


# ─────────────────────────────────────────────
# NIGHT TRANSITION
# ─────────────────────────────────────────────

label night_scene:
    scene black
    with Dissolve(1.5)

    if current_day < 5:
        "Night falls over Pelau Siring."
        "Day [current_day] has ended."
        $ _days_left = 5 - current_day
        "[_days_left] day(s) remain."
    else:
        "Night falls over Pelau Siring for the last time."
        "Five days. That was all you had."
        "Tomorrow you leave — with whatever answers you've found."

    return


# ─────────────────────────────────────────────
# ENDING
# ─────────────────────────────────────────────

label game_ending:
    scene black
    with Dissolve(2.0)

    "Five days have passed. You board the boat back to the mainland."

    # ── Thia ──────────────────────────────────
    "Thia."

    if friend_notes["thia"]["solved"]:
        "Her skin no longer smells of the spring."
        "The things she throws away stay gone now."
        "She texted you once to say she thinks about where she leaves things. That was all she said."
    else:
        "She was found in her apartment three days after you returned. Her throat had closed."
        "The doctors couldn't explain the brackish water in her lungs."
        "Everything she had ever thrown away was piled neatly around her bed."

    # ── Marcus ────────────────────────────────
    "Marcus."

    if friend_notes["marcus"]["solved"]:
        "He took a day off for the first time in months."
        "He said it felt strange, sitting still. But he managed it."
        "He's learning to let the work wait."
    else:
        "He collapsed at his desk six days after you returned."
        "His coworkers said he hadn't left the building in four days."
        "He died doing exactly what the curse demanded, until there was nothing left of him."

    # ── Yuna ──────────────────────────────────
    "Yuna."

    if friend_notes["yuna"]["solved"]:
        "She slept through the night. Then the next. Then the next."
        "She doesn't remember the dreams anymore."
        "She called you once to say she was okay. That was enough."
    else:
        "Yuna's parents were found murdered in their home two weeks after you returned."
        "Three days later, Yuna was found dead as well. She had taken her own life."
        "The dreams had shown her what she could not live with."

    # ── Ending branch ─────────────────────────
    $ friends_saved = sum(1 for f in friend_notes.values() if f["solved"])

    if friends_saved < 2:
        "You stare at the water as the island disappears behind you."
        "The village gave nothing back. You took nothing home."
        "You wonder if you ever really saw any of them at all."
        "{b}Bad Ending — The Village Remembers{/b}"

    elif friends_saved == 2:
        "Two of your friends will wake up tomorrow as themselves again."
        "The third you don't let yourself think about."
        "The village gave up some of what it took. Not all of it."
        "You wonder what it would have cost you to stay one more day."
        "{b}Normal Ending — Partial Restitution{/b}"

    else:
        "You don't feel like a hero. You feel like someone who finally paid attention."
        "The village is still standing behind you. Its history remains."
        "But something has been returned — something the colony tried to erase."
        "That, at least, was yours to give back."
        "{b}Good Ending — What Was Taken{/b}"

    return
