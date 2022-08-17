import pygame            #importamos la libreria 
import sys  
from math import pi

#variables 
ancho_pantalla=800 
alto_pantalla=608 
color_fondo=(34,121,153)
color_elementos=(153,88,18)
size=(ancho_pantalla,alto_pantalla)
clock=pygame.time.Clock()  # esto es para optimizar las animaciones  

#iniciamos pygame  
pygame.init()

#crear ventana  
screen=pygame.display.set_mode(size) 
screen.fill(color_fondo)

#Titulo 
pygame.display.set_caption("Primer ejercicio pygame")


#Bucle principal  

while True: 
    for event in pygame.event.get(): # decirle a pygame que coja todos los eventos y los recorra 
        if(event.type==pygame.QUIT): 
            sys.exit()
            
        #dibujamos 
        pygame.draw.rect(screen,
                         color_elementos,
                         (200,200,50,50),
                         width=0,
                         border_radius=9,
                         border_top_left_radius=9,
                         border_top_right_radius=0,
                         border_bottom_right_radius=0,
                         border_bottom_left_radius=0, 
                         )
        
        pygame.draw.polygon(screen,
                            color_elementos,
                            [[100,100],[0,200],[200,200]],8)
        
        pygame.draw.line(screen,
                         color_elementos,
                         [400,0],[400,200],
                          4)
        
        pygame.draw.arc(screen, 
                        color_elementos,
                        [210,75,150,125],
                         0,
                         pi/2,
                         10)
        
        pygame.draw.circle(screen,
                           color_elementos,
                           [500,500],
                           90,
                           20, 
                           draw_top_right=True,
                           draw_top_left=True, 
                           draw_bottom_left=True, 
                           draw_bottom_right=True)
        
        pygame.draw.ellipse(screen,
                            color_elementos,
                            [100,500,70,50],
                             8)
        pygame.draw.aaline(screen,
                           color_elementos,
                           [700,0],[700,700],
                           False,
                           )
            
        #disparamos la ventana 
        pygame.display.flip()
        clock.tick(30)