

init -1 python:
    ITEM_CATALOG = {}


# ── Item-highlight text tag ───────────────────────────────────────────────────
# Use {item}...{/item} in any dialogue/narration to highlight text that signifies
# picking up or noticing a collectible item. To recolor every highlight in the
# game, change ITEM_COLOR in one place here.

init python:
    ITEM_COLOR = "#6fcf97"

    def _item_text_tag(tag, argument, contents):
        return (
            [(renpy.TEXT_TAG, "color=" + ITEM_COLOR), (renpy.TEXT_TAG, "b")]
            + contents
            + [(renpy.TEXT_TAG, "/b"), (renpy.TEXT_TAG, "/color")]
        )

    config.custom_text_tags["item"] = _item_text_tag


# ── Location-hint text tag ────────────────────────────────────────────────────
# Use {place}...{/place} in any dialogue/narration to highlight a location the
# player is being pointed toward. To recolor every hint in the game, change
# PLACE_COLOR in one place here.

    PLACE_COLOR = "#ffa733"

    def _place_text_tag(tag, argument, contents):
        return (
            [(renpy.TEXT_TAG, "color=" + PLACE_COLOR), (renpy.TEXT_TAG, "b")]
            + contents
            + [(renpy.TEXT_TAG, "/b"), (renpy.TEXT_TAG, "/color")]
        )

    config.custom_text_tags["place"] = _place_text_tag
