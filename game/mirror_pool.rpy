default bottleReturned = False
default signInvestigated = False
default drainInvestigated = False
default finalBottleChoiceUnlocked = False
default bottleResolved = False
default signRestorationUnlocked = False
default signChanged = False
default puzzleSolved = False
default mirror_pool_intro_seen = False
image spring_bg_without_bottle = "images/SpringBackgroundWithoutBottle.png"
image spring_bg_with_bottle = "images/SpringBackgroundWithBottle.png"
image sign_view_bg = "images/BackgroundViewWhenViewingSign.png"
image sign_before_change = "images/SignBeforeChange.png"
image sign_after_correct_change = "images/SignAfterCorrectChange.png"

transform sign_full_view:
    xalign 0.5
    yalign 0.20
    zoom 2.0

screen mirror_pool_screen():
    modal True
    tag mirror_pool

    if bottleResolved:
        add "SpringBackgroundWithoutBottle.png" at fit_screen
    else:
        add "SpringBackgroundWithBottle.png" at fit_screen

    # Drainage pipe/grate hotspot
    button:
        xpos 525
        ypos 650
        xsize 303
        ysize 147
        background None
        hover_background Solid("#ffffff22")
        action Return("drain")

    # Bottle hotspot (only present when the bottle is unresolved)
    if not bottleResolved:
        button:
            xpos 590
            ypos 840
            xsize 114
            ysize 180
            background None
            hover_background Solid("#ffffff22")
            action Return("bottle")

    # Tourist sign hotspot
    button:
        xpos 1630
        ypos 550
        xsize 281
        ysize 270
        background None
        hover_background Solid("#ffffff22")
        action Return("sign")

    textbutton "Return to Map":
        style "return_map_button"
        text_style "return_map_button_text"
        xalign 0.97
        yalign 0.04
        action Return("return_map")

label mirror_pool_scene:
    while True:
        if bottleResolved:
            scene spring_bg_without_bottle at fit_screen
        else:
            scene spring_bg_with_bottle at fit_screen

        with Dissolve(0.5)

        if not mirror_pool_intro_seen:
            "Mangrove roots twist into the dark water. The air smells faintly of salt and rust."
            "This is the place tourists called the Mirror Pool."
            "This is where Thia left the bottle behind."
            $ mirror_pool_intro_seen = True

        call screen mirror_pool_screen
        $ choice = _return

        if choice == "bottle":
            call mirror_pool_bottle from _call_mirror_pool_bottle
        elif choice == "sign":
            call mirror_pool_sign from _call_mirror_pool_sign
        elif choice == "drain":
            call mirror_pool_drain from _call_mirror_pool_drain
        elif choice == "change_sign":
            call mirror_pool_sign_restore from _call_mirror_pool_sign_restore
        elif choice == "return_map":
            return
        elif choice == "check_thia":
            call mirror_pool_thia_message from _call_mirror_pool_thia_message
        elif choice == "final_bottle":
            call mirror_pool_final_bottle_choice from _call_mirror_pool_final_bottle_choice

        if puzzleSolved:
            return

    return

label mirror_pool_bottle:
    if bottleResolved:
        "The bottle is gone from the spring now. The water is quieter for it."
        return

    if finalBottleChoiceUnlocked:
        call mirror_pool_final_bottle_choice from _call_mirror_pool_final_bottle_choice_1
        return

    if not bottleReturned:
        "Thia’s bottle lies near the waterline, half-sunk in mud."
        "It looks ordinary. That almost makes it worse."

        menu:
            "Throw it away":
                "You pick up the bottle and throw it into the trash bin near the trail."
                "For a moment, the spring is quiet."
                "Something rolls softly through the mud."
                "The bottle is back at the water’s edge, wet with brackish water."
                "Hmm... that did not fix it."
                $ bottleReturned = True
            "Leave it for now":
                "You decide not to disturb the bottle yet."
    else:
        "The bottle is still here."
        "Every time you try to remove it, the spring gives it back."

    if bottleReturned and signInvestigated and drainInvestigated and not finalBottleChoiceUnlocked:
        $ finalBottleChoiceUnlocked = True
    return

label mirror_pool_sign:
    if signRestorationUnlocked and not signChanged:
        call mirror_pool_sign_restore from _call_mirror_pool_sign_restore_1
        return

    scene sign_view_bg at fit_screen
    show sign_before_change at sign_full_view
    with Dissolve(0.5)

    "The sign names this place as the Mirror Pool."
    "A scenic stop. A place for visitors. A place made easy to look at."
    "But the wood underneath looks older than the words painted on top."

    menu:
        "Look closer":
            "Beneath the tourist name, you notice an older meaning trying to surface."
            "This place was not always named for reflection."
            "It was once named for mourning."
            $ signInvestigated = True
        "Return to Spring":
            pass

    if bottleReturned and signInvestigated and drainInvestigated and not finalBottleChoiceUnlocked:
        $ finalBottleChoiceUnlocked = True
    return

label mirror_pool_drain:
    "The pipe is rusted through, but the dark stain beneath it remains."
    "A thin trail leads from the pipe into the spring."

    menu:
        "Inspect the pipe":
            "A colonial marker is almost buried in the mud:"
            "“WASTE CHANNEL 3.”"
            "This spring was not only neglected."
            "It was used."
            $ drainInvestigated = True
        "Return to Spring":
            pass

    if bottleReturned and signInvestigated and drainInvestigated and not finalBottleChoiceUnlocked:
        $ finalBottleChoiceUnlocked = True
    return

label mirror_pool_final_bottle_choice:
    if not finalBottleChoiceUnlocked:
        return

    "You know enough now to understand why the bottle keeps returning."
    "The spring was not only a scenic place."
    "It was a place renamed, used, and made to hold what others wanted gone."
    "What do you do with Thia’s bottle?"

    while True:
        menu:
            "Throw it in the trash again.":
                "You throw the bottle away again."
                "For a moment, the spring is still."
                "Then the bottle rolls back through the mud."
                "Hmm... that is not right."
                "Throwing it away treats the problem like litter, but this place was already forced to hold what others discarded."
            "Leave it by the spring as an offering.":
                "You place the bottle carefully by the water."
                "Nothing changes."
                "Hmm... that does not feel right either."
                "The bottle was not left in mourning. It was left because Thia assumed the place would absorb it."
            "Carry it away and uncover the old name on the sign.":
                "You pick up Thia’s bottle and hold onto it."
                "This time, it does not roll back."
                "The spring does not ask you to leave the bottle here."
                "It asks you to stop pretending this place was only scenery."
                $ bottleResolved = True
                $ signRestorationUnlocked = True
                jump mirror_pool_after_bottle_choice

    return

label mirror_pool_after_bottle_choice:
    scene spring_bg_without_bottle at fit_screen
    with Dissolve(0.5)

    "The bottle is gone, but the sign still speaks first."
    "“The Mirror Pool.”"
    "A tourist name. A clean name. A name that makes the spring easier to pass through."

    menu:
        "Change the Sign Back":
            call mirror_pool_sign_restore from _call_mirror_pool_sign_restore_2
        "Return to Spring":
            pass

    return

label mirror_pool_sign_restore:
    scene sign_view_bg at fit_screen
    if not signChanged:
        show sign_before_change at sign_full_view
    else:
        show sign_after_correct_change at sign_full_view
    with Dissolve(0.5)

    if not signChanged:
        "The bottle is gone, but the sign still speaks first."
        "“The Mirror Pool.”"
        "A tourist name. A clean name. A name that makes the spring easier to pass through."
        "What should the sign say now?"

        while True:
            menu:
                "Please keep this area clean.":
                    "Hmm... that is not enough."
                    "The marker talks about cleanliness, but not memory."
                    "This place was not only dirtied. It was renamed, used, and made easier to ignore."
                "Mother Spring: a place of mourning, later used as a waste channel.":
                    "You fix the marker beneath the old sign."
                    "The words “Mirror Pool” are still there, but they no longer get the last word."
                    $ signChanged = True
                    $ puzzleSolved = True
                    jump mirror_pool_sign_restored
                "Do not litter. Fines may apply.":
                    "Hmm... that makes the harm too small."
                    "This was never only about litter."
                    "A warning sign cannot acknowledge what happened here."

    else:
        "The sign now names what the tourist version hid."
        "Mother Spring."
        "A place of mourning."
        "Later used as a waste channel."
        return

label mirror_pool_sign_restored:
    scene sign_view_bg at fit_screen
    show sign_after_correct_change at sign_full_view
    with Dissolve(0.5)

    "The sign now names what the tourist version hid."
    "Mother Spring."
    "A place of mourning."
    "Later used as a waste channel."
    "The bottle stays in your bag."
    "It does not return."

    menu:
        "Check on Thia":
            call mirror_pool_thia_message from _call_mirror_pool_thia_message_1
        "Return to Spring":
            pass

    return

label mirror_pool_thia_message:
    "Message from Thia:"
    "“I threw something away today and it stayed gone."
    "I don’t think that means I fixed anything."
    "But I think I understand why it kept coming back.”"
    "Thia’s affliction has eased."

    menu:
        "Return to Map":
            return
        "Stay at the Spring":
            pass

    return
