import pygame 

WHITE=(255,255,255) 

class Bola_hielo(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("img/bolaHielo.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
  
      
