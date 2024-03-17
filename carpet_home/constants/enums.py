import enum
from carpet_home.constants.base_enum_class import BaseEnumClass


class ColorEnum(BaseEnumClass, enum.Enum):
    red = "RED"
    black = "BLACK"


class MaterialEnum(BaseEnumClass, enum.Enum):
    wool = "WOOL"
    wool_and_bamboo_silk = "WOOL_AND_BAMBOO_SILK"
    wool_and_silk = "WOOL_AND_SILK"
    silk = "SILK"
    viscose = "VISCOSE"
    jute_and_hemp = "JUTE_AND_HEMP"
    cotton = "COTTON"
    others = "OTHERS"


class ShapeEnum(BaseEnumClass, enum.Enum):
    rectangle = "RECTANGLE"
    irregular = "IRREGULAR"
    round = "ROUND"
    runner = "RUNNER"
    oval = "OVAL"
    square = "SQUARE"


class RoomEnum(BaseEnumClass, enum.Enum):
    living = "LIVING"
    dining = "DINING"
    bedroom = "BEDROOM"
    kids_room = "KIDS_ROOM"


class WavingTechniqueEnum(BaseEnumClass, enum.Enum):
    hand_knotted = "HAND_KNOTTED"
    hand_tufted = "HAND_TUFTED"
    hand_loom = "HAND_LOOM"
    flat_waves = "FLAT_WAVES"
    shag = "SHAG"

