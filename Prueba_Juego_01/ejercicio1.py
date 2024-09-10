
import pygame # importamos Pygame
pygame.init()  # Inicialización de Pygame
ventana = pygame.display.set_mode((800,600))  # Inicialización de la superficie de dibujo --  TAMAÑO DE VENTANA 
pygame.display.set_caption("Proyecto Prueba") # TITULO DEL JUEGO
jugando = True # variable verificar estado de juego
while jugando: # Bucle principal del juego
    # Comprobamos los eventos
    #Comprobamos si se ha pulsado el botón de cierre de la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Se pinta la ventana con un color
    # Esto borra los posibles elementos que teníamos anteriormente
    ventana.fill((255, 255, 255))
    # Todos los elementos del juego se vuelven a dibujar
    pygame.display.flip()
    # Controlamos la frecuencia de refresco (FPS)
    pygame.time.Clock().tick(60)
pygame.quit()