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


SoldadoQuieto= [pygame.image.load("Sprites/Soldier/EnEspera/idle1.png"),
               pygame.image.load("Sprites/Soldier/EnEspera/idle2.png"),
               pygame.image.load("Sprites/Soldier/EnEspera/idle3.png"),
               pygame.image.load("Sprites/Soldier/EnEspera/idle4.png"),
               pygame.image.load("Sprites/Soldier/EnEspera/idle5.png"),
               pygame.image.load("Sprites/Soldier/EnEspera/idle6.png")]

SoldadoCaminarDerecha=[pygame.image.load("Sprites/Soldier/Caminar/caminar1.png"),
               pygame.image.load("Sprites/Soldier/Caminar/caminar2.png"),
               pygame.image.load("Sprites/Soldier/Caminar/caminar3.png"),
               pygame.image.load("Sprites/Soldier/Caminar/caminar4.png"),
               pygame.image.load("Sprites/Soldier/Caminar/caminar5.png"),
               pygame.image.load("Sprites/Soldier/Caminar/caminar6.png")]

SoldadoCaminarIzquierda = [pygame.transform.flip(imagen, True, False) for imagen in SoldadoCaminarDerecha] # Invertir la iamgen de la lista de caminar Derecha

# pygame.transform.flip(imagen, True, False): Invierte la imagen horizontalmente.
# Primer parámetro (True): Indica que la imagen debe ser volteada horizontalmente.
# Segundo parámetro (False): Indica que la imagen no debe ser volteada verticalmente.
# List comprehension: Este método recorre cada imagen en SoldadoCaminarDerecha y aplica la transformación para crear la lista SoldadoCaminarIzquierda.

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

XPersonaje = 350
YPersonaje = 400

#Movimiento
VelocidadMovimiento =5
MoverIzquierda = False
MoverDerecha = False

#Pasos
CuentaPasos =0


def RecargarPantalla():
    # Variables Globales

    global CuentaPasos
    global xFondo
    global YFondo

    #Fondo Dinamico

    Xrelativa = xFondo % fondo.get_rect().width  # Obtener el ancho del fondo y dividirlo entre Movimiento de fondo
    pantalla.blit(fondo, (Xrelativa - fondo.get_rect().width, YFondo))
    if Xrelativa < ANCHO:
        pantalla.blit(fondo, (Xrelativa, YFondo))
    xFondo -= 1  # Movimiento Dinamico en X para el fondo

    if CuentaPasos + 1 >= 6:
        CuentaPasos = 0

    # Movimiento a la izquierda
    if MoverIzquierda:
        pantalla.blit(SoldadoCaminarIzquierda[CuentaPasos // 3], (int(XPersonaje), int(YPersonaje)))
        CuentaPasos += 1
    # Movimiento a la derecha
    elif MoverDerecha:
        pantalla.blit(SoldadoCaminarDerecha[CuentaPasos // 3], (int(XPersonaje), int(YPersonaje)))
        CuentaPasos += 1
    else: # Quieto
        pantalla.blit(SoldadoQuieto[0], (int(XPersonaje), int(YPersonaje)))  # Usar la primera imagen de la lista cuando el personaje está quieto


JuegoActivo = True

while JuegoActivo:
    reloj.tick(FPS)  # Control FPS

    for event in pygame.event.get():
        if event.type == QUIT:
            JuegoActivo = False

    #Opcion Tecla Pulsada
    keys= pygame.key.get_pressed()

    # Tecla A - Moviemiento a la izquierda
    if keys[pygame.K_a] and XPersonaje > VelocidadMovimiento:
        XPersonaje -= VelocidadMovimiento
        MoverIzquierda = True
        MoverDerecha = False

    # Tecla D - Moviemiento a la derecha
    elif keys[pygame.K_d] and XPersonaje < ANCHO - VelocidadMovimiento:
        XPersonaje += VelocidadMovimiento
        MoverIzquierda = False
        MoverDerecha = True


    # Personaje quieto
    else:
        MoverIzquierda = False
        MoverDerecha = False
        CuentaPasos = 0

    pygame.display.update() # actualizar frames en pantalla
    RecargarPantalla()

pygame.quit()