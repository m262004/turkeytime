import random, sys, time
import pygame as p
from game_parameters import *
from turkey import *
from utilities import *
from cow2 import *
from button import Button

p.init()
p.mixer.init()

#create screen
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("Turkey Time")
clock = p.time.Clock()

#create sprite groups
turkey = p.sprite.Group()
turkey.add(Turkey())
fo_group = p.sprite.Group()
fo_group.add(FenceOpening())

# initialize misc items
level = 1
lives = NUM_LIVES
result = ""
bkgd_music = p.mixer.Sound("assets/backgroundmusic.wav")
moo = p.mixer.Sound("assets/moo.wav")
heart = p.image.load("assets/heart.png").convert()
heart = p.transform.scale(heart, (HEART_SIZE,HEART_SIZE))
heart.set_colorkey((0, 0, 0))
#clock = p.time.Clock()


#main loop
run = True
background = screen.copy()
draw_background(background)
add_hole(5)
#add a specified number of cows at a random y position on the screen without overlapping the cows
cowypos = list(range(TURKEY_START_Y + 10, FENCE_Y_POS - 10, COW_HEIGHT))
add_cow(3, random.choice(cowypos))



def get_font(size): # Returns font in the desired size
    return p.font.Font("assets/gamefont.ttf", size)

PLAY_BUTTON = Button(image=p.image.load("assets/Play Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 150),
                             text_input="PLAY", font=get_font(65), base_color="Black", hovering_color="White")
PLAY_AGAIN_BUTTON = Button(image=p.image.load("assets/Options Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),
                             text_input="PLAY", font=get_font(45), base_color="Black", hovering_color="White")
INSTRUCTIONS_BUTTON = Button(image=p.image.load("assets/Options Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),
                                text_input="INSTRUCTIONS", font=get_font(65), base_color="Black", hovering_color="White")
INSTRUCTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(65), base_color="Black", hovering_color="White")
QUIT_BUTTON = Button(image=p.image.load("assets/Quit Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150),
                             text_input="QUIT", font=get_font(65), base_color="Black", hovering_color="White")



timer = 300 # 5 minutes in seconds
timer_event = p.USEREVENT + 1 # create a custom event
p.time.set_timer(timer_event, 1000) # set the timer to trigger every second
timer_text = f"{timer // 60:02d}:{timer % 60:02d}"
time_font = p.font.Font("assets/gamefont.ttf", 24)
time_text = time_font.render(timer_text, True, (0,0,0))
#time_text_rect = time_text.get_rect((SCREEN_WIDTH - time_text - 10, 10))


#define screens
def play():
    # Call the countdown function with 5 minutes (300 seconds)
    screen.blit(time_text, (SCREEN_WIDTH - time_text.get_width() - 10, 10))
    # Update the display
    p.display.flip()

    while lives > 0:
        #set frame rate
        clock.tick(60)

        for event in p.event.get():
            if event.type == p.QUIT:
                run = False
            elif event.type == timer_event:
                timer -= 1

        # play background music
        bkgd_music.play(loops=-1)

        # draw the background
        screen.blit(background, (0, 0))

        #update game objects
        cows.update()
        turkey.update()
        fo_group.update()

        # #check for turkey-cow collision and fence opening collision
        # cow_collision = p.sprite.spritecollide(turkey, cows, False)
        # hole_collision = p.sprite.spritecollide(turkey, holes, False)
        # fo_collision = p.sprite.spritecollide(turkey, fo_group, False)
        # if cow_collision:
        #     turkey.x = TURKEY_START_X
        #     turkey.y = TURKEY_START_Y
        #     lives -= len(cow_collision)
        #     p.mixer.Sound.play(moo)
        # if hole_collision:
        #     turkey.x = TURKEY_START_X
        #     turkey.y = TURKEY_START_Y
        #     lives -= len(hole_collision)
        # if fo_collision:
        #     level += 1
        #     cows.empty()
        #     if level == 2:
        #         add_cow(2, random.choice(cowypos))
        #         add_hole(1)
        #     if level == 3:
        #         add_cow(1, random.choice(cowypos))
        #         add_hole(1)
        #     if level == 4:
        #         add_cow(2, random.choice(cowypos))
        #         add_hole()
        #     #end screen
        #     if level > 4:
        #         result = "win"
        #         result_screen()

        # if cow goes off screen
        for cow in cows:
            if cow.rect.x > SCREEN_WIDTH:
                cows.remove(cow)
                add_cow(1, cow.y, 0)


        holes.draw(screen)
        cows.draw(screen)
        turkey.draw(screen)
        fo_group.draw(screen)


        cows.update()
        turkey.update()
        fo_group.update()
        holes.update()

        # draw the lives in the upper left corner
        for i in range(lives):
            screen.blit(heart, (i * HEART_SIZE + 5, 5))

        p.display.update()

    if lives <= 0:
        result = "lose"
        result_screen()

        p.display.update()


def instructions():
    while True:
        # play background music
        bkgd_music.play(loops=-1)

        # draw the background
        screen.blit(background, (0, 0))

        OPTIONS_MOUSE_POS = p.mouse.get_pos()

        instruction_img = p.image.load("assets/instructions.png")
        screen.blit(instruction_img)

        # change mouse hover color
        INSTRUCTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        INSTRUCTIONS_BACK.update(screen)

        # determine mouse click events
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    start()

        p.display.update()

def start():
    while True:
        # play background music
        bkgd_music.play(loops=-1)

        # draw the background
        screen.blit(background, (0, 0))

        MENU_MOUSE_POS = p.mouse.get_pos()

        #change roll-over color
        for button in [PLAY_BUTTON, INSTRUCTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        # determine mouse click events
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if INSTRUCTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    instructions()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    p.quit()
                    sys.exit()

        p.display.update()

def result_screen():
    while True:
        # play background music
        bkgd_music.play(loops=-1)

        # draw the background
        screen.blit(background, (0, 0))
        #initialize mouse position
        mouse_pos = p.mouse.get_pos()

        if result == "win":
            win_text = get_font(100).render("You Won!", True, "White")
            screen.blit(win_text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 150))
            #score = timeleft
            #score_text = get_font(100).render(f"Score: {score}", True, "White")
            #screen.blit(score_text, (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 100))
        if result == "lose":
            lose_text = get_font(100).render("You Lost.", True, "White")
            screen.blit(lose_text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 150))


        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                if PLAY_AGAIN_BUTTON.checkForInput(mouse_pos):
                    play()
                if QUIT_BUTTON.checkForInput(mouse_pos):
                    p.quit()
                    sys.exit()

        p.display.update()

# open the start menu to start the game
start()