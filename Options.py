from Options import Toggle, Range, PerGameCommonOptions
import dataclasses

class FranklinBadgeLogic(Toggle):
    """If enabled, the Franklin Badge will be logically required to traverse certain areas
    (like Mt. Itoi) and to face the final boss without being defeated by lightning.
    """
    display_name = "Franklin Badge Logic"
    default = True

class RequiredMelodies(Range):
    """The number of melodies required to be able to challenge the final boss."""
    display_name = "Required Melodies"
    range_start = 1
    range_end = 8
    default = 8

@dataclasses.dataclass
class M1Options(PerGameCommonOptions):
    """The options for a Mother 1 game."""
    FranklinBadgeLogic: FranklinBadgeLogic
    RequiredMelodies: RequiredMelodies
