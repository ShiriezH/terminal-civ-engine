import random
from colorama import Style, init
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

    def simulate_turn(self):
        """Simulate one turn of the world."""
        for faction in self.factions:
            faction.collect_resources()
            self.expand_territory(faction)

    def expand_territory(self, faction):
        """Attempt to expand faction territory by claiming adjacent tiles."""
        for tile in list(faction.tiles):
            x, y = self.find_tile_position(tile)
            neighbors = self.get_neighbors(x, y)

            for neighbor in neighbors:
                if neighbor.symbol == "~":
                    continue

                if neighbor.owner is None:
                    faction.add_tile(neighbor)
                    return

                if neighbor.owner != faction:
                    self.resolve_combat(faction, neighbor.owner, neighbor)
                    return

    def resolve_combat(self, attacker, defender, tile):
        """Simple combat resolution between two factions."""
        attacker_power = len(attacker.tiles) + random.randint(0, 3)
        defender_power = len(defender.tiles) + random.randint(0, 3)

        if attacker_power > defender_power:
            defender.tiles.remove(tile)
            attacker.add_tile(tile)

    def find_tile_position(self, target_tile):
        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == target_tile:
                    return i, j
        return None, None

    def get_neighbors(self, x, y):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.height and 0 <= ny < self.width:
                neighbors.append(self.grid[nx][ny])

        return neighbors

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

    def check_victory(self):
        """Check if one faction controls all non-water tiles."""
        total_land_tiles = sum(
            1
            for row in self.grid
            for tile in row
            if tile.symbol != "~"
        )

        for faction in self.factions:
            if len(faction.tiles) == total_land_tiles:
                return faction

        return None

    def print_statistics(self):
        print("\n--- Faction Statistics ---")
        for faction in self.factions:
            print(
                f"{faction.name} ({faction.symbol}) | "
                f"Tiles: {len(faction.tiles)} | "
                f"Resources: {faction.resources}"
            )