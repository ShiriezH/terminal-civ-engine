import random


class Faction:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.resources = 0
        self.tiles = []

    def add_tile(self, tile):
        tile.owner = self
        self.tiles.append(tile)

    def collect_resources(self):
        self.resources += sum(tile.resource_value for tile in self.tiles)