from worlds.AutoWorld import World
from BaseClasses import Region, Location, Item, Tutorial

from .Items import M1Item, item_table, item_name_to_id
from .Locations import M1Location, location_table, location_name_to_id
from .Options import M1Options
from .Regions import create_regions
from .Rules import set_rules

class M1World(World):
    """
    Mother 1, known as EarthBound Beginnings in the West, is the first game in the
    Mother series of RPGs. It follows the story of Ninten, a young boy with psychic
    powers, as he travels the world to collect eight melodies and stop a looming
    alien invasion.
    """
    game: str = "Mother 1"

    options_dataclass = M1Options
    options: M1Options

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    item_name_groups = {
        "Melodies": {
            "First Melody",
            "Second Melody",
            "Third Melody",
            "Fourth Melody",
            "Fifth Melody",
            "Sixth Melody",
            "Seventh Melody",
            "Eighth Melody",
        }
    }
    location_name_groups = {}

    def create_item(self, name: str) -> Item:
        """Create a single Mother 1 item."""
        data = item_table[name]
        return M1Item(name, data.classification, data.code, self.player)

    def create_regions(self):
        """Create the regions and locations for the world."""
        create_regions(self)

    def set_rules(self):
        """Set the access rules for locations and regions."""
        set_rules(self)

    def create_itempool(self):
        """Create the item pool for the world."""
        # For now, we will create a simple item pool with all items.
        # This will be expanded in a later phase to handle options and filler.
        for name in self.item_name_to_id.keys():
            self.multiworld.itempool.append(self.create_item(name))

        # Lock the victory item to the final boss event
        victory = self.create_item("Victory")
        self.multiworld.get_location("Giegue's Ship - Defeat Giegue", self.player).place_locked_item(victory)
        self.multiworld.itempool.remove(victory)
