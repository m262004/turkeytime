import pygame as p
from game_parameters import *

class Turkey(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # where turkey starts
        self.x = TURKEY_START_X
        self.y = TURKEY_START_Y
        self.speed = 4
        self.width = TURKEY_WIDTH
        self.height = TURKEY_HEIGHT
        self.turkey = p.image.load('assets/turkey.png')
        self.image = self.turkey
        self.rect = self.image.get_rect()
        #resize
        # self.turkey = p.transform.scale(self.turkey, (self.width, self.height))

        self.image = self.turkey
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self):
        self.move()
        self.correction()
        self.rect.center = (self.x, self.y)

    def move(self):
        key = p.key.get_pressed()
        if key[p.K_LEFT]:
            self.x -= self.speed
        if key[p.K_RIGHT]:
            self.x += self.speed
        if key[p.K_UP]:
            self.y -= self.speed
        if key[p.K_DOWN]:
            self.y += self.speed

    #makes sure turkey doesn't go off screen
    def correction(self):
        if self.x - self.width/2 < 0:
            self.x = self.width/2
        if self.x + self.width/2 > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width/2
        if self.y - self.height/2 < 0:
            self.y = self.height/2
        if self.y + self.height/2 > FENCE_Y_POS:
            self.y = FENCE_Y_POS - self.height/2

#turkey = p.sprite.Group()

