import pygame

class Items:

    def __init__(self, x, y, image_type):
        self.x = x
        self.y = y
        self.image_type = image_type
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.house = pygame.image.load("images/house.png")

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
        self.image = pygame.transform.scale(self.image, scale_size)

    def check_image(self, image_type):
        if image_type == 1:
            self.rescale_image(self.image)