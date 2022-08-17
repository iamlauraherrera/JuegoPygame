import pygame  

WHITE=(255,255,255)
BLACK=(0,0,0)

class Hero(pygame.sprite.Sprite): 
    def __init__(self,position): 
        self.sheet=pygame.image.load("img/Hero.png").convert()
        self.sheet.set_colorkey(WHITE) 
        self.sheet.set_clip(pygame.Rect(0,0,55,104))
        self.image=self.sheet.subsurface(self.sheet.get_clip())
        self.rect=self.image.get_rect()
        self.rect.topleft=position 
        self.frame=0 
        self.right_states={0:(0,0,55,104),1:(55,0,55,104),2:(110,0,55,104),3:(165,0,55,104)} 
        self.left_states={0:(0,104,55,104),1:(55,104,55,104),2:(110,104,55,104),3:(165,104,55,104)} 
        #self.up_states={}
        #self.down_states={}
        self.derecha=False 
        self.izquierda=False
        self.disparo=False
    
    def get_frame(self,frame_set):#le pasamos la tupla por parametros para mover el sprite sheet
            self.frame +=1 
            if self.frame>(len(frame_set)-1):   
                self.frame=0
            return frame_set[self.frame]
        
    def clip(self,clipped_rect): #coge el clip del diccionario y comprueba que de verdad es un diccionario
            if type(clipped_rect) is dict: 
                self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
            else: 
                self.sheet.set_clip(pygame.Rect(clipped_rect))
            return clipped_rect 
        
    def update(self,direccion):  #comprueba la direccion y pasa el diccionario a clip para comprobarlo 
            if direccion=='left': 
                 self.clip(self.left_states)
                 self.izquierda=True 
                 self.derecha=False
               
            if direccion=='right': 
                 self.clip(self.right_states)
                 self.derecha=True 
                 self.izquierda=False
             
            if direccion=='stand_left': 
                 self.clip(self.left_states[0])
                 self.izquierda=True 
                 self.derecha=False
                 
            if direccion=='stand_right':
                 self.clip(self.right_states[0])
                 self.derecha=True 
                 self.izquierda=False
               
            self.image=self.sheet.subsurface(self.sheet.get_clip())
        
    def handle_event(self,event): #Cuando el jugador pulsa determinada tecla
           
            if event.type==pygame.KEYDOWN: 
                if event.key==pygame.K_LEFT: 
                    self.update('left')
                    self.rect.x-=10
                if event.key==pygame.K_RIGHT:  
                    self.update('right')
                    self.rect.x+=10
            if event.type==pygame.KEYUP: 
                if event.key==pygame.K_LEFT:
                    self.update('stand_left')
                if event.key==pygame.K_RIGHT: 
                    self.update('stand_right') 
        
            if event.type==pygame.MOUSEBUTTONDOWN: 
                self.disparo=True 
               
                   
       

