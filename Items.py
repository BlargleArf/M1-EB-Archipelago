from BaseClasses import Item, ItemClassification

# The base ID for all Mother 1 items. This should be unique to this APWorld.
BASE_ID = 1989000

class M1Item(Item):
    """
    A Mother 1 item.
    """
    game: str = "Mother 1"

class ItemData:
    """
    A dataclass to hold information about a Mother 1 item.
    """
    def __init__(self, code: int, classification: ItemClassification):
        self.code = code
        self.classification = classification

# The main table of all items in the game.
# The keys are the item names, and the values are the item data.
item_table = {
    # Progression Items (Melodies)
    "First Melody":     ItemData(BASE_ID + 0, ItemClassification.progression),
    "Second Melody":    ItemData(BASE_ID + 1, ItemClassification.progression),
    "Third Melody":     ItemData(BASE_ID + 2, ItemClassification.progression),
    "Fourth Melody":    ItemData(BASE_ID + 3, ItemClassification.progression),
    "Fifth Melody":     ItemData(BASE_ID + 4, ItemClassification.progression),
    "Sixth Melody":     ItemData(BASE_ID + 5, ItemClassification.progression),
    "Seventh Melody":   ItemData(BASE_ID + 6, ItemClassification.progression),
    "Eighth Melody":    ItemData(BASE_ID + 7, ItemClassification.progression),

    # Progression Items (Keys and Quest Items)
    "Zoo Key":          ItemData(BASE_ID + 8, ItemClassification.progression),
    "Pass":             ItemData(BASE_ID + 9, ItemClassification.progression), # For the train
    "Rocket":           ItemData(BASE_ID + 10, ItemClassification.progression), # For the rocket
    "Ghost's Key":      ItemData(BASE_ID + 11, ItemClassification.progression), # For the haunted house

    # Useful Items
    "Franklin Badge":   ItemData(BASE_ID + 12, ItemClassification.useful),
    "Magic Coin":       ItemData(BASE_ID + 13, ItemClassification.useful),
    "Magic Herb":       ItemData(BASE_ID + 14, ItemClassification.useful),
    
    # Filler Items (Example Weapons, more to be added)
    "Plastic Bat":      ItemData(BASE_ID + 15, ItemClassification.filler),
    "Wooden Bat":       ItemData(BASE_ID + 16, ItemClassification.filler),
    "Slingshot":        ItemData(BASE_ID + 17, ItemClassification.filler),

    # Victory Condition
    "Victory":          ItemData(BASE_ID + 100, ItemClassification.progression),
}

# A mapping of item names to their unique Archipelago IDs.
item_name_to_id = {name: data.code for name, data in item_table.items()}
