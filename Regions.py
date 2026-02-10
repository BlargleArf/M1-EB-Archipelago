from BaseClasses import Region, Entrance
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import M1World

def create_regions(world: "M1World"):
    """
    Creates all the regions for the Mother 1 world and connects them.
    """
    player = world.player
    multiworld = world.multiworld

    # Create all regions based on the provided list
    menu = Region("Menu", player, multiworld)
    magicant = Region("Magicant", player, multiworld)
    duncans_factory = Region("Duncan's Factory", player, multiworld)
    mt_itoi = Region("Mt. Itoi", player, multiworld)
    crystal_cavern = Region("Crystal Cavern", player, multiworld)
    yucca_desert = Region("Yucca Desert", player, multiworld)
    podunk = Region("Podunk", player, multiworld)
    rosemarys_house = Region("Rosemary's House", player, multiworld)
    spookane = Region("Spookane", player, multiworld)
    giegue_ship = Region("Giegue's Ship", player, multiworld) # Final area

    # Add locations to their respective regions
    podunk.locations += [
        multiworld.get_location("Ninten's Basement - Chest", player),
        multiworld.get_location("South of Podunk - Cave Chest", player),
        multiworld.get_location("Ninten's House - Sister", player),
        multiworld.get_location("Canary Village - Canary's Chick", player), # Canary Village is part of Podunk area
        multiworld.get_location("Zoo - Superintendent", player), # The Zoo is part of Podunk area
        multiworld.get_location("Podunk - Mayor's House Present", player),
    ]
    magicant.locations += [
        multiworld.get_location("Magicant - Queen Mary", player),
    ]
    spookane.locations += [
        multiworld.get_location("Spookane - Ghost's Piano", player),
    ]
    rosemarys_house.locations += [
        multiworld.get_location("Rosemary's House - West Room Chest", player),
    ]
    yucca_desert.locations += [
        multiworld.get_location("Yucca Desert - Cactus", player),
    ]
    duncans_factory.locations += [
        multiworld.get_location("Duncan's Factory - Present", player),
    ]
    # Swamp is part of the path to Mt Itoi, will treat it as part of Mt. Itoi for now
    mt_itoi.locations += [
        multiworld.get_location("Swamp - Underwater Palace Robot", player),
        multiworld.get_location("Mt. Itoi - Robot's Grave", player),
    ]
    crystal_cavern.locations += [
        multiworld.get_location("Mt. Itoi - Eve's Remains", player), # Eve is in the Crystal Cavern
    ]
    giegue_ship.locations += [
        multiworld.get_location("Giegue's Ship - Defeat Giegue", player),
    ]

    # Connect the regions logically
    menu.connect(podunk, "New Game", lambda state: True)
    podunk.connect(magicant, "Enter Magicant", lambda state: True)
    magicant.connect(podunk, "Exit Magicant", lambda state: True)
    podunk.connect(spookane, "Podunk to Spookane", lambda state: True)
    spookane.connect(rosemarys_house, "Enter Rosemary\'s House", lambda state: True)
    spookane.connect(yucca_desert, "Spookane to Yucca Desert", lambda state: True)
    yucca_desert.connect(duncans_factory, "Yucca Desert to Duncan's Factory", lambda state: True)
    duncans_factory.connect(mt_itoi, "Duncan's Factory to Mt. Itoi", lambda state: True)
    mt_itoi.connect(crystal_cavern, "Enter Crystal Cavern", lambda state: True)
    crystal_cavern.connect(giegue_ship, "Crystal Cavern to Giegue's Ship", lambda state: True)

    # Add all created regions to the multiworld
    multiworld.regions += [
        menu, magicant, duncans_factory, mt_itoi, crystal_cavern,
        yucca_desert, podunk, rosemarys_house, spookane, giegue_ship
    ]
