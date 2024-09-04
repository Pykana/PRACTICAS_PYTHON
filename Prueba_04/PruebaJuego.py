import pygame, sys
from pygame.locals import *

pygame.init() #inicializar pygame 
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO,ALTO)) #tamaño ventana
titulo = 'Test Game' #declarar titulo
icono = pygame.image.load("Sprites/Icon/GameIcon.png") #declarar icono
fondo = pygame.image.load("Assets/Background/City1/Bright/City1(800x600).png").convert() #para fondo dinamico
FPS= 60
reloj= pygame.time.Clock()

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

xFondo=0
YFondo=0

while True:  #buble de juego
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    Xrelativa = xFondo % fondo.get_rect().width  # Obtener el ancho del fondo y dividirlo entre Movimiento de fondo
    pantalla.blit(fondo, (Xrelativa - fondo.get_rect().width, YFondo))

    if Xrelativa < ANCHO:
        pantalla.blit(fondo,(Xrelativa,YFondo))

    xFondo-=1 #Movimiento Dinamico en X para el fondo
    reloj.tick(FPS)#Control FPS
    pygame.display.update() # actualizar frames en pantalla
