import random
import pygame as p
from game_parameters import *
import sys
from turkey import *
from utilities import *
from cow2 import *

p.init()
p.mixer.init()

#create screen
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("Turkey Time")
clock = p.time.Clock()

#create turkey sprite group
turkey = p.sprite.Group()
turkey.add(Turkey())

# create fence opening sprite group
fo_group = p.sprite.Group()
fo_group.add(FenceOpening())

# initialize misc items
level = 1
bkgd_music = p.mixer.Sound("assets/backgroundmusic.wav")
moo = p.mixer.Sound("assets/moo.wav")
heart = p.image.load("assets/heart.png").convert()
heart = p.transform.scale(heart, (HEART_SIZE,HEART_SIZE))

#life_icon.set_colorkey((0, 0, 0))
#clock = p.time.Clock()
lives = NUM_LIVES

#main loop
run = True
background = screen.copy()
draw_background(background)
add_cow(1,200)

#while lives > 0:
while run:
    #set frame rate
    clock.tick(60)

    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    # play background music
    bkgd_music.play(loops=-1)

    # draw the background
    screen.blit(background, (0, 0))

    #update game objects
    cows.update()
    turkey.update()
    fo_group.update()

    #check for turkey-cow collision and fence opening collision
    cow_collision = p.sprite.spritecollide(turkey, cows, False)
    fo_collision = p.sprite.spritecollide(turkey, fo_group, False)
    if cow_collision:
        turkey.x = TURKEY_START_X
        turkey.y = TURKEY_START_Y
        lives -= len(cow_collision)
        p.mixer.Sound.play(moo)
    if fo_collision:
        level += 1
        cows.empty()
        if level == 2:
            add_cow()
        if level == 3:
            add_cow()
        if level == 4:
            add_cow()
        #end screen
        if level > 4:
            winfont = p.font.Font("assets/gamefont.ttf", 48)
            text = winfont.render("You Win!", True, (255, 0, 0))
            screen.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, 100))
            #play again button


    # if cow goes off screen
    for cow in cows:
        if cow.rect.x > SCREEN_WIDTH:
            cows.remove(cow)
            add_cow(1, cow.y, 0)


    cows.draw(screen)
    turkey.draw(screen)
    fo_group.draw(screen)

    cows.update()
    turkey.update()
    fo_group.update()

    # draw the lives in the upper left corner
    for i in range(lives):
        screen.blit(heart, (i * HEART_SIZE, SCREEN_HEIGHT - HEART_SIZE))

    p.display.update()

