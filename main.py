import pygame as p
from game_parameters import *
from turkey import *

p.init()

win=p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = p.time.Clock()

#create turkey sprite group
turkey = Turkey()
turkey_group = p.sprite.Group()
turkey_group.add(turkey)

#main loop
run = True
while run:
    #fix frame rate so turkey not speedy
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    turkey_group.draw(win)
    turkey_group.update()

    p.display.update()

