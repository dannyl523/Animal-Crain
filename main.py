import pygame
import random
import world_1
import tiles
from player import Player

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Pygame Introduction")

# set up variables for the display
size = (1920, 1020)
screen = pygame.display.set_mode(size)

p = Player(200, 200)


# render the text for later


# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.blit(p.image, p.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




