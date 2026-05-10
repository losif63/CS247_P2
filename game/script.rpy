define m = Character('Me', color="#c8c8ff")
image intro = "intro.png"

define FANON_BODY = ("\"Colonialism is not satisfied merely with holding a people in its grip "
    "and emptying the native's brain of all form and content. By a kind of perverted logic, "
    "it turns to the past of the oppressed people, and distorts, disfigures, and destroys it.\"")
define FANON_SOURCE = "—FRANTZ FANON, The Wretched of the Earth"

define FAULKNER_BODY = "\"The past is never dead. It’s not even past.\""
define FAULKNER_SOURCE = "—WILLIAM FAULKNER, Requiem for a Nun"

define SHIRE_BODY = "\"I tried to leave you behind but I am made of everything you ever put me through.\""
define SHIRE_SOURCE = "–WARSAN SHIRE"

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

    scene intro
    
    "An eerie atmosphere creeps in as I approach Pelau Siring."
    
    m "Well, here I am again. All alone, this time..."

    "Last month, I visited this place for my summer vacation with 5 of my friends - Evelyn, Mark, Jessica, Darvin, and Stephen."

    "After returning from the vacation, strange symptoms have appeared. I was the only one unaffected."

    "The doctors couldn't identify what's wrong with them. Something tells me that the secret lies in this village..."
    
