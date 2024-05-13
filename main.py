import pygame
import random
from player import Player
from world_1 import World

world_list = [ [1, 1, 1, 1, 2, 2, 2, 1, 1, 1],
          ]


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
# WORLD
    left_right_row = 0
    y = 10
    for i in range(10):
        tiles = []
        updown_row = 0
        x = 10
        for j in range(5):
            t = World(x, y, updown_row, left_right_row, world_list[updown_row])
            left_right_row += 1
            x = x + 24
            tiles.append(t)
        updown_row += 1
        y = y + 24

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    # SCREEN FILL
    screen.fill((255, 255, 255))
    # ------------------------------- #
    screen.blit(t.image, t.rect)
    screen.blit(p.image, p.rect)
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




