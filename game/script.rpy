define m = Character('Me', color="#c8c8ff")

default map_onboarding_shown = False
default journal_available = False
default current_day = 1
default locations_today = 0
default museumTradeMapFound = False
default museumMasksFound = False
default museumPlantationRecordsFound = False
default ended_early = False
default museum_intro_done = False  # True once the player has made their forced first visit to the museum
default friends_saved_today = []  # Friends solved during the current day; drained each night
image intro = "Enter.png"
image village_map = "images/Map.jpg"
image townhall = "images/newtownhall.png"
image church = "images/church.png"
image museum = "images/museum.png"
image graveyard = "images/graveyard.png"
image hospital        = "images/hospital.png"
image hospital_2f     = "images/hospital2ndfloor.png"
image hospital_3f     = "images/hospital3rdfloor.png"
image hospital_basement = "images/hospitalbasement.png"
image emptyhome = "images/emptyhome.png"
image bg black = Solid("#000")
image remnant_logo = "images/RemnantLogo.png"
image thia = "images/ThiaTransparentBG.png"
image marcus = "images/marcusasset.png"
# image theo   = "images/theo.png"
image yuna   = "images/yunaasset.png"
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

transform logo_intro:
    xalign 0.5
    yalign 0.5
    zoom 1.2
    alpha 0.0
    linear 2.5 alpha 1.0

transform friend_flashback:
    xalign 0.5
    yalign 0.74
    xanchor 0.5
    yanchor 1.0
    zoom 0.65

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

style content_warning_header:
    color "#b89050"
    size 40
    text_align 0.5
    bold True

style content_warning_body:
    color "#ffffff"
    size 28
    text_align 0.5
    layout "subtitle"
    line_spacing 10

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

screen content_warning():
    add "#000000"
    vbox:
        xalign 0.5
        yalign 0.45
        xmaximum 1100
        spacing 40
        text "Content Warning" style "content_warning_header"
        text "This game contains descriptions of violence and torture.\n\nViewer discretion is advised." style "content_warning_body"

label start:
    ################ Starting Sequence #################
    $ quick_menu = True
    scene black

    show screen content_warning
    with Dissolve(2.0)
    $ renpy.pause(5.0, hard=False)
    hide screen content_warning with Dissolve(2.0)

    show screen epigraph(FANON_BODY, FANON_SOURCE)
    with Dissolve(2.0)
    $ renpy.pause(5.0, hard=False)
    hide screen epigraph with Dissolve(2.0)

    show remnant_logo at logo_intro
    $ renpy.pause(6.0, hard=False)
    hide remnant_logo with Dissolve(1.5)

    $ quick_menu = True

    scene intro at fit_screen

    play music "audio/intro/frogs-intro.wav" loop fadein 1.5
    play sound "audio/intro/insects-intro.wav" loop fadein 1.5

    "An eerie atmosphere creeps in as I approach Pelau Siring."

    "It looks just the same as it did the last time I was here, bright and sunny and bustling with tourists."

    "But I can't shake the sense of unease."

    "I'm here all alone this time..."

    "Last month, I visited for my summer vacation with 3 of my friends - Thia, Marcus and Yuna."

    "After returning from the vacation, they all started experiencing strange and unexplainable symptoms. I was the only one unaffected."

    call friends_flashback from _call_friends_flashback

    play music "audio/intro/frogs-intro.wav" loop fadein 1.5
    play sound "audio/intro/insects-intro.wav" loop fadein 1.5

    "The doctors couldn't identify what's wrong with them. However, they said that if this goes on they won't last more than {b}five days{/b}."
    
    "I must do something. Something tells me that the secret lies in this village..."

    $ journal_available = True

    jump village_map


# ─────────────────────────────────────────────
# FRIENDS FLASHBACK
# ─────────────────────────────────────────────

label friends_flashback:

    stop music fadeout 1.0
    stop sound fadeout 1.0

    scene bg black
    show thia at friend_flashback
    with Dissolve(1.0)
    play music "audio/intro/thia-intro-trash.wav" loop fadein 1.0
    play sound "audio/intro/thia-intro-trickle.wav" loop fadein 1.0
    "Thia."
    "She can't get rid of anything."
    "Whatever she throws away comes back. Receipts pile up in her pockets. Food wrappers reappear on her bed."
    "Lately it's gotten physical — her skin smells like mangrove water no matter how much she showers, and she keeps coughing up brackish water."

    scene bg black
    show marcus at friend_flashback
    with Dissolve(1.0)
    play music "audio/intro/marcus-intro-type.wav" loop fadeout 0.5 fadein 0.5
    play sound "audio/intro/marcus-pen-intro.wav" loop fadeout 0.5 fadein 0.5
    "Marcus."
    "He can't stop working. He shows up to work hours early and leaves late at night."
    "At home, he can't sit down. He types up documents, scribbles notes furiously, paces, cleans, organizes, anything to keep being productive."

    scene bg black
    show yuna at friend_flashback
    with Dissolve(1.0)
    play music "audio/intro/yuna-intro-footsteps.mp3" loop fadeout 0.5 fadein 0.5
    play sound "audio/intro/yuna-intro-voices.wav" loop fadeout 0.5 fadein 0.5
    "Yuna."
    "She is plagued by recurring dreams she can't escape."
    "In them, her father is dragged away and tortured to death. Her mother is taken and used as a subject of illegal human experimentation."
    "The dreams come every night. She wakes up screaming. Her sanity is slowly eroding."

    stop music fadeout 1.0
    stop sound fadeout 1.0
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

            text "Use the {b}Journal{/b} icon at the bottom right of the screen to open your investigation notes at any time.\n\n• {item}Inventory{/item} — clues and items you've collected\n• {b}Friends{/b} — your friends' current status":
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

            text "You have {b}5 days{/b} to save your friends.\n\nEach day, you may explore {b}3 locations{/b}. Once you visit a third location, night falls and the day ends.\n\nUse your time wisely.":
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

    # On the very first move of day 1, only the museum is selectable — it grounds
    # the player in the village's history before they explore anywhere else.
    $ _first_day_lock = (not museum_intro_done) and current_day == 1
    $ _locked_tint = "#aa2a2a66"   # reddish veil over the locations locked on day 1
    $ _museum_tint = "#ffffff44"   # soft white highlight on the museum — the only place to go

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
        sensitive (not _first_day_lock)
        action [Play("sound", "audio/map/map-click.wav"), Confirm("Do you want to move to the Rubber Plantation?", yes=Return("rubber_plantation"))]

    # Town Hall — upper-left building
    button:
        xpos 553
        ypos 286
        xsize 178
        ysize 183
        background None
        hover_background "#ffffff22"
        sensitive (not _first_day_lock)
        action [Play("sound", "audio/map/map-click.wav"), Confirm("Do you want to move to the Town Hall?", yes=Return("town_hall"))]

    # Museum — upper-center columned building
    button:
        xpos 937
        ypos 250
        xsize 151
        ysize 139
        background (_museum_tint if _first_day_lock else None)
        hover_background "#ffffff22"
        action [Play("sound", "audio/map/map-click.wav"), Confirm("Do you want to move to the Museum?", yes=Return("museum"))]

    # Graveyard — upper-right-center gravestones
    button:
        xpos 1197
        ypos 244
        xsize 224
        ysize 193
        background None
        hover_background "#ffffff22"
        sensitive (not _first_day_lock)
        action [Play("sound", "audio/map/map-click.wav"), Confirm("Do you want to move to the Graveyard?", yes=Return("graveyard"))]

    # Church — far-right steeple
    button:
        xpos 1462
        ypos 243
        xsize 165
        ysize 274
        background None
        hover_background "#ffffff22"
        sensitive (not _first_day_lock)
        action [Play("sound", "audio/map/map-click.wav"), Confirm("Do you want to move to the Church?", yes=Return("church"))]

    # Empty Home — center small house
    button:
        xpos 1100
        ypos 657
        xsize 161
        ysize 128
        background None
        hover_background "#ffffff22"
        sensitive (not _first_day_lock)
        action [Play("sound", "audio/map/map-click.wav"), Confirm("Do you want to move to the Empty Home?", yes=Return("empty_home"))]

    # Hospital — right-lower cross building
    button:
        xpos 1494
        ypos 634
        xsize 183
        ysize 229
        background None
        hover_background "#ffffff22"
        sensitive (not _first_day_lock)
        action [Play("sound", "audio/map/map-click.wav"), Confirm("Do you want to move to the Hospital?", yes=Return("hospital"))]

    # Mangrove Spring — far right tourist stop
    button:
        xpos 1685
        ypos 250
        xsize 223
        ysize 455
        background None
        hover_background "#ffffff22"
        sensitive (not _first_day_lock)
        action Confirm("Do you want to move to the Mangrove Spring?", yes=Return("mirror_pool"))


# ─────────────────────────────────────────────
# MAIN MAP LOOP
# ─────────────────────────────────────────────

label village_map:
    scene village_map at fit_screen
    with Dissolve(1.0)

    play music "audio/map/map-ticking.wav" loop fadein 1.5
    stop sound fadeout 1.5
    play ambience "audio/map/map-atmosphere.wav" loop fadein 1.5

    if not map_onboarding_shown:
        $ map_onboarding_shown = True
        call screen map_onboarding_screen
        call screen map_time_limit_screen

    # First move of day 1: steer the player to the museum for context.
    if not museum_intro_done and current_day == 1:
        m "I should first find out what's going on in this village."
        m "The museum seems like a good place to get some context. I'll start there."

    call screen village_map_screen
    $ map_choice = _return

    stop music fadeout 1.0
    stop ambience fadeout 1.0

    if map_choice == "rubber_plantation":
        call rubber_plantation_scene from _call_rubber_plantation_scene
    elif map_choice == "town_hall":
        call town_hall_scene from _call_town_hall_scene
    elif map_choice == "museum":
        call museum_scene from _call_museum_scene
        $ museum_intro_done = True
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

    # Early ending — if every friend has been saved, the journey is complete and
    # the game ends the moment the player returns to the map.
    if friend_notes and all(f["solved"] for f in friend_notes.values()):
        $ ended_early = True
        scene black
        with Dissolve(1.0)
        call show_friend_save_notifications from _call_show_friend_save_notifications_ending
        jump game_ending

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


# church_scene is defined in locations/church.rpy


# hospital_scene is defined in locations/hospital.rpy


# ─────────────────────────────────────────────
# NIGHT TRANSITION
# ─────────────────────────────────────────────

label play_night_ambience:
    play music "audio/intro/frogs-intro.wav" loop fadein 1.5
    play ambience "audio/intro/intro-forest.wav" loop fadein 1.5
    play sound "audio/intro/insects-intro.wav" loop fadein 1.5
    return


# Plays each pending friend's "they're okay" notification, then drains the list.
# Called from night_scene and from the early-ending branch in village_map.
label show_friend_save_notifications:
    if "thia" in friends_saved_today:
        "You received a message from Thia:"
        show thia at friend_flashback
        "Something changed."
        "I threw something away today and it stayed gone."
        "But I don't think it was because I finally got rid of it."
        "I think it was because I stopped asking the wrong place to hold it."
        "Thia's affliction has eased."
        hide thia
        with Dissolve(0.5)

    if "marcus" in friends_saved_today:
        show marcus at friend_flashback
        with Dissolve(1.0)
        "You received a message from Marcus's parents."
        "Back home, Marcus sits down for the first time in days."
        "It seems his afflictions have eased."
        hide marcus
        with Dissolve(0.5)

    if "yuna" in friends_saved_today:
        "Your phone buzzes."
        show yuna at friend_flashback
        with Dissolve(1.0)
        "You received a message from Yuna's roommate: {i}I don't know what happened, but she slept through the night. No screaming. She says the dreams are gone.{/i}"
        "It seems her afflictions have eased. She's going to be okay."
        hide yuna
        with Dissolve(0.5)

    $ friends_saved_today = []
    return


label night_scene:
    scene black
    with Dissolve(1.5)
    call play_night_ambience from _call_night_ambience

    if current_day < 5:
        "Night falls over Pelau Siring."
        "Day [current_day] has ended."
    else:
        "Night falls over Pelau Siring for the last time."

    call show_friend_save_notifications from _call_show_friend_save_notifications_night

    if current_day < 5:
        $ _days_left = 5 - current_day
        "[_days_left] day(s) remain."
    else:
        "Tomorrow you leave — with whatever answers you've found."

    return


# ─────────────────────────────────────────────
# ENDING IMAGE CARDS
# ─────────────────────────────────────────────

transform ending_image_fade:
    xalign 0.5
    yalign 0.5
    alpha 0.0
    linear 2.5 alpha 1.0

label show_ending_image(image_path):
    scene black
    show expression image_path as ending_card at ending_image_fade
    $ renpy.pause(15.0, hard=False)
    hide ending_card with Dissolve(1.5)
    return


label game_ending:
    window hide
    scene black
    with Dissolve(2.0)

    if ended_early:
        call show_ending_image("images/if_ended_early1.jpg") from _call_ending_if_ended_early1
        call show_ending_image("images/if_ended_early2.jpg") from _call_ending_if_ended_early2
    else:
        call show_ending_image("images/else_ended_early.jpg") from _call_ending_else_ended_early

    # ── Thia ──────────────────────────────────
    if friend_notes["thia"]["solved"]:
        call show_ending_image("images/if_thia_solved.jpg") from _call_ending_if_thia_solved
    else:
        call show_ending_image("images/else_thia_solved.jpg") from _call_ending_else_thia_solved

    # ── Marcus ────────────────────────────────
    if friend_notes["marcus"]["solved"]:
        call show_ending_image("images/if_marcus_solved.jpg") from _call_ending_if_marcus_solved
    else:
        call show_ending_image("images/else_marcus_solved.jpg") from _call_ending_else_marcus_solved

    # ── Yuna ──────────────────────────────────
    if friend_notes["yuna"]["solved"]:
        call show_ending_image("images/if_yuna_solved.jpg") from _call_ending_if_yuna_solved
    else:
        call show_ending_image("images/else_yuna_solved.jpg") from _call_ending_else_yuna_solved

    # ── Ending branch ─────────────────────────
    $ friends_saved = sum(1 for f in friend_notes.values() if f["solved"])

    if friends_saved < 2:
        call show_ending_image("images/lessthantwo_1.jpg") from _call_ending_lessthantwo_1
        call show_ending_image("images/lessthantwo_2.jpg") from _call_ending_lessthantwo_2

    elif friends_saved == 2:
        call show_ending_image("images/equaltotwo_1.jpg") from _call_ending_equaltotwo_1
        call show_ending_image("images/equaltotwo_2.jpg") from _call_ending_equaltotwo_2

    else:
        call show_ending_image("images/allsolved_1.jpg") from _call_ending_allsolved_1
        call show_ending_image("images/allsolved_2.jpg") from _call_ending_allsolved_2

    return