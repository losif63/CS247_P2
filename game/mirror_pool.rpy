default bottleReturned = False
default bottleFilled = False
default bayaniNoteRead = False
default codeNoteFound = False
default waterNoteFound = False
default museumFragmentsFound = False
default signMarksRevealed = False
default signInvestigated = False
default drainInvestigated = False
default signRemoved = False
default finalBottleChoiceUnlocked = False
default bottleResolved = False
default messageDecoded = False
default signRestorationUnlocked = False
default signChanged = False
default puzzleSolved = False
default mirror_pool_intro_seen = False
image spring_bg_without_bottle = "images/SpringBackgroundWithoutBottle.png"
image spring_bg_with_bottle = "images/SpringBackgroundWithBottle.png"
image spring_bg_without_sign = "images/SignAfterRemoved.png"
image sign_view_bg = "images/BackgroundViewWhenViewingSign.png"
image sign_before_change = "images/SignBeforeChange.png"
image sign_with_marks_revealed = "images/SignWithMarksRevealed.png"
# Thia sprite used for the final message
image thia_sprite = "images/ThiaTransparentBG.png"

transform thia_left_speaker:
    # Anchor the sprite by its bottom edge and place it above the dialogue box
    xalign 0.12
    # lowered to sit closer to the dialogue box
    yalign 0.74
    xanchor 0.5
    yanchor 1.0
    zoom 0.65

transform sign_full_view:
    xalign 0.5
    yalign 0.20
    zoom 2.0

transform sign_revealed_view:
    xalign 0.5
    yalign 0.20
    zoom 0.489

screen mirror_pool_screen():
    modal True
    tag mirror_pool

    if signRemoved:
        add "SignAfterRemoved.png" at fit_screen
    elif bottleFilled:
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

    # Bottle hotspot (only present when the bottle is unresolved, unfilled, and the sign has not been removed)
    if not bottleResolved and not signRemoved and not bottleFilled:
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
        action Confirm("Are you sure you want to return to the map?", Return("return_map"))

label mirror_pool_scene:
    play ambience "audio/mangrove/mangrove-ambient.wav" fadein 1.0

    while True:
        if signRemoved:
            scene spring_bg_without_sign at fit_screen
        elif bottleFilled:
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
        elif choice == "return_map":
            stop ambience fadeout 1.0
            return
        elif choice == "check_thia":
            call mirror_pool_thia_message from _call_mirror_pool_thia_message


        if puzzleSolved:
            return

    return

label mirror_pool_bottle:
    
    if bottleResolved:
        "The bottle is gone from the spring now. The water is quieter for it."
        return

    if not bottleReturned:
        "Thia’s bottle lies near the waterline, half-sunk in mud."
        "It looks ordinary. That almost makes it worse."

        menu:
            "Throw it away":
                play sound "<from 0 to 2>audio/mangrove/mangrove-throw-away-bottle.wav"
                "You pick up the bottle and throw it into the trash bin near the trail."
                "For a moment, the spring is quiet."
                play sound "audio/mangrove/mangrove-bottle-reappear.mp3"
                "Something thuds in the mud."
                "The bottle is back at the water’s edge, wet with brackish water."
                "Hmm... that did not fix it."
                $ bottleReturned = True
                $ journal_update_friend("thia", note="\"I keep cleaning my room, but everything I throw away outside keeps coming back.\"")
            "Leave it for now":
                "You decide not to disturb the bottle yet."
        return

    if not bottleFilled:
        "The bottle is still here."
        "Every time you try to remove it, the spring gives it back."

        if bottleReturned and signInvestigated and drainInvestigated:
            menu:
                "Fill the bottle with spring water.":
                    play sound "<from 0 to 3>audio/mangrove/mangrove-fill-bottle.wav"
                    "You lower Thia’s bottle into the spring."
                    "The water inside darkens, then stills."
                    "For the first time, the bottle does not roll away from your hand."
                    "The bottle is no longer only something Thia left behind."
                    "For now, it is carrying something back."
                    $ bottleFilled = True
                    $ journal_add_item(
                        "mirror_pool.bottle_of_spring_water",
                        "Bottle of Spring Water",
                        "Mirror Pool",
                        "A bottle filled with dark spring water from the Mirror Pool. It feels less like trash and more like a message waiting to be carried."
                    )
                "Leave it for now":
                    "You decide not to disturb it yet."
        else:
            menu:
                "Leave it for now":
                    "You decide not to disturb it yet."
        return

    "The bottle is full of dark spring water."
    "It feels less like trash now and more like a message waiting to be carried."

    menu:
        "Return to Spring":
            pass
    return

label mirror_pool_sign:
    if signRemoved:
        call mirror_pool_sign_removed from _call_mirror_pool_sign_removed
        return

    scene sign_view_bg at fit_screen
    show sign_before_change at sign_full_view
    with Dissolve(0.5)

    "The sign names this place as the Mirror Pool."
    "A scenic stop. A place for visitors. A place made easy to look at."
    "But the wood underneath looks older than the words painted on top."

    if not signMarksRevealed:
        if bottleFilled:
            menu:
                "Pour spring water over the sign.":
                    play sound "audio/mangrove/mangrove-water-on-sign.wav"
                    "The spring water runs down the tourist sign."
                    "For a moment, nothing happens."
                    "Then the paint begins to darken."
                    play sound "audio/mangrove/mangrove-rumble-words-appear.wav"
                    "Thin marks appear beneath the words Mirror Pool, like something older is pressing through."
                    $ signMarksRevealed = True
                    $ journal_add_item(
                        "mirror_pool.hidden_sign_marks",
                        "Hidden Sign Marks",
                        "Mirror Pool Sign",
                        "After spring water touched the sign, three marks appeared beneath the tourist paint: S-03, S-08, and S-14."
                    )
                    scene sign_view_bg at fit_screen
                    show sign_with_marks_revealed at sign_revealed_view
                    with Dissolve(0.5)
                    "You see three stamped codes: S-03, S-08, and S-14."
                    "They do not look like part of the original carving. They look added later — like museum labels, or catalog numbers."
                    "Maybe these numbers are not the message itself."
                    "Maybe they point to pieces of something that was taken apart."
                    "I should check the {color=#ffff00}{b}museum{/color{/b} again."
                "Look closer":
                    "The words are painted over older wood."
                    "Something is underneath, but the tourist sign is covering most of it."
                    $ signInvestigated = True
                "Return to Spring":
                    pass
        else:
            menu:
                "Look closer":
                    "The words are painted over older wood."
                    "Something is underneath, but the tourist sign is covering most of it."
                    $ signInvestigated = True
                "Return to Spring":
                    pass
    else:
        scene sign_view_bg at fit_screen
        show sign_with_marks_revealed at sign_revealed_view
        with Dissolve(0.5)

        if not museumFragmentsFound:
            "The codes remain on the sign: S-03, S-08, and S-14."
            "They are too precise to be natural marks."
            "They look like the kind of labels used to organize artifacts after they have been removed from where they belonged."
            menu:
                "Return to Spring":
                    pass
        elif not messageDecoded:
            call mirror_pool_decode_marks from _call_mirror_pool_decode_marks
        else:
            call mirror_pool_remove_sign_choice from _call_mirror_pool_remove_sign_choice
    return

label mirror_pool_drain:
    "The pipe is rusted through, but the dark stain beneath it remains."
    "A thin trail leads from the pipe into the spring."

    menu:
        "Inspect the pipe":
            play sound "<from 0 to 3>audio/mangrove/mangrove-inspect-pipe.mp3"
            "A colonial marker is almost buried in the mud:"
            "WASTE CHANNEL 3."
            "This spring was not only neglected."
            "It was used."
            $ drainInvestigated = True
            $ journal_update_friend("thia", note="There's mud in my sheets. I'm coughing up brackish water every hour and the saltiness is burning my throat.")
        "Return to Spring":
            pass

    return

label mirror_pool_decode_marks:
    scene sign_view_bg at fit_screen
    show sign_with_marks_revealed at sign_revealed_view
    with Dissolve(0.5)

    "You line up the fragments in your mind."
    "S-03. S-08. S-14."

    $ _decoded = False
    while not _decoded:
        menu:
            "MOTHER SPRING REMEMBERS":
                "The words return in order."
                "MOTHER SPRING REMEMBERS."
                "The revealed marks pulse faintly beneath the tourist name."
                "For the first time, the sign does not feel blank."
                "It feels like it has been waiting to be read correctly."
                $ messageDecoded = True
                $ journal_add_item(
                    "mirror_pool.decoded_message",
                    "Decoded Spring Message",
                    "Mirror Pool Sign",
                    "The hidden marks on the sign were decoded as: MOTHER SPRING REMEMBERS."
                )
                $ _decoded = True

            "SPRING MOTHER REMEMBERS":
                "Hmm... that does not feel right."
                "The words are there, but the order still hides the beginning."
                "Check what you recorded from the museum."

            "REMEMBERS MOTHER SPRING":
                "Hmm... that does not feel right."
                "The words are there, but the order still hides the beginning."
                "Check what you recorded from the museum."

    "The tourist name still sits on the surface."
    "But beneath it, the older words remain."
    "This place was not always Mirror Pool."
    "It was Mother Spring."
    "And someone tried to make that memory look like a collection of fragments."
    call mirror_pool_remove_sign_choice from _call_mirror_pool_decode_to_remove
    return

label mirror_pool_remove_sign_choice:
    scene sign_view_bg at fit_screen
    show sign_with_marks_revealed at sign_revealed_view
    with Dissolve(0.5)

    "The decoded message is clear now."
    "The problem is not that the sign needs better words."
    "The problem is that the tourist sign was placed over what was already there."

    "What do you do with the tourist sign?"

    while True:
        menu:
            "Write the hidden message onto the sign.":
                "Hmm... that feels too easy."
                "The message was not missing because no one wrote it."
                "It was hidden because something was placed over it."

            "Put up a new warning about littering.":
                "That makes the harm too small."
                "This was never only about litter."

            "Pull the tourist sign away.":
                play sound "audio/mangrove/mangrove-wood-creak.m4a"
                "You grip the edge of the tourist sign."
                "The wood groans as it pulls loose from the older post beneath it."
                "For a moment, the spring is quiet."
                "Then the tourist sign comes free."
                $ signRemoved = True
                jump mirror_pool_sign_removed

label mirror_pool_sign_removed:
    scene spring_bg_without_sign at fit_screen
    with Dissolve(0.5)

    "The tourist name no longer gets the last word."
    "The spring is still dark."
    "The mangroves still hold what they were made to hold."
    "But the sign is gone now."

    "You are still holding Thia's bottle, filled with the spring water you collected earlier."

    call mirror_pool_final_bottle_resolution from _call_mirror_pool_final_bottle_resolution
    return

label mirror_pool_final_bottle_resolution:
    scene spring_bg_without_sign at fit_screen
    with Dissolve(0.5)

    "The bottle is still in your hand, heavy with spring water."
    "The spring has returned what it needed to return."

    "What do you do with Thia’s bottle now?"

    while True:
        menu:
            "Leave it by the spring.":
                "You start to set the bottle down."
                "Hmm... no."
                "The bottle was not left in mourning."
                "It was left because Thia assumed the place would hold it for her."

            "Throw it away again.":
                "You look toward the trash bin."
                "But this is not about making the bottle disappear anymore."

            "Carry it away.":
                "You cap the bottle and carry it away from the spring."
                "This time, it does not pull back toward the water."
                "It is only a bottle now."
                $ bottleResolved = True
                $ puzzleSolved = True
                $ journal_update_friend(
                    "thia",
                    note="Thia’s affliction was tied to the Mirror Pool, a mourning site renamed for tourists after being used as Waste Channel 3. The hidden marks beneath the tourist sign decoded to: MOTHER SPRING REMEMBERS.",
                    solved=True
                )
                $ journal_remove_item("mirror_pool.bottle_of_spring_water")
                $ journal_remove_item("museum.spring_fragments")
                $ journal_remove_item("mirror_pool.hidden_sign_marks")
                $ journal_remove_item("mirror_pool.decoded_message")
                $ journal_remove_item("empty_home.basement.crumpled_code_note")
                jump mirror_pool_thia_message


label mirror_pool_thia_message:
    stop ambience fadeout 1.0
    play music "audio/mangrove/mangrove-solve.mp3" fadein 1.0
    "Message from Thia:"
    show thia_sprite onlayer master at thia_left_speaker zorder 2000
    "Something changed."
    "I threw something away today and it stayed gone."
    "But I don’t think it was because I finally got rid of it."
    "I think it was because I stopped asking the wrong place to hold it."
    "Thia’s affliction has eased."
    $ journal_update_friend("thia", note="Thia's affliction has eased.", solved=True)
    hide thia_sprite onlayer master

    menu:
        "Return to Map":
            return
        "Stay at the Spring":
            pass

    return
