# Mother 1 Setup Guide

## Required Software

*   A legally obtained US ROM of **EarthBound Beginnings** for the Nintendo Entertainment System (NES).
*   The **[BizHawk Emulator](https://tasvideos.org/BizHawk/ReleaseHistory)** (version 2.8 or newer is recommended).
*   The Archipelago package, which includes the necessary client libraries. You can find the latest release [here](https://github.com/ArchipelagoMW/Archipelago/releases).

## Connecting to the MultiServer

1.  **Launch BizHawk** and load your EarthBound Beginnings ROM.
2.  Open the Lua Console by navigating to `Tools > Lua Console`.
3.  In the Lua Console window, click `Script > Open Script`.
4.  Navigate to your Archipelago installation directory, and find the Mother 1 client script located at `AP/worlds/m1/m1_client.lua` (or similar path).
5.  The script will prompt you in the console for your server address, slot name, and password. Enter these details.
6.  Once connected, you can start playing! The script will run in the background, automatically sending and receiving items.
