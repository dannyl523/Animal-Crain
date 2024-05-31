import pygame

class Items:

    def __init__(self, x, y, image_type):
        self.x = x
        self.y = y
        self.image_type = image_type
        self.image_list = ["images/house.png", " "]
        self.image = pygame.image.load(self.image_list[image_type])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])


    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .2, self.image_size[1] * .2)
        self.image = pygame.transform.scale(self.image, scale_size)
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def check_image(self, image_type):
        if image_type == 0:
            self.image = pygame.image.load(self.image_list[0])
            self.rescale_image(self.image)
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

