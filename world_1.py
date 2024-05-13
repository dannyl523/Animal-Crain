import pygame

class World:

    def __init__(self, x, y, updown_row, left_right_row, tile_type):
        self.x = x
        self.y = y
        self.updown_row = updown_row
        self.left_right_row = left_right_row
        self.tile_type = tile_type
        self.image_list = ["images/tile_grass.png", "images/tile_magma.png", "images/tile_pavement.png", "images/tile_water.png"]
        self.image = pygame.image.load(self.image_list[0])
        self.image_size = self.image.get_size()
        self.rescale_image(self.image)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .6, self.image_size[1] * .6)
        self.image = pygame.transform.scale(self.image, scale_size)


    def tiles(self, tile_type):
        if self.tile_type == 1:
            self.image = pygame.image.load(self.image_list[0])
            self.rescale_image(self.image)
        elif self.tile_type == 2:
            self.image = pygame.image.load(self.image_list[1])
            self.rescale_image(self.image)