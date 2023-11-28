import time
import pygame as p
import random
from game_parameters import *
def draw_background(surf):
# load images
    fenceog = p.image.load("assets/fence.png")
    fence = p.transform.scale(fenceog, (FENCE_OPENING_WIDTH, FENCE_OPENING_HEIGHT))
    grass = p.image.load("assets/grass.png").convert()
# use the png transparency
    #fence.set_colorkey((0, 0, 0))
# fill the screen with grass
    for x in range(0, SCREEN_WIDTH, TILE_SIZE):
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            surf.blit(grass, (x, y))
# draw the fence along the bottom
    for x in range(0, SCREEN_WIDTH, FENCE_WIDTH):
        surf.blit(fence, (x, SCREEN_HEIGHT - FENCE_HEIGHT*2.2))
#     # draw the title at the top center of the screen
    #title_font = p.font.Font("assets/gamefont.ttf", 48)
    #text = title_font.render("Turkey Time", True, (0, 0, 0))
    #surf.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 0))

# def add_cow(num_cows):
#     for _ in range(num_cows):
#         cows.add(Cow(cow_y    (random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2), random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))



# class Screen(p.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.img1 = p.image.load('../turkeytime/assets/grass.png')
#         #win screen
#         self.img2 = p.image.load(win.png)
#         self.img2 = p.transform.scale(self.img2, (SCREEN_WIDTH,SCREEN_HEIGHT))
#         #lose screen
#         self.img3 = p.image.load(lose.png)
#         self.img3 = p.transform.scale(self.img3, (SCREEN_WIDTH, SCREEN_HEIGHT))
#
#         self.image = self.img1
#         #topL corner of image
#         self.x = 0
#         self.y = 0
#
#         self.rect = self.image.get_rect()
#
#     def update(self):
#         #puts topL corner of image in topL corner of screen
#         self.rect.topleft = (self.x, self.y)

class FenceOpening(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = p.image.load('assets/grass.png')
        self.image = p.transform.scale(self.image, (FENCE_OPENING_WIDTH*0.75, FENCE_OPENING_HEIGHT/2))

        self.x = random.randint(FENCE_WIDTH, SCREEN_WIDTH-FENCE_WIDTH)
        self.y = FENCE_Y_POS

        self.rect = self.image.get_rect()

    def update(self):
        self.collision()
        self.rect.center = (self.x, self.y)

    def collision(self):
        global SCORE, cow
        fo_hit = p.sprite.spritecollide(self, cow_group, False)
        if fo_hit:
            if SCORE < 5:
                switchlevel()
            turkey.x = TURKEY_START_X
            turkey.y = TURKEY_START_Y


LEVEL = 0
#level_font = p.font.Font("assets/gamefont.ttf", 80)

#def leveldisplay():
    #level_text = level_font.render(str(LEVEL) + ' /5', True, (0, 0, 0))
    #screen.blit(level_text, (255, 10))

    # def switchlevel():
    #     global SCORE
    #
    #     if cow1.speed < 0:
    #         cow1.speed -= 1
    #     else:
    #         cow1.speed += 1
    #     if cow2.speed < 0:
    #         cow2.speed -= 1
    #     else:
    #         cow2.speed += 1
    #
    #     SCORE += 1


