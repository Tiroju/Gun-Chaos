import pygame
import random
import platfo
from sheet import *
from pygame_functions import *

screen_width = 1200
screen_height = 800

class Player(pygame.sprite.Sprite):
    def __init__(self, sheet, x, y):
        super().__init__()
        self.sheet = sheet
        self.frame = 0
        self.image = sheet.get_sprite(0, 0, 110, 125)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.gravity = 0.2
        self.velocity = pygame.math.Vector2(0, 0)

    def update(self, platf_list, keys):
        if keys[pygame.K_LEFT]:
            self.velocity.x = -2
        elif keys[pygame.K_RIGHT]:
            self.velocity.x = 2
        else:
            self.velocity.x = 0

        if keys[pygame.K_UP] and self.rect.bottom == screen_height:
            self.velocity.y = -7

        self.velocity.y += self.gravity
        proposed_rect = self.rect.move(self.velocity)
        collided_with_platf = False
        for platf in platf_list:
            if proposed_rect.colliderect(platf.rect):
                if self.velocity.y > 0 and self.rect.bottom <= platf.rect.top:
                    self.rect.bottom = platf.rect.top
                    collided_with_platf = True
                elif self.velocity.y < 0 and self.rect.top >= platf.rect.bottom:
                    self.rect.top = platf.rect.bottom
                    collided_with_platf = True
                self.velocity.y = 0
                break

        if not collided_with_platf:
            self.rect = proposed_rect

        self.frame = (self.frame + 1) % 4
        self.image = self.sheet.get_sprite(128 * self.frame, 0, 110, 125)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Gun Chaos")
        self.clock = pygame.time.Clock()
        self.background_image = pygame.image.load('Images/MB.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (screen_width, screen_height))
        self.the_sheet = Spritesheet('Images/Sugnoma.png')
        self.players = pygame.sprite.Group(Player(self.the_sheet, 0, screen_height - 500),
                                           Player(self.the_sheet, 500, screen_height - 500))
        self.platf_list = [platfo.Platfo(220*i, 220+random.randint(1,30)) for i in range(6)]

    def run(self):
        while True:
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            keys = pygame.key.get_pressed()
            for player in self.players:
                player.update(self.platf_list, keys)

            self.screen.blit(self.background_image, (0, 0))
            for platf in self.platf_list:
                pygame.draw.rect(self.screen, (170, 170, 170), platf.rect)

            self.players.draw(self.screen)
            pygame.display.flip()
            
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
            if second_player_rect.top < 0:
                second_player_rect.top = 0
            if second_player_rect.bottom > screen_height:
                second_player_rect.bottom = screen_height

if __name__ == '__main__':
    game = Game()
    game.run()
