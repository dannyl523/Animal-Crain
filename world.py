import pygame
from tiles import Tiles

class World:

    def __init__(self):
        self.generated_world = self.create_world


    def create_world(self):
        f = open("world1", "r")
        grid = []
        column = 0
        y = 0
        for line in f:
            row = []
            rowing = 0
            x = 10
            for character in line:
                if character == "#":
                    t = Tiles(x, y, rowing, column, 0)
                    rowing = rowing + 1
                    x = x + 30
                    row.append(t)
                if character == ".":
                    t = Tiles(x, y, rowing, column, 2)
                    rowing = rowing + 1
                    x = x + 30
                    row.append(t)
            column = column + 1
            y = y + 24
            grid.append(row)
        return grid



