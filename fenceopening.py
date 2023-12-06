import pygame as p
import random
from game_parameters import *

class FenceOpening(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = p.image.load('assets/grass.png').convert()
        self.image = p.transform.scale(self.image, (FENCE_OPENING_WIDTH, FENCE_OPENING_HEIGHT))

        self.x = random.randint(FENCE_WIDTH, SCREEN_WIDTH-FENCE_WIDTH)
        self.y = FENCE_Y_POS + FENCE_HEIGHT/2

        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        #self.collision()
        self.rect.center = (self.x, self.y)

fo_group = p.sprite.Group()