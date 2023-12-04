import time, sys, random
import pygame as p
from cow2 import *
import turkey
from game_parameters import *
from button import Button
from fenceopening import *

def draw_background(surf):
# load images
    fenceog = p.image.load("assets/fence.png")
    fence = p.transform.scale(fenceog, (FENCE_WIDTH, FENCE_HEIGHT))
    grass = p.image.load("assets/grass.png").convert()
# use the png transparency
    #fence.set_colorkey((0, 0, 0))

# fill the screen with grass
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            surf.blit(grass, (x, y))

# draw the fence along the bottom
    for x in range(0, SCREEN_WIDTH, FENCE_WIDTH):
        surf.blit(fence, (x, SCREEN_HEIGHT - FENCE_HEIGHT - 10))

# draw the title at the top center of the screen
    title_font = p.font.Font("assets/gamefont.ttf", 48)
    text = title_font.render("Turkey Time", True, (0, 0, 0))
    surf.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 10))

# Define the countdown function
# def countdown(time_in_sec, type_screen_here):
#     # Loop until the time is zero
#     while time_in_sec:
#         # Format the time as minutes and seconds
#         mins, secs = divmod(time_in_sec, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         # Print the time with a carriage return
#         #print(timeformat, end='\r')
#         time_font = p.font.Font("assets/gamefont.ttf", 24)
#         time = time_font.render(timeformat, True, (0, 0, 0))
#         type_screen_here.blit(time, (SCREEN_WIDTH - time.get_width(), 10))
#         # Wait for one second
#         time.sleep(1)
#         # Decrement the time by one second
#         time_in_sec -= 1
#     for event in p.event.get():
#         if event.type == p.QUIT:
#             p.quit()
#             sys.exit()


def add_cow(num_cows, y_pos, x_pos = random.randint(0, SCREEN_WIDTH)):
    for i in range(num_cows):
        cows.add(Cow(x_pos, y_pos))


class Hole(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = p.image.load('assets/hole.png')
        self.image = p.transform.scale(self.image, (HOLE_WIDTH, HOLE_HEIGHT))

        self.x = random.randint(HOLE_WIDTH, SCREEN_WIDTH - HOLE_WIDTH)
        self.y = random.randint(150, 450)

        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)

holes = p.sprite.Group()

def add_hole(num_holes):
    for i in range(num_holes):
        holes.add(Hole())

def add_fo(num_fo):
    for i in range(num_fo):
        fo_group.add(FenceOpening())


