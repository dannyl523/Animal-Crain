import pygame
from world import World

class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image_list = ["images/player_up.png", "images/player_down.png", "images/player_left.png", "images/player_right.png"]
        self.image = pygame.image.load(self.image_list[3])
        self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 2

    def rescale_image(self, image):
        self.image_size = self.image.get_size()
        scale_size = (self.image_size[0] * .7, self.image_size[1] * .7)
        self.image = pygame.transform.scale(self.image, scale_size)


    def move_player(self, direction):
        # move the player based on the direction!
        if direction == "up":
            self.image = pygame.image.load(self.image_list[0])
            self.rescale_image(self.image)
            self.y = self.y - self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

        if direction == "down":
            self.image = pygame.image.load(self.image_list[1])
            self.rescale_image(self.image)
            self.y = self.y + self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

        if direction == "left":
            self.image = pygame.image.load(self.image_list[2])
            self.rescale_image(self.image)
            self.x = self.x - self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

        if direction == "right":
            self.image = pygame.image.load(self.image_list[3])
            self.rescale_image(self.image)
            self.x = self.x + self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])



