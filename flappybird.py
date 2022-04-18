import pygame, sys
# from pygame import mixer
from random import randint
from time import sleep
import numpy as np



pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load("dao xiang.mp3")
# pygame.mixer.music.set_volume(0.7)
# pygame.mixer.music.play()


clock= pygame.time.Clock()

display_size = [550,500]
display = pygame.display.set_mode(display_size)
display_lose = pygame.display.set_mode(display_size)
bg = pygame.image.load('image/fl_bg.png')
bg = pygame.transform.scale(bg,(550,500))

text = pygame.font.Font(None,30)
textt = pygame.font.SysFont('arialblack',15)
name = "Rotsarak"
texte = pygame.font.Font(None, 30)
textc = pygame.font.Font(None, 22)
over = "Game over bitch!!!"
guide= "Press R to restart, Press Q to leave the game, Press up arrow to jump"

pole_width = 55
pole_gap = 100
pole_x = 550
top_pole_height = randint(20,440)
pole_color = (45,15,85)

polea_width = 70
polea_gap = 125
polea_x = 550
top_polea_height = randint(20,440)
polea_color = (50,0,50)

bird = pygame.image.load('image/angry-bird-icon.png')
bird = pygame.transform.scale(bird,(40,40))
bird_x = 100
bird_y = 200
score = 0

keep_alive = True
run = True
while run:
    # event adding code
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        run = False
    if keys[pygame.K_r]:
        keep_alive = True
        pole_x = 550
        polea_x = 550 + 500
        score = 0
    if keep_alive == True:

        #control the bird
        bird_y = bird_y + 1.6
        if keys[pygame.K_UP]:
            bird_y = bird_y - 8

        #display bird and background
        display.blit(bg, [0,0])
        display.blit(bird, [bird_x, bird_y])

        #pole code
        pole_x = pole_x - 1.5
        print("pole_x = " , pole_x)
        if pole_x <= -pole_width:
            pole_x = 550
            top_pole_height = randint(50, 100)
            score = score + 1
        pygame.draw.rect(display, pole_color, (pole_x , 0, pole_width, top_pole_height))
        pygame.draw.rect(display, pole_color, (pole_x, top_pole_height + pole_gap, pole_width, 500))

        print("bird_x=",bird_x)
        print("bird_y",bird_y)
        if pole_x <= bird_x + 40 and bird_x <= pole_x + pole_width:
            if bird_y <= top_pole_height or bird_y + 40 >= top_pole_height + pole_gap:
                # if score != 0:
                #     score = score - 1
                over_texte = texte.render(f'{over} with Score {score}',True, (0,0,0),sleep(.02))
                print(display.blit(over_texte, (160,220)))
                keep_alive = False

        #2nd pole code
        polea_x = polea_x - 0.8
        if polea_x <= -polea_width + 200:
            polea_x = 550 + 500
            top_polea_height = randint(20, 450)

        pygame.draw.rect(display, polea_color, (polea_x, 0, polea_width, top_polea_height))
        pygame.draw.rect(display, polea_color, (polea_x, top_polea_height + polea_gap, polea_width, 500))

        if polea_x <= bird_x + 40 and bird_x <= polea_x + polea_width:
            if bird_y <= top_polea_height or bird_y + 40 >= top_polea_height + polea_gap:
                if score != 0:
                    score = score - score - 1

        score_text = text.render(f'Score:{score}', True, (0,255,255))
        display.blit(score_text,(0,0))

    guide_text= textc.render(f'{guide}', True, (255,0,0))
    display.blit(guide_text,(10,480))

    pygame.display.update()
    clock.tick(60)
