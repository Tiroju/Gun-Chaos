import pygame


class Spritesheet:
    def __init__(self,filename):
        self.filename= filename
        self.sprite_sheet= pygame.image.load(filename).convert()
        
    def get_sprite(self,x,y,w,h):
        sprite = pygame.Surface((w,h))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprite_sheet,(0,0),(x,y,w,h))
        return sprite

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image
    
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("Images/balle.png")
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        
    def tir(self,direc,x,y):
        """
        Fonction pour déplacer la balle dans la direction que le joueur regarde
        """
        if direc == "D" :
            self.image = pygame.image.load("Images/balle_reverse.png")
            self.image = pygame.transform.scale(self.image, (20, 20))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.rect.x += 200
            
        elif direc == "G" :
            self.image = pygame.image.load("Images/balle.png")
            self.image = pygame.transform.scale(self.image, (20, 20))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.rect.x -= 200
            
            
class Player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = "D"
        self.cd = 200
        self.vie = 5
        self.on_ground=False
        
    def jump(self):
        """
        Fonction pour permettre au personnage de sauter
        """
        if self.cd >= 1000 and self.on_ground:
            self.y -= 150
            self.cd = 0
            self.on_ground=False
            return True
        return False
        
    def mort(self):
        """
        Fonction qui renvoie True si le joueur n'a plus de vie et False sinon
        """
        if self.vie <= 0:
            return True
        return False
