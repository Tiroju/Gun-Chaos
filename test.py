import pygame
from pygame.locals import *
import math
from sheet import *
from pygame_functions import *

screen_width = 1200
screen_height = 540
gravity=0.8

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Gun Chaos")
background_image = pygame.image.load('Images/gg.png')
BLACK=(0,0,0)

the_sheet = Spritesheet('Images/Sugnoma.png')
player1_posx=500.0
player1_posy=0
player2_posx=1000.0
player2_posy=0
the_rev_sheet=Spritesheet('Images/Sugnoma_reverse.png')
first_player = the_sheet.get_sprite(0, 0, 128, 125)
second_player = the_sheet.get_sprite(128, 0, 128, 125)
the_player=Player(500,0)
the_second_player=Player(1000,0)

clock=pygame.time.Clock()

left1_animations=[the_rev_sheet.get_sprite(896,128,128,128),
                 the_rev_sheet.get_sprite(896,256,128,128),
                 the_rev_sheet.get_sprite(896,384,128,128),
                 the_rev_sheet.get_sprite(896,512,128,128)]

right1_animations=[the_sheet.get_sprite(0,128,128,110),
                  the_sheet.get_sprite(0,256,128,110),
                  the_sheet.get_sprite(0,384,128,110),
                  the_sheet.get_sprite(0,512,128,110)]

second_player_direction=''

left2_animations=[the_rev_sheet.get_sprite(768,128,128,128),
                 the_rev_sheet.get_sprite(768,256,128,128),
                 the_rev_sheet.get_sprite(768,384,128,128),
                 the_rev_sheet.get_sprite(768,512,128,128)]

right2_animations=[the_sheet.get_sprite(128,128,128,110),
                  the_sheet.get_sprite(128,256,128,110),
                  the_sheet.get_sprite(128,384,128,110),
                  the_sheet.get_sprite(128,512,128,110)]
second_player_direction=''


anim_loop=1.0
player_width = 65
player_height = 65
first_player_rect = pygame.Rect(500, screen_height - 500, player_width, player_height)
second_player_rect = pygame.Rect(1000, screen_height - 500, player_width, player_height)
platf_rects = [Rect(1, 420, 300, 25),
               Rect(100,400, 300, 25),
               Rect(220,370, 465, 25),
               Rect(290,340, 320, 25),
               Rect(260,240, 200, 25),
               Rect(130,70, 200, 25),
               Rect(370,160,440, 25),
               Rect(820,70, 200, 25),
               Rect(740, 410, 370, 25)]

first_player_vel_y = 0.0
second_player_vel_y = 0.0

on_platf_player1 = False
on_platf_player2 = False

movement_speed=8

while True:
    collide1 = False
    collide2 = False
    
    t=clock.tick()
    the_player.cd+=t
    the_second_player.cd+=t
    
    if the_player.mort():
        a=1
    if the_second_player.mort():
        a=2
    
    for platf_rect in platf_rects:
        if first_player_rect.colliderect(platf_rect):
            collide1 = True

        if second_player_rect.colliderect(platf_rect):
            collide2 = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    

    

    # Move first player with arrow keys
    if keys[pygame.K_LEFT] :
        first_player_direction="G"
        proposed_first_player_rect = first_player_rect.move(-2*gravity, 0)
        player1_posx=player1_posx-2*gravity
        first_player=left1_animations[math.floor(anim_loop)]
        anim_loop+=0.01
        if anim_loop>=3:
            anim_loop=1
        if not proposed_first_player_rect.colliderect(second_player_rect):
            first_player_rect = proposed_first_player_rect
       

    # check for collisions with platforms
        """for platf in platf_list:
            if proposed_first_player_rect.colliderect(platf.rect):
                first_player_vel_y = 0
                first_player_rect.bottom = platf.rect.top"""
                

    if keys[pygame.K_RIGHT]:
        first_player_direction="D"
        proposed_first_player_rect = first_player_rect.move(2*gravity, 0)
        player1_posx=player1_posx+2*gravity
        first_player=right1_animations[math.floor(anim_loop)]
        anim_loop+=0.01
        if anim_loop>=3:
            anim_loop=1
        if not proposed_first_player_rect.colliderect(second_player_rect):
            first_player_rect = proposed_first_player_rect

        # check for collisions with platforms
        """for platf in platf_list:
            if proposed_first_player_rect.colliderect(platf.rect):
                first_player_vel_y = 0
                first_player_rect.bottom = platf.rect.top"""
            

    # Jump with up arrow key
    if keys[pygame.K_UP] :
        the_player.jump()
        first_player_vel_y = -5

    first_player_vel_y += gravity
    proposed_rect = first_player_rect.move(0, int(first_player_vel_y))
    if not proposed_rect.colliderect(second_player_rect):
        first_player_rect = proposed_rect
    else:
        first_player_vel_y = 0.0
            # check for collisions with platforms
                

    if keys[pygame.K_q] :
        second_player_direction="G"
        proposed_second_player_rect = second_player_rect.move(-2*gravity, 0)
        player2_posx=player2_posx-2*gravity
        second_player=left2_animations[math.floor(anim_loop)]
        anim_loop+=0.01
        if anim_loop>=4:
            anim_loop=1
        if not proposed_second_player_rect.colliderect(first_player_rect):
            second_player_rect = proposed_second_player_rect

        # check for collisions with platforms
        """for platf in platf_list:
            if proposed_second_player_rect.colliderect(platf.rect):
                second_player_vel_y = 0
                second_player_rect.bottom = platf.rect.top"""
                

    if keys[pygame.K_d]:
        second_player_direction="D"
        proposed_second_player_rect = second_player_rect.move(2*gravity, 0)
        player2_posx += movement_speed
        second_player=right2_animations[math.floor(anim_loop)]
        anim_loop+=0.01
        if anim_loop>=4:
            anim_loop=1
        if not proposed_second_player_rect.colliderect(first_player_rect):
            second_player_rect = proposed_second_player_rect
        """for platf in platf_list:
            platf.update_rect()
            if proposed_first_player_rect.colliderect(platf.rect):
                first_player_vel_y = 0
                first_player_rect.bottom = platf.rect.top
            if proposed_second_player_rect.colliderect(platf.rect):
                second_player_vel_y = 0
                second_player_rect.bottom = platf.rect.top"""
                

    # Jump with W key
    if keys[pygame.K_z] :
        the_second_player.jump()
        second_player_vel_y = -5

    second_player_vel_y += gravity
    proposed_rect = second_player_rect.move(0, int(second_player_vel_y))
    if not proposed_rect.colliderect(first_player_rect):
        second_player_rect = proposed_rect
    else:
        second_player_vel_y = 0.0
    
    first_player_vel_y += gravity
    second_player_vel_y += gravity

    proposed_first_player_rect = first_player_rect.move(0, int(first_player_vel_y))
    proposed_second_player_rect = second_player_rect.move(0, int(second_player_vel_y))

    for platf_rect in platf_rects:
        if platf_rect.colliderect(first_player_rect):
            if player1_posy>0 :
                first_player_rect.bottom=platf_rect.top




    # Prevent players from moving off the screen
    if first_player_rect.left < 0:
        first_player_rect.left = 0
    if first_player_rect.right > screen_width:
        first_player_rect.right = screen_width
    if first_player_rect.top < 0:
        first_player_rect.top = 0
    if first_player_rect.bottom > screen_height:
        first_player_rect.bottom = screen_height

    if second_player_rect.left < 0:
        second_player_rect.left = 0
    if second_player_rect.right > screen_width:
        second_player_rect.right = screen_width
    if second_player_rect.top< 0:
        second_player_rect.top = 0
    if second_player_rect.bottom > screen_height:
        second_player_rect.bottom = screen_height
    
    first_player=pygame.transform.scale(first_player,(65,65))
    second_player=pygame.transform.scale(second_player,(65,65))
    
    for platf in platf_rects:
        if first_player_rect.colliderect(platf):
            if first_player_vel_y > 0:
                first_player_rect.y = platf.y - player_height
                first_player_vel_y = 0.0
                the_player.on_ground = True
                break
            elif first_player_vel_y < 0:
                first_player_rect.y = platf.y + platf.height
                first_player_vel_y = 0.0
                break
        else:
            the_player.on_ground = False
    
    for platf in platf_rects:
        if second_player_rect.colliderect(platf):
            if second_player_vel_y > 0:
                second_player_rect.y = platf.y - player_height
                second_player_vel_y = 0.0
                the_second_player.on_ground = True
                break
            elif second_player_vel_y < 0:
                second_player_rect.y = platf.y + platf.height
                second_player_vel_y = 0.0
                break
        else:
            the_second_player.on_ground = False   

    screen.fill((0, 0, 0))
    screen.blit(background_image,(0,0))
    screen.blit(first_player,first_player_rect )
    screen.blit(second_player, second_player_rect)
    pygame.draw.rect(screen, (255, 255, 0), first_player_rect)
    pygame.draw.rect(screen, (255, 0, 255), second_player_rect)
    for platf_rect in platf_rects:
        pygame.draw.rect(screen, (255, 0, 0), platf_rect)
    pygame.display.update()        