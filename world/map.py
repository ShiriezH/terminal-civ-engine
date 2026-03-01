import random
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


class Map:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = []
        self.generate_map()

    def generate_map(self):
        """Generate terrain using weighted probabilities."""
        terrain_types = {
            "~": 0.1,   # Water
            ".": 0.5,   # Plains
            "F": 0.3,   # Forest
            "^": 0.1    # Mountain
        }

        terrain_list = []
        for symbol, weight in terrain_types.items():
            terrain_list.extend([symbol] * int(weight * 100))

        self.grid = [
            [random.choice(terrain_list) for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def display(self):
        color_map = {
            "~": Fore.BLUE,
            ".": Fore.GREEN,
            "F": Fore.LIGHTGREEN_EX,
            "^": Fore.WHITE
        }

        for row in self.grid:
            colored_row = [
                color_map.get(tile, Fore.RESET) + tile + Style.RESET_ALL
                for tile in row
            ]
            print(" ".join(colored_row))