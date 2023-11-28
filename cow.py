import pygame as p
import random
from game_parameters import *

class Cow(p.sprite.Sprite):
    def __init__(self, y_pos): #, num_cows):
        super().__init__()
        self.y = y_pos
        self.image = p.image.load("assets/cow.png").convert()
        self.speed = random.randint(COW_SPEED_MIN, COW_SPEED_MAX)
        #start at middle of screen so you can't just straight shot
        self.x = random.randint(0, SCREEN_WIDTH)
        #resize
        self.width = 354
        self.height = 200
        self.image = p.transform.scale(self.image, (self.width, self.height))

        #self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        self.rect.center = (x, y)

        self.speed = random.uniform(COW_SPEED_MIN, COW_SPEED_MAX)

        #self.num_cows = num_cows

    def update(self):
        self.x += self.speed
        #self.move()
        self.rect.y = self.y

    # def move(self):
    #     self.x += self.speed

        #bounce off walls
        if self.y - self.height/2 < 0:
            self.y = self.height/2
            self.speed *= -1
        elif self.y + self.height/2 > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height / 2
            self.speed *= -1

    def draw(self, screen):
        screen.blit(self.image, self.rect)


cows = p.sprite.Group()
