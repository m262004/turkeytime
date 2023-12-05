import pygame as p
import random
from game_parameters import *

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

    def draw(self, screen):
        screen.blit(self.image, self.rect)


cows = p.sprite.Group()
