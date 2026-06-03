################################################################################
## Empty Home — Exploration Tree
##
## Tree structure:
##   empty_home
##   ├── empty_home.living_room
##   ├── empty_home.backyard
##   └── empty_home.basement_door
##
## To add a child to an existing node: add its ID to the parent's "children"
## list and add a new entry to EXPLORE_NODES. To add a puzzle, set "puzzle"
## to a label name and define that label below.
################################################################################


image emptyhome_livingroom = "images/emptyhome_livingroom.png"
image emptyhome_backyard = "images/emptyhome_backyard.png"
image emptyhome_basement = "images/emptyhome_basement.png"


init python:
    renpy.music.register_channel("atmosphere", "sfx", loop=False)
    renpy.music.register_channel("atmosphere2", "sfx", loop=False)

    EXPLORE_NODES.update({

        "empty_home": {
            "name":       "Empty Home",
            "parent":     None,
            "intro":      "empty_home_intro",
            "on_enter":   "empty_home_on_enter",
            "children":   [
                "empty_home.living_room",
                "empty_home.backyard",
                "empty_home.basement_door",
            ],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.living_room": {
            "name":       "Living Room",
            "parent":     "empty_home",
            "intro":      "empty_home_living_room_intro",
            "on_enter":   "empty_home_living_room_on_enter",
            "children":   ["empty_home.living_room.drawer", "empty_home.living_room.couch", "empty_home.living_room.table"],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.living_room.drawer": {
            "name":       "Drawer",
            "parent":     "empty_home.living_room",
            "intro":      "empty_home_living_room_drawer_intro",
            "children":   [],
            "objects": [
                {
                    "id":        "empty_home.living_room.drawer.top",
                    "name":      "Top Drawer",
                    "item":      None,
                    "action":    "empty_home_drawer_top_action",
                    "msg_first": "The top drawer slides open. Nothing but old receipts and a broken pen.",
                    "msg_done":  "Just old receipts.",
                },
                {
                    "id":        "empty_home.living_room.drawer.middle",
                    "name":      "Middle Drawer",
                    "item":      "empty_home.basement_door.key",
                    "action":    "empty_home_drawer_middle_action",
                    "msg_first": "You find a {item}small key{/item} taped to the back of the drawer.",
                    "msg_done":  "The middle drawer is empty.",
                },
                {
                    "id":        "empty_home.living_room.drawer.bottom",
                    "name":      "Bottom Drawer",
                    "item":      None,
                    "action":    "empty_home_drawer_bottom_action",
                    "msg_first": "Stuck. The bottom drawer won't budge no matter how hard you pull.",
                    "msg_done":  "Still stuck.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.living_room.couch": {
            "name":       "Couch",
            "parent":     "empty_home.living_room",
            "intro":      "empty_home_living_room_couch_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.living_room.table": {
            "name":       "Table",
            "parent":     "empty_home.living_room",
            "intro":      "empty_home_living_room_table_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "empty_home.living_room.table.picture",
                    "name":      "Family Photo",
                    "item":      None,
                    "action":    "empty_home_photo_assemble",
                    "msg_first": "",
                    "msg_done":  "The reassembled photo sits in its frame.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.backyard": {
            "name":       "Backyard",
            "parent":     "empty_home",
            "intro":      "empty_home_backyard_intro",
            "on_enter":   "empty_home_backyard_on_enter",
            "children":   ["empty_home.backyard.swing", "empty_home.backyard.garden"],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.backyard.swing": {
            "name":       "Swing",
            "parent":     "empty_home.backyard",
            "intro":      "empty_home_backyard_swing_intro",
            "children":   [],
            "objects":    [
                {
                    "id":        "empty_home.backyard.left_swing",
                    "name":      "Left Swing",
                    "item":      "empty_home.backyard.swing.photo",
                    "action":    None,
                    "msg_first": "There seems to be a {item}piece of a photo{/item} lying on top of the seat. The piece shows a young girl smiling.",
                    "msg_done":  "There is nothing on the swing.",
                },
                {
                    "id":        "empty_home.backyard.right_swing",
                    "name":      "Right Swing",
                    "item":      None,
                    "action":    None,
                    "msg_first": "There is nothing on the swing.",
                    "msg_done":  "There is nothing on the swing.",
                },
            ],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.backyard.garden": {
            "name":       "Garden",
            "parent":     "empty_home.backyard",
            "intro":      "empty_home_backyard_garden_intro",
            "children":   [],
            "objects":    [],
            "puzzle":     None,
            "requires":   None,
            "unlock":     None,
            "locked_msg": None,
        },

        "empty_home.basement_door": {
            "name":       "Basement",
            "parent":     "empty_home",
            "intro":      "empty_home_basement_door_intro",
            "on_enter":   "empty_home_basement_on_enter",
            "children":   [],
            "objects":    [
                {
                    "id":        "empty_home.basement.bookshelf",
                    "name":      "Bookshelf",
                    "item":      "empty_home.basement.diary",
                    "action":    "empty_home_bookshelf_action",
                    "msg_first": [
                        "There seems to be a bookshelf alongside the back wall of the basement.",
                        "An uncanny book immediately catches your eye - it says {item}Sonia's Diary{/item} on the front cover.",
                        "You reach out your hand and turn the pages. It seems like this belonged to a girl a long time ago.",
                        '"April 15th, 1925."',
                        '"It was rainy today. Mommy also looked really sad. Maybe she doesn\'t like rain."',
                        '"I wanted to cheer mommy up, so we played hide and seek together!"',
                        '"Mommy played it. She told me to stay hidden in the basement - and that I should never come out no matter what, even if mommy calls me."',
                        '"So I hid in the basement and stayed there forever! Mommy never found me."',
                        '"I heard a lot of footsteps and shouting upstairs - it seems like mommy invited neighbors to play as well."',
                        '"After a few hours I became hungry, so I came out of the basement. Mommy was missing - and there were policemen around my house."',
                        '"I asked the policemen where mommy and daddy is. He told me that daddy is at the {place}city hall{/place}, and mommy went to the {place}hospital{/place} because she was sick."',
                        '"I am starving. I hope she comes back soon."',
                        "You close the book."
                    ],
                    "msg_done":  "You've already viewed this bookshelf.",
                },
                {
                    "id":        "empty_home.basement.crumpled_code_note",
                    "name":      "Crumpled Paper Behind Bookshelf",
                    "item":      "empty_home.basement.crumpled_code_note",
                    "action":    "empty_home_crumpled_code_note_action",
                    "msg_first": [
                        "Behind the rack, something brittle catches against the wood.",
                        "You pull out a crumpled paper, damp at the edges but still readable.",
                        "The paper only has one sentence:",
                        "\"Water reveals hidden writing.\"",
                    ],
                    "msg_done": "The paper is already in your notes.",
                },
            ],
            "puzzle":     None,
            "requires":   "empty_home.basement_door.key",
            "unlock":     "empty_home_basement_unlock",
            "locked_msg": "The door is locked. Perhaps there is a key somewhere?",
        },

    })

    ITEM_CATALOG.update({
        "empty_home.basement_door.key": {
            "name": "Basement Key",
            "location": "Empty Home - Living Room",
            "description": "Key that opens the basement door of the empty home."
        },

        "empty_home.basement.diary": {
            "name": "Sonia's Diary",
            "location": "Empty Home - Basement",
            "description": "Diary of a girl named Sonia. It states that her dad is at the {place}city hall{/place}, and her mom is at the {place}hospital{/place}."
        },

        "empty_home.backyard.swing.photo": {
            "name": "Photo Piece 3",
            "location": "Empty Home - Backyard",
            "description": "A piece of a torn photo. The piece shows a young girl smiling."
        },

        "empty_home.basement.crumpled_code_note": {
            "name": "Crumpled Water Note",
            "location": "Empty Home - Basement",
            "description": "A damp, crumpled paper found behind the basement rack. It reads: \"Water reveals hidden writing.\""
        },

    })


# ── Entry point (called from the village map loop) ────────────────────────────

label empty_home_scene:
    call explore_node("empty_home") from _call_empty_home_root
    return


# ── Intro labels (called once per node on first visit) ────────────────────────

label empty_home_intro:
    scene emptyhome at fit_screen
    with Dissolve(0.5)
    play sound "audio/home/home-enter-door.wav"
    "The door to the empty home swings open at your touch — it wasn't locked."
    "A layer of dust coats everything. Furniture still in place, as if the occupants simply vanished."
    return

label empty_home_living_room_intro:
    scene emptyhome_livingroom at fit_screen
    with Dissolve(0.5)
    "You step into the living room."
    "A sofa, a low table, a radio on the shelf — all arranged with a care that makes the emptiness worse."
    "A child's drawing is pinned to the wall. You don't want to look at it too long."
    return

label empty_home_living_room_drawer_intro:
    "You investigate the drawer at the corner of the living room."
    return

label empty_home_living_room_couch_intro:
    "You investigate the couch at the center of the living room."
    "It's quite old fashioned and heavily worn out."
    return

label empty_home_living_room_table_intro:
    "A table sits at the center of the living room."
    return

label empty_home_backyard_intro:
    scene emptyhome_backyard at fit_screen
    with Dissolve(0.5)
    "The backyard is overgrown, weeds swallowing what was once a tended vegetable garden."
    "A rusted watering can lies on its side by the door. The soil around it is dry and cracked."
    return

label empty_home_backyard_swing_intro:
    "There is an empty swing in the middle of the vegetable garden. You make your way through the weeds toward the swing."
    return

label empty_home_backyard_garden_intro:
    "There is a garden in the middle of the backyard - it seems that it hasn't been tended for years."
    "You notice weeds and all sorts of wild plants growing in the garden."
    return

label empty_home_basement_door_intro:
    scene emptyhome_basement at fit_screen
    with Dissolve(0.5)
    "The basement is eerie and cold."
    return


# ── on_enter labels (background, called every visit) ──────────────────────────

label empty_home_on_enter:
    scene emptyhome at fit_screen
    with Dissolve(0.5)
    return

label empty_home_living_room_on_enter:
    scene emptyhome_livingroom at fit_screen
    with Dissolve(0.5)
    return

label empty_home_backyard_on_enter:
    scene emptyhome_backyard at fit_screen
    with Dissolve(0.5)
    return

label empty_home_basement_on_enter:
    scene emptyhome_basement at fit_screen
    with Dissolve(0.5)
    return

label empty_home_basement_unlock:
    play sound "audio/home/basement-door-open.wav"
    "You fit the key into the lock. It turns with a heavy click."
    "The door swings inward. Cold air rises from below."
    # The key has served its purpose — drop it from the inventory.
    $ journal_remove_item("empty_home.basement_door.key")
    return

label empty_home_crumpled_code_note_action:
    if waterNoteFound:
        "You've already noted the crumpled paper."
        return

    $ waterNoteFound = True
    play sound "audio/home/home-paper-crumple.wav"
    "Behind the rack, something brittle catches against the wood."
    "You pull out a {item}crumpled paper{/item}, damp at the edges but still readable."
    "The paper only has one sentence:"
    "\"Water reveals hidden writing.\""
    # $ journal_add_item(
    #     "empty_home.basement.crumpled_water_note",
    #     "Crumpled Water Note",
    #     "Empty Home - Basement",
    #     "A damp, crumpled paper found behind the basement rack. It reads: \"Water reveals hidden writing.\""
    # )
    return


# ── Bookshelf action label ────────────────────────────────────────────────────

label empty_home_bookshelf_action:
    "There seems to be a bookshelf alongside the back wall of the basement."
    "An uncanny book immediately catches your eye - it says {item}Sonia's Diary{/item} on the front cover."
    play sound "audio/home/home-basement-turn-pages.wav"
    "You reach out your hand and turn the pages. It seems like this belonged to a girl a long time ago."
    "\"April 15th, 1925.\""
    play ambience "audio/home/home-rain.wav" loop fadein 2.0
    "\"It was rainy today. Mommy also looked really sad. Maybe she doesn't like rain.\""
    "\"I wanted to cheer mommy up, so we played hide and seek together!\""
    "\"Mommy played it. She told me to stay hidden in the basement - and that I should never come out no matter what, even if mommy calls me.\""
    "\"So I hid in the basement and stayed there forever! Mommy never found me.\""
    play music "audio/home/home-mob.wav" fadein 1.0
    play sound "audio/home/home-ransack.wav"
    play atmosphere "audio/home/home-footsteps-1.wav"
    play atmosphere2 "audio/home/home-basement-footsteps-2.wav"
    "\"I heard a lot of footsteps and shouting upstairs - it seems like mommy invited neighbors to play as well.\""
    "\"After a few hours I became hungry, so I came out of the basement. Mommy was missing - and there were policemen around my house.\""
    "\"I asked the policemen where mommy and daddy is. He told me that daddy is at the {place}city hall{/place}, and mommy went to the {place}hospital{/place} because she was sick.\""
    "\"I am starving. I hope she comes back soon.\""
    stop music fadeout 2.0
    stop ambience fadeout 2.0
    stop atmosphere fadeout 2.0
    stop atmosphere2 fadeout 2.0
    "You close the book."

    # If the player has already investigated the locations the diary points to,
    # acknowledge it so they aren't sent back to a place they've already cleared.
    $ visited_cityhall = "city_hall.joaquin_page" in collected_items and "city_hall.execution_page" in collected_items
    $ visited_hospital = "hospital.basement.morgue.emilia.photo" in collected_items
    if visited_cityhall and not visited_hospital:
        m "I already visited the city hall and collected the interrogation files and the execution records."
        m "There might be something left to uncover in the {place}hospital{/place}. Maybe I should go there."
    elif not visited_cityhall and visited_hospital:
        m "I already visited the hospital. I've found the photo piece in the morgue."
        m "There might be something left to uncover in the {place}city hall{/place}. Maybe I should go there."
    elif visited_cityhall and visited_hospital:
        m "I already finished exploring both the city hall and the hospital. I shouldn't need to revisit them."
    return



# ── Drawer action labels ──────────────────────────────────────────────────────

label empty_home_drawer_top_action:
    play sound "audio/home/home-drawer-open.wav"
    "The top drawer slides open. Nothing but old receipts and a broken pen."
    return

label empty_home_drawer_middle_action:
    play sound "audio/home/home-drawer-open.wav"
    "You find a {item}small key{/item} taped to the back of the drawer."
    play sound "audio/home/home-key-found.wav"
    return

label empty_home_drawer_bottom_action:
    play sound "audio/home/home-jammed-drawer.wav"
    "Stuck. The bottom drawer won't budge no matter how hard you pull."
    return


# ── Photo assembly puzzle ─────────────────────────────────────────────────────

label empty_home_photo_assemble:
    $ _pieces_needed = [
        "church.backyard.lawn.photo_piece",
        "hospital.basement.morgue.emilia.photo",
        "empty_home.backyard.swing.photo",
    ]
    $ _missing = sum(1 for p in _pieces_needed if p not in collected_items)
    if _missing > 0:
        $ _piece_word = "piece" if _missing == 1 else "pieces"
        "You need to collect [_missing] more [_piece_word] to assemble the photo."
        $ interacted_objects = set(x for x in interacted_objects if x != "empty_home.living_room.table.picture")
    else:
        call empty_home_photo_flashback from _call_empty_home_photo_flashback
        call empty_home_photo_present from _call_empty_home_photo_present
    return


label empty_home_photo_flashback:
    $ Yuna = Character("Yuna", color="#aad4f5")

    scene yuna
    with Dissolve(1.0)

    "A memory surfaces — early in the trip, before anything felt wrong."
    "The group had wandered into a quieter part of the village, past the market stalls and down a dirt road lined with overgrown hedges."
    "A cluster of children appeared from behind a gate, small hands outstretched, voices overlapping."

    "One of them tugged at Yuna's sleeve."
    Yuna "Don't touch me."

    "The child flinched but didn't step back. The others kept asking — for coins, for food, for anything."
    "A woman came rushing out from further down the road, breathless, bowing her head."
    "\"I'm so sorry — I'm so sorry, please forgive them, they don't mean any harm—\""

    Yuna "Then teach them some manners. Children who beg from strangers are an embarrassment to whoever is supposed to be raising them."
    Yuna "If you can't manage them, perhaps you shouldn't be."

    "The nanny went quiet. The children stared."
    "You remember how the smallest one slowly lowered her hand."
    "No one said anything after that. The group kept walking."

    scene black
    with Dissolve(1.0)
    return


label empty_home_photo_present:
    "The three pieces fit together perfectly."
    "A family portrait — a man, a woman, a little girl. All smiling."
    "You set it back in the frame and look at it for a long time."

    m "Joaquin Gonzalez."
    "The name from the city hall archive. Arrested for instigating independence riots. Interrogation Method 3A. Executed and buried in the church backyard."
    m "He's the father."

    m "Emilia Gonzalez."
    "The name tag in the hospital morgue. A unit with a photo piece inside — someone put it there deliberately, or it was left behind when she was taken."
    m "She's the mother. Taken for experimentation. She didn't survive either."

    m "And Sonia."
    "The handwriting in the diary. A little girl hiding in the basement, waiting for a mother who was never going to come home."
    "She waited. She came upstairs to find policemen. She asked where her parents were."
    "She was told her father was at city hall. Her mother was at the hospital."
    "Both were already gone."

    m "She grew up without them. In this house, or somewhere after it — she grew up alone."

    "You think about the children on the road."
    "The small hand reaching out. Yuna's voice cutting it down."
    "Those children at the orphanage — they had the same look Sonia must have had."
    "Waiting for someone. Not understanding why no one came."

    m "Yuna didn't see them. She saw an inconvenience."
    m "But I wonder if somewhere, underneath all of that — she already knew what it felt like to lose them."
    m "She just hadn't admitted it yet."

    "Your phone buzzes."
    "A message from Yuna's roommate: {i}I don't know what happened, but she slept through the night. No screaming. She says the dreams are gone.{/i}"
    m "..."
    m "She's going to be okay."

    $ journal_update_friend("yuna", note="Her recurring dreams mirrored the fate of the Gonzalez family exactly — a father dragged away and killed, a mother taken for illegal experimentation. The village made her live through what she had refused to see in the children on the road.", solved=True)
    $ journal_remove_item("church.backyard.lawn.photo_piece")
    $ journal_remove_item("hospital.basement.morgue.emilia.photo")
    $ journal_remove_item("empty_home.backyard.swing.photo")
    $ journal_remove_item("empty_home.basement.diary")

    return
