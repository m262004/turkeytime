import random, sys, time
import pygame as p
import pygame.mixer

from game_parameters import *
from turkey import *
from utilities import *
from cow2 import *
from fenceopening import *
from button import Button
import pickle

p.init()
p.mixer.init()

#create screen
screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
p.display.set_caption("Turkey Time")
clock = p.time.Clock()

#create sprite groups
turkey = Turkey()
turkey_group = p.sprite.Group()
turkey_group.add(turkey)
fo_group = p.sprite.Group()
fo_group.add(FenceOpening())

# initialize misc items
level = 1
lives = NUM_LIVES
result = ""
bkgd_music = p.mixer.Sound("assets/backgroundmusic.wav")
moo = p.mixer.Sound("assets/moo.wav")
c1 = p.mixer.Channel(0)
c2 = p.mixer.Channel(1)
heart = p.image.load("assets/heart.png").convert()
heart = p.transform.scale(heart, (HEART_SIZE,HEART_SIZE))
heart.set_colorkey((0, 0, 0))

#code to have backgroudmusic.wav play in the background and moo.wav play when the sprite groups turkey_group and cows collide

# Define the file name for saving and loading
file_name = "game_data"
# Try to load the existing file and get the score from it
try:
    with open(file_name, "rb") as file:
        score = pickle.load(file)
# If the file does not exist, set the score to zero
except:
    score = 0


#main loop
run = True
background = screen.copy()
draw_background(background)
add_hole(5)
#add a specified number of cows at a random y position on the screen without overlapping the cows
cowypos = list(range(TURKEY_START_Y + COW_HEIGHT + 10, FENCE_Y_POS - 10, COW_HEIGHT))
add_cow(3, random.choice(cowypos))


def get_font(size): # Returns font in the desired size
    return p.font.Font("assets/gamefont.ttf", size)

PLAY_BUTTON = Button(image=p.image.load("assets/Play Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 150),
                             text_input="PLAY", font=get_font(65), base_color="Black", hovering_color="White")
PLAY_AGAIN_BUTTON = Button(image=p.image.load("assets/Quit Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),
                             text_input="MAIN MENU", font=get_font(45), base_color="Black", hovering_color="White")
INSTRUCTIONS_BUTTON = Button(image=p.image.load("assets/Options Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),
                                text_input="INSTRUCTIONS", font=get_font(65), base_color="Black", hovering_color="White")
INSTRUCTIONS_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(65), base_color="Black", hovering_color="White")
QUIT_BUTTON = Button(image=p.image.load("assets/Quit Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150),
                             text_input="QUIT", font=get_font(65), base_color="Black", hovering_color="White")

def draw_game_objects():
    holes.draw(screen)
    cows.draw(screen)
    fo_group.draw(screen)
    turkey_group.draw(screen)
    turkey_group.x = TURKEY_START_X
    turkey_group.y = TURKEY_START_Y
def empty_groups():
    fo_group.empty()
    cows.empty()



# timer = 300 # 5 minutes in seconds
# timer_event = p.USEREVENT + 1 # create a custom event
# p.time.set_timer(timer_event, 1000) # set the timer to trigger every second
# time_font = p.font.Font("assets/gamefont.ttf", 24)
# time_text = time_font.render(f"{timer // 60:02d}:{timer % 60:02d}", True, (0,0,0))
##time_text_rect = time_text.get_rect((SCREEN_WIDTH - time_text.get_width() - 10, 10))

# def format_time(time_sec):
# # Calculate the minutes and seconds from the time in seconds
# mins, secs = divmod(time_sec, 60)
# # Format the time as mm:ss
# timeformat = ‘{:02d}:{:02d}’.format(mins, secs)
# return timeformat

run = True


#define screens
def play():
    level = 1
    lives = NUM_LIVES
    while run:
        #set frame rate
        #clock.tick(60)
        timer = 300  # 5 minutes in seconds
        timer_event = p.USEREVENT + 1  # create a custom event
        p.time.set_timer(timer_event, 1000)  # set the timer to trigger every second
        time_font = p.font.Font("assets/gamefont.ttf", 24)
        time_text = time_font.render(f"{timer // 60:02d}:{timer % 60:02d}", True, (0, 0, 0))
        #screen.blit(time_text, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30, 10))

        # Call the countdown function with 5 minutes (300 seconds)
        #screen.blit(time_text, (SCREEN_WIDTH - time_text.get_width() - 10, 10))

        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            # if event.type == timer_event:
            #     timer -= 1
            #     time_text = time_font.render(f"{timer // 60:02d}:{timer % 60:02d}", True, (0, 0, 0))
            if lives < 0: # or timer == 0:
                result_screen("lose")
            if  p.key.get_pressed()[p.K_s]:
                with open(file_name, "wb") as file:
                    pickle.dump(score, file)

            # elif event.type == timer_event:
            #     timer -= 1

        # play background music
        c1.play(bkgd_music, loops=-1)

        # draw the background
        screen.blit(background, (0, 0))

        #update game objects
        cows.update()
        turkey_group.update()
        fo_group.update()

        #check for turkey-cow collision and fence opening collision
        cow_collision = p.sprite.groupcollide(turkey_group, cows, False, False)
        hole_collision = p.sprite.groupcollide(turkey_group, holes, False, False)
        fo_collision = p.sprite.groupcollide(turkey_group, fo_group, False, False)
        if cow_collision:
            turkey.x = TURKEY_START_X
            turkey.y = TURKEY_START_Y
            c2.play(moo)
            lives -= 1
            turkey_group.update()
        if hole_collision:
            turkey.x = TURKEY_START_X
            turkey.y = TURKEY_START_Y
            lives -= 1


        if fo_collision:
            level += 1
            turkey_group.rect.center = (TURKEY_START_X, TURKEY_START_Y)
            #cows.empty()
            if level == 2:
                add_cow(2, random.choice(cowypos))
                add_hole(1)
            if level == 3:
                add_cow(1, random.choice(cowypos))
                add_hole(1)
            if level == 4:
                add_cow(2, random.choice(cowypos))
                add_hole()
            #end screen
            if level > 4:
                result_screen("win")

        # if cow goes off-screen
        for cow in cows:
            if cow.rect.x > SCREEN_WIDTH:
                cows.remove(cow)
                add_cow(1, cow.y, 0)

        draw_game_objects()
        # holes.draw(screen)
        # cows.draw(screen)
        # fo_group.draw(screen)
        # turkey_group.draw(screen)

        cows.update()
        turkey_group.update()
        fo_group.update()
        holes.update()

        # draw the lives in the upper left corner
        for i in range(lives):
            screen.blit(heart, (i * HEART_SIZE + 5, 5))

        #p.display.flip()
        p.display.update()
        clock.tick(60)

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

def result_screen(result):
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
            # save score if s key is pressed
            if event.key == p.K_s:
                with open(file_name, "wb") as file:
                    pickle.dump(score, file)

        if result == "lose":
            empty_groups()
            lose_text = get_font(100).render("You Lost", True, "White")
            screen.blit(lose_text, (SCREEN_WIDTH/2 - lose_text.get_width()/2, SCREEN_HEIGHT/2 - 150))
            # play background music
            bkgd_music.play(loops=-1)
            MOUSE_POS = p.mouse.get_pos()
            # change mouse hover color
            PLAY_AGAIN_BUTTON.changeColor(MOUSE_POS)
            PLAY_AGAIN_BUTTON.update(screen)
            for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()
                if event.type == p.MOUSEBUTTONDOWN:
                    if PLAY_AGAIN_BUTTON.checkForInput(MOUSE_POS):
                        start()

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