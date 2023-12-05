import random, sys, time
import pygame as p
import pygame.mixer
from game_parameters import *
from turkey import *
from utilities import *
from cow2 import *
from fenceopening import *
from button import Button

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

#add a specified number of cows at a random y position on the screen without overlapping the cows
cowypos = list(range(TURKEY_START_Y + COW_HEIGHT + 10, FENCE_Y_POS - 10, COW_HEIGHT))

def get_font(size): # Returns font in the desired size
    return p.font.Font("assets/gamefont.ttf", size)

PLAY_BUTTON = Button(image=p.image.load("assets/Play Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 150),
                             text_input="PLAY", font=get_font(65), base_color="Black", hovering_color="White")
PLAY_AGAIN_BUTTON = Button(image=p.image.load("assets/Quit Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),
                             text_input="MAIN MENU", font=get_font(45), base_color="Black", hovering_color="White")
INSTRUCTIONS_BUTTON = Button(image=p.image.load("assets/Options Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2),
                                text_input="INSTRUCTIONS", font=get_font(65), base_color="Black", hovering_color="White")
INSTRUCTIONS_BACK = Button(image=None, pos=(140, 460),
                            text_input="BACK", font=get_font(45), base_color="Black", hovering_color="White")
QUIT_BUTTON = Button(image=p.image.load("assets/Quit Rect.png"), pos=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 150),
                             text_input="QUIT", font=get_font(65), base_color="Black", hovering_color="White")

def draw_game_objects():
    holes.draw(screen)
    cows.draw(screen)
    fo_group.draw(screen)
    turkey_group.draw(screen)

def update_game_objects():
    cows.update()
    turkey_group.update()
    fo_group.update()
    holes.update()
def empty_groups():
    fo_group.empty()
    cows.empty()
    holes.empty()
def reset_level():
    empty_groups()
    add_cow(3, random.choice(cowypos))
    add_hole(5)
    add_fo(1)
    draw_game_objects()
    update_game_objects()

# initialize timer event
timer_event = p.USEREVENT + 1  # create a custom event
p.time.set_timer(timer_event, 1000)  # set the timer to trigger every second

#main loop
run = True
background = screen.copy()
draw_background(background)

#define screens
def play():
    level = 1
    lives = NUM_LIVES
    reset_level()
    timer = 120 #in seconds
    score = 0
    while run:
        #set frame rate
        clock.tick(60)

        # play background music
        c1.play(bkgd_music, loops=-1)

        # draw the background
        screen.blit(background, (0, 0))

        # draw the level
        level_font = p.font.Font("assets/gamefont.ttf", 24)
        level_text = level_font.render(f"Level: {level} of 4", True, "Black")
        screen.blit(level_text, (10, HEART_SIZE + 10))

        # draw timer on screen
        time_font = p.font.Font("assets/gamefont.ttf", 32)
        time_text = time_font.render(f"{timer // 60:02d}:{timer % 60:02d}", True, (0, 0, 0))
        screen.blit(time_text, (SCREEN_WIDTH - 125, 15))


        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == timer_event:
                timer -= 1
                time_text = time_font.render(f"{timer // 60:02d}:{timer % 60:02d}", True, (0, 0, 0))
                if timer <= 0:
                    result_screen("lose")
            if lives < 0: # or timer == 0:
                result_screen("lose")


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
            turkey.x = TURKEY_START_X
            turkey.y = TURKEY_START_Y
            reset_level()
            if level == 2:
                add_cow(2, random.choice(cowypos))
                add_hole(1)
            if level == 3:
                add_cow(3, random.choice(cowypos))
                add_hole(1)
            if level == 4:
                add_cow(3, random.choice(cowypos))
                add_hole(1)
            #end screen
            if level > 4:
                # high_score = load_high_score()
                # score = int(timer * 10)
                # def retrieve_score():
                #     return score
                # if score > high_score:
                #     high_score = score
                #     save_high_scores(high_score)
                result_screen("win")

        # if cow goes off-screen
        for cow in cows:
            if cow.rect.x > SCREEN_WIDTH:
                cows.remove(cow)
                add_cow(1, cow.y, 0)

        draw_game_objects()

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
            result_screen("lose")

        p.display.update()


def instructions():
    while True:
        # play background music
        bkgd_music.play(loops=-1)

        # draw the background
        screen.blit(background, (0, 0))

        OPTIONS_MOUSE_POS = p.mouse.get_pos()

        instruction_img = p.image.load("assets/instructions.png")
        instruction_img = p.transform.scale(instruction_img, (I_WIDTH, I_HEIGHT))
        screen.blit(instruction_img, (SCREEN_HEIGHT/2 - instruction_img.get_height()/2 - 50, SCREEN_WIDTH/2 - instruction_img.get_width()/2 + 70))

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
            empty_groups()
            win_text = get_font(100).render("You Won!", True, "White")
            screen.blit(win_text, (SCREEN_WIDTH / 2 - win_text.get_width() / 2, SCREEN_HEIGHT / 2 - 150))
            # load and display high score
            # high_score = load_high_score()
            # high_score_text = get_font(50).render(f"Your score: {score}  High score: {high_score}", True, "White")
            # screen.blit(high_score_text, (SCREEN_WIDTH / 2 - win_text.get_width() / 2, SCREEN_HEIGHT / 2 - 200))

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