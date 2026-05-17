################################################################################
## Exploration Engine
##
## Each location file registers its subtree in EXPLORE_NODES via init python.
## The generic explore_node label drives all navigation — no per-location logic.
##
## Node dict schema:
##   name       (str)        — display name shown in nav buttons
##   parent     (str|None)   — parent node ID; None for root nodes
##   intro      (str|None)   — Ren'Py label called on first visit; None = silent
##   children   (list[str])  — child node IDs shown as nav buttons
##   objects    (list[dict]) — interactable objects at this node (see object schema)
##   puzzle     (str|None)   — label called for puzzle; tracked in solved_puzzles
##   requires   (str|None)   — item ID in collected_items required to unlock node
##   unlock     (str|None)   — label called the first time player unlocks this node
##   locked_msg (str|None)   — Notify text shown when clicking locked without item
##
## Object dict schema (one entry in "objects"):
##   id        (str)      — globally unique ID (e.g. "location.node.object_name")
##   name      (str)      — button label
##   item      (str|None) — item ID added to collected_items on first interaction
##   action    (str|None) — label called on first interaction; None = show msg_first
##   msg_first (str)      — narration shown on first interaction (when action is None)
##   msg_done  (str)      — Notify text shown on all subsequent interactions
################################################################################

init -1 python:
    EXPLORE_NODES = {}


# ── Persistent exploration state ──────────────────────────────────────────────

default visited_nodes      = set()
default collected_items    = set()
default solved_puzzles     = set()
default unlocked_nodes     = set()
default interacted_objects = set()


# ── Styles ────────────────────────────────────────────────────────────────────

style explore_nav_frame:
    background "#000000cc"
    padding (30, 24, 30, 24)

style explore_location_text:
    color "#aaaaaa"
    size 20
    italic True
    text_align 0.5

style explore_child_button:
    background Frame("#333333bb", 6, 6)
    hover_background Frame("#666666cc", 6, 6)
    padding (16, 12)
    xsize 480

style explore_child_button_text:
    color "#ffffff"
    hover_color "#ffdd88"
    size 26
    text_align 0.5

style explore_locked_button is explore_child_button:
    background Frame("#1a1a1a99", 6, 6)

style explore_locked_button_text is explore_child_button_text:
    color "#555555"
    hover_color "#555555"

style explore_unlockable_button is explore_child_button:
    background Frame("#26567dbb", 6, 6)
    hover_background Frame("#82c8fecc", 6, 6)

style explore_unlockable_button_text is explore_child_button_text:
    color "#ffffff"
    hover_color "#ffdd88"

style explore_back_button is explore_child_button:
    background Frame("#1a1a1a99", 6, 6)
    hover_background Frame("#444444cc", 6, 6)

style explore_back_button_text is explore_child_button_text:
    color "#888888"
    hover_color "#ffffff"
    size 22

style explore_object_button is explore_child_button:
    background Frame("#2a1a0099", 6, 6)
    hover_background Frame("#5a3a00cc", 6, 6)

style explore_object_button_text is explore_child_button_text:
    color "#ddaa44"
    hover_color "#ffcc66"
    size 24


# ── Navigation screen ─────────────────────────────────────────────────────────

screen explore_nav_screen(node_name, children, objects, has_parent):
    modal True

    frame:
        style "explore_nav_frame"
        xalign 0.5
        yalign 0.85
        xmaximum 560

        vbox:
            xfill True
            spacing 10

            text "[node_name]":
                style "explore_location_text"
                xalign 0.5

            null height 4

            for obj in objects:
                $ _used     = obj["id"] in interacted_objects
                $ _obj_name = obj["name"]
                if _used:
                    textbutton "[_obj_name]":
                        style "explore_locked_button"
                        action Notify(obj["msg_done"])
                        xalign 0.5
                else:
                    textbutton "[_obj_name]":
                        style "explore_object_button"
                        action Return(("object", obj["id"]))
                        xalign 0.5

            if objects and children:
                null height 4

            for child_id in children:
                $ _cn         = EXPLORE_NODES[child_id]
                $ _cn_name    = _cn["name"]
                $ _locked     = _cn["requires"] is not None and child_id not in unlocked_nodes
                $ _can_unlock = _locked and _cn["requires"] in collected_items
                if _can_unlock:
                    $ _unlocked_label = _cn_name + " (unlocked)"
                    textbutton "[_unlocked_label]":
                        style "explore_unlockable_button"
                        action Return(("unlock", child_id))
                        xalign 0.5
                elif _locked:
                    $ _msg = _cn["locked_msg"] if _cn["locked_msg"] else "It's locked."
                    $ _locked_label = _cn_name + " (locked)"
                    textbutton "[_locked_label]":
                        style "explore_locked_button"
                        action Notify(_msg)
                        xalign 0.5
                else:
                    textbutton "[_cn_name]":
                        style "explore_child_button"
                        action Return(child_id)
                        xalign 0.5

            null height 4

            if has_parent:
                textbutton "← Go Back":
                    style "explore_back_button"
                    action Return("Back")
                    xalign 0.5
            else:
                textbutton "← Go Back":
                    style "explore_locked_button"
                    action NullAction()
                    xalign 0.5

            textbutton "← Finish Investigation & Leave":
                style "explore_back_button"
                action Return("Leave")
                xalign 0.5

# ── Generic exploration label ─────────────────────────────────────────────────

label explore_node(node_id):
    $ _node = EXPLORE_NODES[node_id]

    # Play intro on first visit only
    if node_id not in visited_nodes:
        $ visited_nodes.add(node_id)
        if _node["intro"] is not None:
            call expression _node["intro"] from _call_explore_intro

    # Trigger unsolved puzzle
    if _node["puzzle"] is not None and _node["puzzle"] not in solved_puzzles:
        call expression _node["puzzle"] from _call_explore_puzzle
        $ solved_puzzles.add(_node["puzzle"])

    # Show nav buttons until player leaves
    if _node["children"] or _node.get("objects"):
        $ _exploring = True
        while _exploring:
            call screen explore_nav_screen(_node["name"], _node["children"], _node.get("objects", []), _node["parent"] is not None)
            if isinstance(_return, tuple) and _return[0] == "unlock":
                $ _unlock_node = EXPLORE_NODES[_return[1]]
                $ _unlock_node_name = _return[1]
                if _unlock_node["unlock"] is not None:
                    call expression _unlock_node["unlock"] from _call_explore_unlock
                else:
                    $ _unlock_name = _unlock_node["name"]
                    "[_unlock_name] is now accessible."
                $ unlocked_nodes.add(_unlock_node_name)
            elif isinstance(_return, tuple) and _return[0] == "object":
                $ _obj = next(o for o in _node["objects"] if o["id"] == _return[1])
                $ interacted_objects.add(_obj["id"])
                if _obj["item"] is not None:
                    $ collected_items.add(_obj["item"])
                if _obj["action"] is not None:
                    call expression _obj["action"] from _call_explore_object
                else:
                    $ _obj_msg = _obj["msg_first"]
                    "[_obj_msg]"
            elif _return == "Back":
                call explore_node(_node["parent"]) from _call_explore_parent
            elif _return == "Leave":
                $ _exploring = False
                $ visited_nodes = set()
            elif isinstance(_return, str):
                call explore_node(_return) from _call_explore_recurse

    return
