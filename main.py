import pygame
import random
from player import Player
from world import World

world_1 = World()
world_1_grid = world_1.create_world()

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
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        p.move_player("right")
    if keys[pygame.K_a]:
        p.move_player("left")
    if keys[pygame.K_w]:
        p.move_player("up")
    if keys[pygame.K_s]:
        p.move_player("down")

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False



    # SCREEN FILL
    screen.fill((255, 255, 255))
    # ------------------------------- #
    for row in world_1_grid:
        for tile in row:
            screen.blit(tile.image, tile.rect)
    screen.blit(p.image, p.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




