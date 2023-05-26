import pygame
class Platfo:
    def __init__(self,x,y):
        self.img=pygame.image.load("Images/UNY4.png").convert_alpha()
        self.rect=pygame.Rect(x,y,100,20)
        self.rect.x=x
        self.rect.y=y
        self.nb_contacts=0
        
    def update_rect(self):
        self.rect = pygame.Rect(self.rect.left, self.rect.top, self.img.get_width(), self.img.get_height())