################################################################################
## Exploration Engine
##
## Each location file registers its subtree in EXPLORE_NODES via init python.
## The generic explore_node label drives all navigation — no per-location logic.
##
## Node dict schema:
##   name     (str)       — display name shown in nav buttons
##   parent   (str|None)  — parent node ID; None for root nodes
##   intro    (str|None)  — Ren'Py label called on first visit; None = silent
##   children (list[str]) — child node IDs shown as nav buttons
##   puzzle   (str|None)  — label called for puzzle; tracked in solved_puzzles
##   requires (str|None)  — item ID in collected_items required to enter node
################################################################################

init -1 python:
    EXPLORE_NODES = {}


# ── Persistent exploration state ──────────────────────────────────────────────

default visited_nodes   = set()
default collected_items = set()
default solved_puzzles  = set()


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

style explore_back_button is explore_child_button:
    background Frame("#1a1a1a99", 6, 6)
    hover_background Frame("#444444cc", 6, 6)

style explore_back_button_text is explore_child_button_text:
    color "#888888"
    hover_color "#ffffff"
    size 22


# ── Navigation screen ─────────────────────────────────────────────────────────

screen explore_nav_screen(node_name, children, has_parent):
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

            for child_id in children:
                $ _cn      = EXPLORE_NODES[child_id]
                $ _cn_name = _cn["name"]
                $ _locked  = _cn["requires"] is not None and _cn["requires"] not in collected_items
                if _locked:
                    $ _locked_label = _cn_name + " (locked)"
                    textbutton "[_locked_label]":
                        style "explore_locked_button"
                        action NullAction()
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
    if _node["children"]:
        $ _exploring = True
        while _exploring:
            call screen explore_nav_screen(_node["name"], _node["children"], _node["parent"] is not None)
            $ _nav_choice = _return if isinstance(_return, str) else None
            if _nav_choice == 'Back':
                call explore_node(_node["parent"]) from _call_explore_parent
            elif _nav_choice == 'Leave':
                $ _exploring = False
                # Reset visited nodes
                $ visited_nodes = set()
            else:
                call explore_node(_nav_choice) from _call_explore_recurse

    return
