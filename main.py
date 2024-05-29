import pygame
from player import Player
from world import World
from tiles import Tiles
from world_items import Items

world_1 = World()
world_1_grid = world_1.create_world()


def check_tiles():
    if p.x <= 60:
        p.x = 70
        p.y = 900
    if p.y <= 95:
        p.x = 70
        p.y = 900
    if p.x >= 1050 and p.y <= 200:
        p.x = 70
        p.y = 900
    if p.x >= 150 and p.y >= 155 and p.y <= 295:
        p.x = 70
        p.y = 900
    if p.x >= 150 and p.x <= 1400 and p.y >= 345:
        p.x = 70
        p.y = 900
    if p.x >= 1500 and p.y >= 350:
        p.x = 70
        p.y = 900


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Pygame Introduction")
h = Items.()

# set up variables for the display
size = (1920, 1020)
screen = pygame.display.set_mode(size)
p = Player(70, 900)
mouse_pos = (0, 0)

# render the text for later
mouse_position = my_font.render(str(mouse_pos), False, (255, 255, 255))
player_position = my_font.render(str(p.x) + str(p.y), False, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        p.move_player("right")
        check_tiles()
    if keys[pygame.K_a]:
        p.move_player("left")
        check_tiles()
    if keys[pygame.K_w]:
        p.move_player("up")
        check_tiles()
    if keys[pygame.K_s]:
        p.move_player("down")
        check_tiles()


    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        mouse_pos = pygame.mouse.get_pos()
        mouse_position = my_font.render(str(mouse_pos), False, (255, 255, 255))
        player_position = my_font.render("(" + str(p.x) + ", " + str(p.y) + ")", False, (255, 255, 255))

    # SCREEN FILL
    screen.fill((255, 255, 255))
    # ------------------------------- #
    for row in world_1_grid:
        for tile in row:
            screen.blit(tile.image, tile.rect)
    screen.blit(p.image, p.rect)
    screen.blit(h, (1200, 150))
    screen.blit(mouse_position, (1000, 100))
    screen.blit(player_position, (1000, 900))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




