import pygame
from pygame.locals import *
import math
from sheet import *
from pygame_functions import *

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 1200
screen_height = 540
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gun Chaos")

# Load images
background_image = pygame.image.load('Images/gg.png')

# Define colors
BLACK = (0, 0, 0)

# Define player and platform variables
player_width = 65
player_height = 65
gravity = 0.8
movement_speed = 8

player1_posx = 500.0
player1_posy = 0
player2_posx = 1000.0
player2_posy = 0

first_player_direction = ""
second_player_direction = ""
anim_loop = 1.0

the_sheet = Spritesheet('Images/Sugnoma.png')
the_rev_sheet = Spritesheet('Images/Sugnoma_reverse.png')

first_player = the_sheet.get_sprite(0, 0, 128, 125)
second_player = the_sheet.get_sprite(128, 0, 128, 125)

left1_animations = [the_rev_sheet.get_sprite(896, 128, 128, 128),
                    the_rev_sheet.get_sprite(896, 256, 128, 128),
                    the_rev_sheet.get_sprite(896, 384, 128, 128),
                    the_rev_sheet.get_sprite(896, 512, 128, 128)]

right1_animations = [the_sheet.get_sprite(0, 128, 128, 110),
                     the_sheet.get_sprite(0, 256, 128, 110),
                     the_sheet.get_sprite(0, 384, 128, 110),
                     the_sheet.get_sprite(0, 512, 128, 110)]

left2_animations = [the_rev_sheet.get_sprite(768, 128, 128, 128),
                    the_rev_sheet.get_sprite(768, 256, 128, 128),
                    the_rev_sheet.get_sprite(768, 384, 128, 128),
                    the_rev_sheet.get_sprite(768, 512, 128, 128)]

right2_animations = [the_sheet.get_sprite(128, 128, 128, 110),
                     the_sheet.get_sprite(128, 256, 128, 110),
                     the_sheet.get_sprite(128, 384, 128, 110),
                     the_sheet.get_sprite(128, 512, 128, 110)]

first_player_rect = pygame.Rect(500, screen_height - 500, player_width, player_height)
second_player_rect = pygame.Rect(1000, screen_height - 500, player_width, player_height)

platf_rects = [Rect(1, 420, 850, 150),
               Rect(170, 400, 565, 150),
               Rect(220, 370, 465, 150),
               Rect(290, 340, 320, 150),
               Rect(340, 300, 200, 150),
               Rect(30, 150, 70, 50),
               Rect(250, 150, 280, 50),
               Rect(800, 150, 320, 50),
               Rect(1100, 420, 850, 150)]

first_player_vel_y = 0.0
second_player_vel_y = 0.0

on_platf_player1 = False
on_platf_player2 = False

clock = pygame.time.Clock()

def game_loop():
    global player1_posx, player1_posy, player2_posx, player2_posy, first_player_vel_y, second_player_vel_y
    global first_player_direction, second_player_direction, anim_loop, on_platf_player1, on_platf_player2

    game_exit = False

    while not game_exit:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        # Player 1 movement
        if keys[pygame.K_LEFT]:
            player1_posx -= movement_speed
            first_player_direction = "left"
        if keys[pygame.K_RIGHT]:
            player1_posx += movement_speed
            first_player_direction = "right"

        # Player 2 movement
        if keys[pygame.K_a]:
            player2_posx -= movement_speed
            second_player_direction = "left"
        if keys[pygame.K_d]:
            player2_posx += movement_speed
            second_player_direction = "right"

        # Apply gravity to both players
        first_player_vel_y += gravity
        second_player_vel_y += gravity

        # Player 1 collision detection and handling
        first_player_rect.x = player1_posx
        first_player_rect.y = player1_posy

        for platf in platf_rects:
            if first_player_rect.colliderect(platf):
                if first_player_vel_y > 0:
                    first_player_rect.y = platf.y - player_height
                    first_player_vel_y = 0.0
                    on_platf_player1 = True
                    break
                elif first_player_vel_y < 0:
                    first_player_rect.y = platf.y + platf.height
                    first_player_vel_y = 0.0
                    break
            else:
                on_platf_player1 = False

        # Player 2 collision detection and handling
        second_player_rect.x = player2_posx
        second_player_rect.y = player2_posy

        for platf in platf_rects:
            if second_player_rect.colliderect(platf):
                if second_player_vel_y > 0:
                    second_player_rect.y = platf.y - player_height
                    second_player_vel_y = 0.0
                    on_platf_player2 = True
                    break
                elif second_player_vel_y < 0:
                    second_player_rect.y = platf.y + platf.height
                    second_player_vel_y = 0.0
                    break
            else:
                on_platf_player2 = False

        # Update player positions
        player1_posy += first_player_vel_y
        player2_posy += second_player_vel_y

        # Render background
        screen.blit(background_image, (0, 0))

        # Render platforms
        for platf in platf_rects:
            pygame.draw.rect(screen, BLACK, platf)

        # Render player 1
        if first_player_direction == "left":
            screen.blit(left1_animations[math.floor(anim_loop)], (player1_posx, player1_posy))
        elif first_player_direction == "right":
            screen.blit(right1_animations[math.floor(anim_loop)], (player1_posx, player1_posy))

        # Render player 2
        if second_player_direction == "left":
            screen.blit(left2_animations[math.floor(anim_loop)], (player2_posx, player2_posy))
        elif second_player_direction == "right":
            screen.blit(right2_animations[math.floor(anim_loop)], (player2_posx, player2_posy))

        # Update animation loop index
        anim_loop += 0.1
        if anim_loop >= 4:
            anim_loop = 0

        pygame.display.update()
        clock.tick(60)

game_loop()
