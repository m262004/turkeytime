import time
import pygame
import random
from fish import fishes, Fish
from game_parameters import *
def draw_background(surf):
# Load tiles from the assets folder into surfaces
    hole = pygame.image.load("../assets/hole.png").convert()
    fence = pygame.image.load("../assets/fence.png").convert()
    grass = pygame.image.load("../assets/grass.png").convert()
# use the png transparency
    hole.set_colorkey((0, 0, 0))
    fence.set_colorkey((0, 0, 0))
# fill the screen with grass
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            surf.blit(grass, (x, y))
# draw the fence along the bottom left
    for x in range(0, SCREEN_WIDTH/2, FENCE_SIZE):
        surf.blit(fence, (x, SCREEN_HEIGHT - FENCE_SIZE))
# draw the fence along the bottom right
    for x in range(SCREEN_WIDTH/2, SCREEN_WIDTH, FENCE_SIZE):
        surf.blit(fence, (x, SCREEN_HEIGHT - FENCE_SIZE))
#     # draw the title at the top center of the screen
#     custom_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", 48)
#     text = custom_font.render("Chomp", True, (255, 69, 0))
#     surf.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))

# def add_cow(num_cows):
#     for _ in range(num_cows):
#         cows.add(Cow(cow_y    (random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2), random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))


