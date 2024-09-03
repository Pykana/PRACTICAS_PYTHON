import pygame, sys    
from pygame.locals import *

pygame.init() #inicializar pygame 

pantalla = pygame.display.set_mode((800,600)) #tamaño ventana
titulo = 'Titulo Juego' #declarar titulo
icono = pygame.image.load("Prueba_04/ball.png") #declarar icono

pygame.display.set_caption(titulo) # setear Titulo 
pygame.display.set_icon(icono)  # setear Icono


#colores

blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)

pantalla.fill(blanco) # cambiar color de fondo de pantalla  -- por defecto en negro

#figuras

reactangulo1 = pygame.draw.rect(pantalla, rojo,(100,100 , 100, 50)) #  crear rectangulo para usar en pantalla , parametros = ( (donde se dibuja), (color), (coordenada x ,coordenada y , largo , alto))

# (100, 100, 100, 50): Este es un conjunto de cuatro valores que define el área y posición del rectángulo:
# 100: Coordenada X de la esquina superior izquierda del rectángulo.
# 100: Coordenada Y de la esquina superior izquierda del rectángulo.
# 100: Ancho del rectángulo.
# 50: Alto del rectángulo.

linea = pygame.draw.line(pantalla,verde, (200, 150), (250, 150), 5) # crear linea para usar en pantalla

# pantalla: Igual que antes, es la superficie de destino donde se dibuja la línea.
# verde: Es el color de la línea, que también debe ser definido como una tupla RGB, por ejemplo, verde = (0, 255, 0).
# (100, 104): Esta es la coordenada X e Y del punto inicial de la línea.
# (199, 104): Esta es la coordenada X e Y del punto final de la línea.
# 10: Este es el grosor de la línea en píxeles.

circulo = pygame.draw.circle(pantalla, azul, (300, 150), 75, 5)  # crear circulo para usar en pantalla

# pygame.draw.line(superficie, color, punto_inicial, punto_final, grosor)
# superficie: Dónde dibujar la línea (por ejemplo, la ventana principal).
# color: El color de la línea.
# punto_inicial: Coordenadas (x, y) de donde comienza la línea.
# punto_final: Coordenadas (x, y) de donde termina la línea.
# grosor: El grosor de la línea en píxeles.

print(reactangulo1) # dibujar rectangulo en pantalla
print(linea) # dibujar linea en pantalla
print(circulo) # dibujar linea en pantalla

while True:  #buble de juego
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() # actualizar frames en pantalla
