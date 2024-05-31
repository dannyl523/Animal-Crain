import pygame

class Tiles:

    def __init__(self, x, y, row, column, tile_type):
        self.x = x
        self.y = y
        self.column = column
        self.row = row
        self.tile_type = tile_type
        self.image_list = ["images/tile_grass.png", "images/tile_home_stone.png", "images/tile_pavement.png", "images/tile_water.png", "images/tile_black.png"]
        if tile_type == 0:
            self.image = pygame.image.load(self.image_list[0])
        elif tile_type == 1:
            self.image = pygame.image.load(self.image_list[1])
        elif tile_type == 2:
            self.image = pygame.image.load(self.image_list[2])
        elif tile_type == 3:
            self.image = pygame.image.load(self.image_list[3])
        elif tile_type == 4:
            self.image = pygame.image.load(self.image_list[4])
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.image_size = self.image.get_size()
        self.rescale_image(self.image)

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * 0.6, self.image_size[1] * 0.6)
        self.image = pygame.transform.scale(self.image, scale_size)

