import pygame
pygame.init() # inicualizar pygame

ventana = pygame.display.set_mode((640,480))  # tamaño de ventana

pygame.display.set_caption("ejercicio 2")  # titulo del juego

ball = pygame.image.load("Assets/ball.png") # Crea el objeto pelota  # ball = pygame.image.load("ball.png") -- bola usando la imagen png

ballrect = ball.get_rect() # Obtengo el rectángulo del objeto anterior --- para la bola creada

# Inicializo los valores con los que se van a mover la pelota

speed = [5,5]  #Inicializamos una lista con dos valores, que llamamos speed. 
               #El primer valor representa el desplazamiento horizontal, y el segundo el desplazamiento vertical. 
               #Lo utilizaremos para mover la pelota.

ballrect.move_ip(0,0)  # Pongo la pelota en el origen de coordenadas

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    # Muevo la pelota
    ballrect = ballrect.move(speed)
    # Compruebo si la pelota llega a los límites de la ventana
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
            
    if ballrect.top < 0 or ballrect.bottom > ventana.get_height():
        speed[1] = -speed[1]
    
    ventana.fill((252, 243, 207))
    # Dibujo la pelota
    ventana.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
    
pygame.quit()# salir  pygame