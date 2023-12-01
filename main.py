import random
import pygame as p
from game_parameters import *
import sys
from turkey import *
from utilities import *
from cow2 import *

p.init()
#create screen
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("Turkey Time")
clock = p.time.Clock()

#create turkey sprite group
#turkey = Turkey()
turkey_group = p.sprite.Group()
turkey_group.add(Turkey())

# #create cow groups
# cows = Cow()
# cow_group = p.sprite.Group()
# cow_group.add(cows)

#
fo_group = p.sprite.Group()
fo_group.add(FenceOpening())

#main loop
run = True
background = screen.copy()
draw_background(background)
add_cow(1,200)

while run:
    #set frame rate
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    # draw the background
    screen.blit(background, (0, 0))

    # #check for turkey-cow collision and fence opening collision
    # cow_collision = p.sprite.spritecollide(turkey, cows, True)
    # fo_collision = p.sprite.spritecollide(turkey, fo, True)
    # if cow_collision:
    #     turkey.x = TURKEY_START_X
    #     turkey.y = TURKEY_START_Y
    # if fo_collision:
    #    cows.empty()
    #    if SCORE == 2:
    #    add_cows()
    #go to next level
    #    if SCORE == 3:
    #    add_cows()
    #go to next level
    #    if SCORE == 4:
    #     turkey_group.empty()
    #     cow_group.empty()
    #     screen.blit(winscreen, (0,0))
    #     #go to next level

        # title_font = p.font.Font("assets/gamefont.ttf", 48)
        # wintext = title_font.render("You Win", True, (0, 0, 0))
        # surf.blit(wintext, (SCREEN_WIDTH / 2 - wintext.get_width() / 2, 0))



    #leveldisplay()
    #check____


    #cow_group.draw(screen)
    turkey_group.draw(screen)
    #fo_group.draw(screen)

    #cow_group.update()
    turkey_group.update()
    #fo_group.update()


    p.display.update()

