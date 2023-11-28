import pygame as p
from game_parameters import *
from turkey import *
from utilities import *
from cow import *

p.init()
#create screen
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("Turkey Time")
clock = p.time.Clock()

#create turkey sprite group
turkey = Turkey()
turkey_group = p.sprite.Group()
turkey_group.add(turkey)

#create cow groups
#cow1 = Cow(SCREEN_HEIGHT/2)
#cow2 = Cow(400,1)
#cow_group = p.sprite.Group()
#cow_group.add(cow1)

# fo = FenceOpening()
# fo_group = p.sprite.Group()
# fo_group.add(fo)


# # place cows off the left side of the screen in random positions
# for _ in range(5):
#     fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2), random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))



add_cow(5)
for _ in range(5):
    cows.add(Cow(random.randint(0, SCREEN_WIDTH/2), cow.y_pos)


#main loop
run = True
background = screen.copy()
draw_background(background)

while run:
    #fix frame rate so turkey not speedy
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    # draw the background
    screen.blit(background, (0, 0))

    #leveldisplay()
    #check____

    turkey_group.draw(screen)
    #cow_group.draw(screen)
    #fo_group.draw(screen)

    turkey_group.update()
    #cow_group.update()
    #fo_group.update()


    p.display.update()

