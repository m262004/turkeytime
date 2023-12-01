import pygame as p
import random
from game_parameters import *
from cow2 import *

class Cow(p.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = p.image.load("assets/cow.png").convert()
        self.image = p.transform.scale(self.image, (COW_WIDTH, COW_HEIGHT))
        self.image = p.transform.flip(self.image, True, False)

        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y

        self.rect.center = (x, y)

        self.speed = random.uniform(COW_SPEED_MIN, COW_SPEED_MAX)

    def update(self):
        self.x += self.speed
        self.rect.x = self.x

        # if self.rect.x > SCREEN_WIDTH:
        #     self.rect.x = -self.rect.width

    def draw(self, screen):
        screen.blit(self.image, self.rect)


cows = p.sprite.Group()



        #sprite = Cow(-i * 100, y_pos, self.image)
        #cows.add(sprite)

        #