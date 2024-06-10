import pygame
from player import Player
from world import World
from tiles import Tiles
from world_items import Items

world_1 = World()
world_1_grid = world_1.create_world_1()
world_2 = World()
world_2_grid = world_2.create_world_2()

def check_tiles_w1():
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
def check_tiles_w2():
    if p.y <= 200:
        p.x = 400
        p.y = 490
    if p.x >= 1530:
        p.x = 400
        p.y = 490
    if p.y >= 735:
        p.x = 400
        p.y = 490
    if p.x < 390 and (p.y > 510 or p.y < 400):
        p.x = 400
        p.y = 490



# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Pygame Introduction")


# set up variables for the display
size = (1920, 1020)
screen = pygame.display.set_mode(size)
p = Player(70, 900)
h = Items(1200, 500, 0)
h.check_image(h.image_type)
on_hut = False
world_1_phase = True
w2_start = False
condition = False

# render the text for later
player_position = my_font.render(str(p.x) + str(p.y), False, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True


# -------- Main Program Loop -----------
while run:
    # --- Main event loop
    if p.x >= 1040 and p.y <= 200:
        on_hut = True
        world_1_phase = False
        p.x = 400
        p.y = 490
        p.delta = 5
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_d]:
        p.move_player("right")
    if keys[pygame.K_a]:
        p.move_player("left")
    if keys[pygame.K_w]:
        p.move_player("up")
    if keys[pygame.K_s]:
        p.move_player("down")
    if world_1_phase == True:
        check_tiles_w1()
    if on_hut == True:
        check_tiles_w2()
        if condition == True and (p.x < 380 and (p.y > 400 or p.y < 530)):
            p.x = 970
            p.y = 150
            p.delta = 2
            on_hut = False
            world_1_phase = True
            w2_start = False

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            run = False
        player_position = my_font.render("(" + str(p.x) + ", " + str(p.y) + ")", False, (255, 255, 255))

    # SCREEN FILL
    screen.fill((255, 255, 255))
    # ------------------------------- #
    if world_1_phase == True:
        condition = False
        for row in world_1_grid:
            for tile in row:
                screen.blit(tile.image, tile.rect)
        screen.blit(h.image, (1000, -10))
    if on_hut == True:
        condition = True
        for row in world_2_grid:
            for tile in row:
                screen.blit(tile.image, tile.rect)


    screen.blit(p.image, p.rect)
    screen.blit(player_position, (1000, 900))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()




