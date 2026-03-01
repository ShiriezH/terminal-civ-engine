from colorama import Fore


class Tile:
    TERRAIN_COLORS = {
        "~": Fore.BLUE,
        ".": Fore.GREEN,
        "F": Fore.LIGHTGREEN_EX,
        "^": Fore.WHITE
    }

    def __init__(self, terrain_symbol):
        self.symbol = terrain_symbol
        self.owner = None  # For future faction ownership
        self.resource_value = self.set_resource_value()

    def set_resource_value(self):
        """Assign resource value based on terrain type."""
        values = {
            "~": 0,   # Water
            ".": 2,   # Plains
            "F": 3,   # Forest
            "^": 1    # Mountain
        }
        return values.get(self.symbol, 0)

    def get_color(self):
        return self.TERRAIN_COLORS.get(self.symbol)