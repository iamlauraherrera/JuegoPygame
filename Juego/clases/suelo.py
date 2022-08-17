import pygame 

class Suelo(pygame.sprite.Sprite):
    def __init__(self): 
        super().__init__()
        self.image=pygame.image.load("fondos/suelo.png").convert() 
        self.rect=self.image.get_rect()