import pygame, sys    
from pygame.locals import *

pygame.init() #inicializar pygame 

pantalla = pygame.display.set_mode((800,600)) #tamaño ventana
titulo = 'Test Game' #declarar titulo
icono = pygame.image.load("Sprites/Icon/GameIcon.png") #declarar icono
fondo = pygame.image.load("Assets/Background/City1/Bright/City1(800x600).png")

pygame.display.set_caption(titulo) # setear Titulo 
pygame.display.set_icon(icono)  # setear Icono

#colores

blanco = (255,255,255)
negro = (0,0,0)
rojo = (255,0,0)
azul = (0,0,255)
verde = (0,255,0)

H0x00E61290 = (144,18,230)
H0x001E6EDD = (144,18,230)

pantalla.fill(blanco) # cambiar color de fondo de pantalla  -- por defecto en negro
# pantalla.blit(fondo,(0,0))

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
circulo2 = pygame.draw.circle(pantalla, azul, (500, 150), 75, 5)  # crear circulo para usar en pantalla

# pygame.draw.line(superficie, color, punto_inicial, punto_final, grosor)
# superficie: Dónde dibujar la línea (por ejemplo, la ventana principal).
# color: El color de la línea.
# punto_inicial: Coordenadas (x, y) de donde comienza la línea.
# punto_final: Coordenadas (x, y) de donde termina la línea.
# grosor: El grosor de la línea en píxeles.

ellipse = pygame.draw.ellipse(pantalla,H0x00E61290, (275,200,40,80),5)

#Pantalla
#Color
#Primeros dos puntos , donde estara el punto central
#Dos ultimos Puntos, dimensiones en X , Y del elipce
#Grosor

puntosPolygon= [(100,150),(100,200),(150,200)] #Puntos para el poligono a crear
poligono = pygame.draw.polygon(pantalla,H0x001E6EDD,puntosPolygon,5) #Crear Poligono

#Pantalla
#Color
#Puntos a crear
#Grosor

print(reactangulo1) # dibujar rectangulo en pantalla
print(linea) # dibujar linea en pantalla
print(circulo) # dibujar circulo en pantalla
print(circulo2) # dibujar circulo2 en pantalla
print(ellipse) # dibujar elipce en pantalla
print(poligono) # dibujar elipce en pantalla

while True:  #buble de juego
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update() # actualizar frames en pantalla