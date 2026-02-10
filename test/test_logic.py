from test.bases import TestBase

class M1Test(TestBase):
    """
    Test class for the Mother 1 APWorld.
    """
    game = "Mother 1"

    def test_starting_locations(self):
        """Tests locations that should be accessible from the very start."""
        self.assertTrue(self.can_reach_location("Ninten's House - Sister"))
        self.assertTrue(self.can_reach_location("Ninten's Basement - Chest"))
        self.assertTrue(self.can_reach_location("Canary Village - Canary's Chick"))
        self.assertTrue(self.can_reach_location("Podunk - Mayor's House Present"))

    def test_zoo_access(self):
        """Tests that the Zoo Superintendent requires the Zoo Key."""
        self.assertFalse(self.can_reach_location("Zoo - Superintendent"))
        self.collect_by_name("Zoo Key")
        self.assertTrue(self.can_reach_location("Zoo - Superintendent"))

    def test_rosemary_access(self):
        """Tests that Rosemary's House requires the Ghost's Key."""
        self.assertFalse(self.can_reach_location("Rosemary's House - West Room Chest"))
        self.collect_by_name("Ghost's Key")
        self.assertTrue(self.can_reach_location("Rosemary's House - West Room Chest"))

    def test_full_progression_to_crystal_cavern(self):
        """Tests the entire chained item progression to reach the Crystal Cavern."""
        # Set Franklin Badge logic to True to test the full chain
        self.world_options["FranklinBadgeLogic"] = True

        # Can't reach the end of the line from the start
        self.assertFalse(self.can_reach_location("Mt. Itoi - Eve's Remains"))

        # Collect Ghost's Key to get into Rosemary's, which is logically on the way to the desert
        self.collect_by_name("Ghost's Key")
        self.assertFalse(self.can_reach_location("Mt. Itoi - Eve's Remains"))

        # Collect Pass to get to the desert
        self.collect_by_name("Pass")
        self.assertFalse(self.can_reach_location("Mt. Itoi - Eve's Remains"))

        # Collect Rocket to get from the factory to Mt. Itoi
        self.collect_by_name("Rocket")
        self.assertFalse(self.can_reach_location("Mt. Itoi - Eve's Remains"))

        # Collect Franklin Badge to get into the Crystal Cavern
        self.collect_by_name("Franklin Badge")
        self.assertTrue(self.can_reach_location("Mt. Itoi - Eve's Remains"))

    def test_crystal_cavern_no_badge_logic(self):
        """Tests that the Crystal Cavern can be reached without the badge if the option is off."""
        self.world_options["FranklinBadgeLogic"] = False
        # We still need the other items to get there
        self.collect_by_name(["Ghost's Key", "Pass", "Rocket"])
        self.assertTrue(self.can_reach_location("Mt. Itoi - Eve's Remains"))

    def test_game_completion_custom_melodies(self):
        """Tests that the RequiredMelodies option correctly adjusts the completion condition."""
        # To test completion, we must be able to reach Giegue's Ship, which requires full progression
        self.world_options["RequiredMelodies"] = 2
        self.collect_by_name(["Ghost's Key", "Pass", "Rocket"])

        # With not enough melodies, we can't win
        self.collect_by_name("First Melody")
        self.assertFalse(self.multiworld.can_reach(self.multiworld.get_location("Giegue's Ship - Defeat Giegue", self.player), self.player))

        # With enough melodies, we can win
        self.collect_by_name("Second Melody")
        self.assertTrue(self.multiworld.can_reach(self.multiworld.get_location("Giegue's Ship - Defeat Giegue", self.player), self.player))
