import random
from colorama import Fore, Style, init
from world.tile import Tile
from entities.faction import Faction

# Initialize colorama
init(autoreset=True)


class Map:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.grid = []
        self.factions = []

        self.generate_map()
        self.spawn_factions()

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
            [Tile(random.choice(terrain_list)) for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def spawn_factions(self):
        """Create and place initial factions on the map."""
        faction_a = Faction("Red Kingdom", "R")
        faction_b = Faction("Blue Empire", "B")

        self.factions = [faction_a, faction_b]

        for faction in self.factions:
            while True:
                x = random.randint(0, self.height - 1)
                y = random.randint(0, self.width - 1)
                tile = self.grid[x][y]

                if tile.owner is None and tile.symbol != "~":
                    faction.add_tile(tile)
                    break

    def display(self):
        for row in self.grid:
            row_display = []
            for tile in row:
                if tile.owner:
                    row_display.append(tile.owner.symbol)
                else:
                    row_display.append(
                        tile.get_color() + tile.symbol + Style.RESET_ALL
                    )
            print(" ".join(row_display))