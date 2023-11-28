import pygame as p
from game_parameters import *

class Turkey(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #where turkey starts
        self.x = 50
        self.y = SCREEN_HEIGHT/2
        self.speed = 4
        self.width = 100
        self.height = 50
        self.turkey = p.image.load('..assets/turkey.png')
        #resize? self.turkey = p.transform.scale(self.turkey, (self.width, self.height))

        self.image = self.turkey
        self.rect = self.image.get_rect()

    def update(self):
        self.move()
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
