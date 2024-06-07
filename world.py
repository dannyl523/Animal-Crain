import pygame
from tiles import Tiles

class World:

    def __init__(self):
        self.generated_world = self.create_world_1
        self.generated_world = self.create_world_2


    def create_world_1(self):
        f1 = open("world1", "r")
        grid_world1 = []
        column_world1 = 0
        y_world1 = 0
        for line in f1:
            row_world1 = []
            rowing_world1 = 0
            x_world1 = 10
            for character in line:
                if character == "#":
                    t = Tiles(x_world1, y_world1, rowing_world1, column_world1, 0)
                    rowing_world1 = rowing_world1 + 1
                    x_world1 = x_world1 + 30
                    row_world1.append(t)
                if character == ".":
                    t = Tiles(x_world1, y_world1, rowing_world1, column_world1, 2)
                    rowing_world1 = rowing_world1 + 1
                    x_world1 = x_world1 + 30
                    row_world1.append(t)
            column_world1 = column_world1 + 1
            y_world1 = y_world1 + 24
            grid_world1.append(row_world1)
        return grid_world1

    def create_world_2(self):
        f2 = open("world2_The_Hut", "r")
        grid_world2 = []
        column_world2 = 0
        y_world2 = 0
        for line in f2:
            row_world2 = []
            rowing_world2 = 0
            x_world2 = 10
            for character in line:
                if character == "#":
                    t = Tiles(x_world2, y_world2, rowing_world2, column_world2, 4)
                    rowing_world2 = rowing_world2 + 1
                    x_world2 = x_world2 + 30
                    row_world2.append(t)
                if character == ".":
                    t = Tiles(x_world2, y_world2, rowing_world2, column_world2, 1)
                    rowing_world2 = rowing_world2 + 1
                    x_world2 = x_world2 + 24
                    row_world2.append(t)
            column_world2 = column_world2 + 1
            y_world2 = y_world2 + 24
            grid_world2.append(row_world2)
        return grid_world2



