from typing import TYPE_CHECKING
from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule, add_rule

if TYPE_CHECKING:
    from . import M1World

def set_rules(world: "M1World"):
    """
    Sets all the rules for the Mother 1 world.
    """
    player = world.player
    options = world.options

    # --- Completion Condition ---
    world.multiworld.completion_condition[player] = lambda state: \
        state.has("Victory", player) and \
        state.has_group("Melodies", player, options.RequiredMelodies.value)

    # --- Entrance Rules ---
    # These rules define the item requirements to move between regions.

    # Access to Rosemary's House requires the Ghost's Key.
    rosemary_entrance = world.multiworld.get_entrance("Enter Rosemary\'s House", player)
    set_rule(rosemary_entrance, lambda state: state.has("Ghost's Key", player))

    # Access to the Yucca Desert via the train requires the Pass.
    desert_entrance = world.multiworld.get_entrance("Spookane to Yucca Desert", player)
    set_rule(desert_entrance, lambda state: state.has("Pass", player))

    # Access to Mt. Itoi via the rocket requires the Rocket item.
    mt_itoi_entrance = world.multiworld.get_entrance("Duncan's Factory to Mt. Itoi", player)
    set_rule(mt_itoi_entrance, lambda state: state.has("Rocket", player))

    # Access to the Crystal Cavern can be protected by Franklin Badge logic.
    crystal_cavern_entrance = world.multiworld.get_entrance("Enter Crystal Cavern", player)
    if options.FranklinBadgeLogic.value:
        set_rule(crystal_cavern_entrance, lambda state: state.has("Franklin Badge", player))
    else:
        set_rule(crystal_cavern_entrance, lambda state: True)

    # --- Location Rules ---
    # Set rules for locations that have specific requirements beyond just reaching their region.

    # Access to the Zoo Superintendent requires the Zoo Key.
    set_rule(world.multiworld.get_location("Zoo - Superintendent", player), lambda state: state.has("Zoo Key", player))

    # The rest of these locations are accessible as long as their region is accessible.
    set_rule(world.multiworld.get_location("Ninten's Basement - Chest", player), lambda state: True)
    set_rule(world.multiworld.get_location("South of Podunk - Cave Chest", player), lambda state: True)
    set_rule(world.multiworld.get_location("Ninten's House - Sister", player), lambda state: True)
    set_rule(world.multiworld.get_location("Canary Village - Canary's Chick", player), lambda state: True)
    set_rule(world.multiworld.get_location("Podunk - Mayor's House Present", player), lambda state: True)
    set_rule(world.multiworld.get_location("Magicant - Queen Mary", player), lambda state: True)
    set_rule(world.multiworld.get_location("Rosemary's House - West Room Chest", player), lambda state: True)
    set_rule(world.multiworld.get_location("Spookane - Ghost's Piano", player), lambda state: True)
    set_rule(world.multiworld.get_location("Yucca Desert - Cactus", player), lambda state: True)
    set_rule(world.multiworld.get_location("Duncan's Factory - Present", player), lambda state: True)
    set_rule(world.multiworld.get_location("Swamp - Underwater Palace Robot", player), lambda state: True)
    set_rule(world.multiworld.get_location("Mt. Itoi - Robot's Grave", player), lambda state: True)
    set_rule(world.multiworld.get_location("Mt. Itoi - Eve's Remains", player), lambda state: True)
