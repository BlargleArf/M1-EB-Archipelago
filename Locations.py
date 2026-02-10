from BaseClasses import Location

# The base ID for all Mother 1 locations. This should be unique to this APWorld.
BASE_ID = 1989000

class M1Location(Location):
    """
    A Mother 1 location.
    """
    game: str = "Mother 1"


# The main table of all locations in the game where items can be found.
# The keys are the location names, and the values are their unique IDs.
location_table = {
    # Melody Locations
    "Canary Village - Canary's Chick":        BASE_ID + 0,
    "Magicant - Queen Mary":                  BASE_ID + 1,
    "Spookane - Ghost's Piano":               BASE_ID + 2,
    "Yucca Desert - Cactus":                  BASE_ID + 3,
    "Youngtown - Baby Dragon":                BASE_ID + 4,
    "Swamp - Underwater Palace Robot":        BASE_ID + 5,
    "Mt. Itoi - Robot's Grave":               BASE_ID + 6,
    "Mt. Itoi - Eve's Remains":               BASE_ID + 7,

    # Key Item Locations
    "Zoo - Superintendent":                   BASE_ID + 8,  # Zoo Key
    "Train Station - Conductor":              BASE_ID + 9,  # Pass
    "Duncan's Factory - Present":             BASE_ID + 10, # Ticket
    "Rosemary's House - West Room Chest":     BASE_ID + 11, # Ghost's Key
    "Twinkle Elementary School - Center Room Chest": BASE_ID + 12, # Franklin Badge
    
    # Example Chest Locations (more to be added)
    "Ninten's Basement - Chest":              BASE_ID + 13,
    "South of Podunk - Cave Chest":           BASE_ID + 14,

    # Early Game Checks
    "Ninten's House - Sister":                BASE_ID + 15,
    "Podunk - Mayor's House Present":         BASE_ID + 16,

    # Event Location for Victory
    "Giegue's Ship - Defeat Giegue":          None, # Event locations do not have an ID
}

# A mapping of location names to their unique Archipelago IDs.
location_name_to_id = {name: uid for name, uid in location_table.items() if uid is not None}
