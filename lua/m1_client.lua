-- Mother 1 Archipelago Client
-- This is the main script that runs in BizHawk to connect the game to the Archipelago server.

-- #################################################################################
-- ## 1. LIBRARY AND DATA IMPORTS
-- #################################################################################

-- Import the connector library provided by Archipelago.
-- This assumes you have copied the 'lib' folder into your 'src' directory.
if not ArchipelagoConnector then
    require("lib.ArchipelagoConnector")
end

-- Import the item and location data we auto-generate with our Python script.
-- This gives us access to the ID-to-name tables.
require("lua.client_data")

-- #################################################################################
-- ## 2. SCRIPT CONFIGURATION AND SERVER CONNECTION
-- #################################################################################

-- Create the main connector object. This is our gateway to the server.
AP = ArchipelagoConnector.new()

-- TODO: These values should be prompted from the user when the script starts.
-- For now, you can hardcode them for testing.
local server_address = "archipelago.gg:12345"
local slot_name = "Ninten"
local password = ""

-- #################################################################################
-- ## 3. MEMORY RESEARCH DATA (TO BE FILLED IN)
-- #################################################################################

-- This table is where you will map your AP Location IDs to the memory addresses you find.
-- This is the most important part of the client development process.
-- Format: [LocationID] = { addr=MemoryAddress, mask=Bitmask }
local LOCATION_MAP = {
    -- Example from our previous discussion:
    -- [1989015] = { addr=0x07E0, mask=0x08 }, -- Ninten's House - Sister

    -- TODO: Add all other location addresses and bitmasks here as you find them.
}

-- TODO: Find the starting memory address of Ninten's inventory block.
local INVENTORY_START_ADDR = 0x0200 -- Example address; needs to be found!

-- #################################################################################
-- ## 4. CLIENT LOGIC AND HELPER FUNCTIONS
-- #################################################################################

local checked_locations = {}

-- This function is called every frame to check for new location checks.
function check_game_locations()
    for id, data in pairs(LOCATION_MAP) do
        if not checked_locations[id] then
            local memory_value = memory.readbyte(data.addr)
            if (memory_value & data.mask) == data.mask then
                console.log("New location checked: " .. (AP_M1_ID_to_Location_Name[id] or id))
                AP:LocationChecks({id})
                checked_locations[id] = true
            end
        end
    end
end

-- This function is called automatically when the server sends us items.
function on_items_received(packet)
    for _, item in ipairs(packet.items) do
        local item_name = AP_M1_ID_to_Item_Name[item.item] or ("Unknown Item: " .. item.item)
        console.log("Received item: " .. item_name)
        emu.message("Received: " .. item_name)

        -- TODO: Implement the logic to find an empty inventory slot
        -- and write the new item's in-game ID to it.
    end
end

-- This function is called when the server confirms our connection.
function on_connected(packet)
    console.log("Connected to server!")
    -- Sync the locations we have already checked with the server.
    for id, data in pairs(packet.checked_locations) do
        checked_locations[id] = true
    end
end

-- #################################################################################
-- ## 5. MAIN SCRIPT LOOP
-- #################################################################################

-- Register our handler functions with the connector.
AP:register_handler("ReceivedItems", on_items_received)
AP:register_handler("Connected", on_connected)

-- Attempt to connect to the server.
console.log("Attempting to connect to " .. server_address .. " as " .. slot_name .. "...")
AP:connect(server_address, slot_name, password)

-- This is the main loop that runs continuously while the script is active.
while true do
    -- Update the server connection (sends/receives messages).
    AP:update()

    -- If we are successfully connected, run our game logic.
    if AP.get_status() == AP.CONNECTION_STATUS.CONNECTED then
        check_game_locations()
    end

    -- Advance the emulator by one frame.
    emu.frameadvance()
end
