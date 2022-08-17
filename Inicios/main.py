import pygame            #importamos la libreria 
import sys  

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
            
        #disparamos la ventana 
        pygame.display.flip()
        clock.tick(30)