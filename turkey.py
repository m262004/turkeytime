import pygame as p
from game_parameters import *

class Turkey(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # where turkey starts
        self.x = TURKEY_START_X
        self.y = TURKEY_START_Y
        self.speed = TURKEY_SPEED
        self.width = TURKEY_WIDTH
        self.height = TURKEY_HEIGHT
        self.turkey = p.image.load('assets/turkey.png').convert()
        # resize
        self.image = p.transform.scale(self.turkey, (self.width, self.height))
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
        elif key[p.K_RIGHT]:
            self.x += self.speed
        elif key[p.K_UP]:
            self.y -= self.speed
        elif key[p.K_DOWN]:
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

    def draw(self, screen):
        screen.blit(self.image, self.rect)

#turkey_group = p.sprite.Group()

