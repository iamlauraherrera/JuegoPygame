import pygame 

WHITE=(255,255,255)

class Enemy(pygame.sprite.Sprite): 
    def __init__(self): 
        super().__init__()
        self.image=pygame.image.load("img/dragon.png").convert()
        #self.image=pygame.transform.scale(pygame.image.load("img/dragon.png").convert(),(10,20))
        self.image.set_colorkey(WHITE) 
        self.rect=self.image.get_rect()

        

