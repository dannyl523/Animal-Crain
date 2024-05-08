import pygame

class World:

    def __init__(self, x, y, updown_row, leftright_row):
        self.x = x
        self.y = y
        self.updown_row = updown_row
        self.leftright_row = leftright_row
        self.image_list = ["images/tile_grass.png", "images/tile_magma.png", "images/tile_pavement.png", "images/tile_water.png"]


