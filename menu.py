# -*- coding: utf-8 -*-
"""
Created on Tue May  9 17:15:27 2023

@author: mamadou.sakho
"""

"""
Importing important libraries
"""
import pygame, sys
import test

"""
Setting up an environment to initialize pygame
"""
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((800, 600),0,32)
 
#setting font settings
font = pygame.font.SysFont(None, 30)
 
"""
A function that can be used to write text on our screen and buttons
"""
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
# A variable to check for the status later
click = False
 
# Main container function that holds the buttons and game functions
def main_menu():
    while True:
 
        screen.fill((192,192,192))
 
        mx, my = pygame.mouse.get_pos()

        #creating buttons
        button_1 = pygame.Rect(300, 200, 200, 50)
        button_2 = pygame.Rect(300, 280, 200, 50)
        button_3 = pygame.Rect(1, 0, 50, 25)

        #defining functions when a certain button is pressed
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                quitter()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)
 
        #writing text on top of button
        draw_text('Main Menu', font, (0,0,0), screen, 330, 40)
        draw_text('PLAY', font, (255,255,255), screen, 370, 215)
        draw_text('OPTIONS', font, (255,255,255), screen, 350, 300)
        draw_text('QUIT', font, (255,255,255), screen, 0, 0)


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)


"""
This function is called when the "PLAY" button is clicked.
"""
def game():
    exec(open("test.py").read())
    
def quitter():
    pygame.quit()
    sys.exit()

"""
This function is called when the "OPTIONS" button is clicked.
"""
def options():
    # basic font for user typed
    base_font = pygame.font.Font(None, 32)
    user_text = ''
      
    # create rectangle
    input_rect = pygame.Rect(200, 100, 140, 32)
      
    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')
      
    # color_passive store color(chartreuse4) which is
    # color of input box.
    color_passive = pygame.Color('White')
    color = color_passive
      
    active = False
    running = True
    while running:
 
        draw_text('OPTIONS SCREEN', font, (255, 255, 255), screen, 20, 20)
        for event in pygame.event.get():
            # if user types QUIT then the screen will close
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
      
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the user clicked inside the input rectangle
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            # Check if the user clicked outside the input rectangle
            if event.type == pygame.MOUSEBUTTONDOWN and not input_rect.collidepoint(event.pos):
                active = False
            
            
            if event.type == pygame.KEYDOWN:
                if active == True :
                    if event.key == pygame.K_BACKSPACE:
                        # get text input from 0 to -1 i.e. end.
                        user_text = user_text[:-1]
                    # Unicode standard is used for string formation
                    else:
                        user_text += event.unicode
          
        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen, color, input_rect,0)
  
        text_surface = base_font.render(user_text, True, (0, 0, 0))
        # render at position stated in arguments
        screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        # display.flip() will update only a portion of the
        # screen to updated, not full area
        pygame.display.flip()
        pygame.display.update()
        mainClock.tick(60)
 
main_menu()