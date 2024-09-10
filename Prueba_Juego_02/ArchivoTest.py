
import pygame, sys
from pygame.locals import *

pygame.init()  # Inicializar pygame
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))  # Tamaño de la ventana
titulo = 'Test Game'  # Declarar título
icono = pygame.image.load("Sprites/Icon/GameIcon.png")  # Declarar icono
fondo = pygame.image.load("Assets/Background/City1/Bright/City1(800x600).png").convert()  # Para fondo dinámico
FPS = 60
reloj = pygame.time.Clock()

pygame.display.set_caption(titulo)  # Setear Título
pygame.display.set_icon(icono)  # Setear Icono

SoldadoQuieto = [pygame.image.load("Sprites/Soldier/EnEspera/idle1.png"),
                 pygame.image.load("Sprites/Soldier/EnEspera/idle2.png"),
                 pygame.image.load("Sprites/Soldier/EnEspera/idle3.png"),
                 pygame.image.load("Sprites/Soldier/EnEspera/idle4.png"),
                 pygame.image.load("Sprites/Soldier/EnEspera/idle5.png"),
                 pygame.image.load("Sprites/Soldier/EnEspera/idle6.png")]

SoldadoCaminarDerecha = [pygame.image.load("Sprites/Soldier/Caminar/caminar1.png"),
                         pygame.image.load("Sprites/Soldier/Caminar/caminar2.png"),
                         pygame.image.load("Sprites/Soldier/Caminar/caminar3.png"),
                         pygame.image.load("Sprites/Soldier/Caminar/caminar4.png"),
                         pygame.image.load("Sprites/Soldier/Caminar/caminar5.png"),
                         pygame.image.load("Sprites/Soldier/Caminar/caminar6.png"),
                         pygame.image.load("Sprites/Soldier/Caminar/caminar7.png")]

SoldadoCaminarIzquierda = [pygame.transform.flip(imagen, True, False) for imagen in SoldadoCaminarDerecha]

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)

H0x00E61290 = (144, 18, 230)
H0x001E6EDD = (144, 18, 230)

xFondo = 0
YFondo = 0

XPersonaje = 300
YPersonaje = 400

# Movimiento
VelocidadMovimiento = 10
MoverIzquierda = False
MoverDerecha = False

# Pasos
CuentaPasos = 0


def RecargarPantalla():
    global CuentaPasos
    global xFondo
    global YFondo

    Xrelativa = xFondo % fondo.get_rect().width
    pantalla.blit(fondo, (Xrelativa - fondo.get_rect().width, YFondo))
    if Xrelativa < ANCHO:
        pantalla.blit(fondo, (Xrelativa, YFondo))
    xFondo -= 1

    if CuentaPasos + 1 >= 7:
        CuentaPasos = 0

    if MoverIzquierda:
        pantalla.blit(SoldadoCaminarIzquierda[CuentaPasos // 1], (int(XPersonaje), int(YPersonaje)))
        CuentaPasos += 1
    elif MoverDerecha:
        pantalla.blit(SoldadoCaminarDerecha[CuentaPasos // 1], (int(XPersonaje), int(YPersonaje)))
        CuentaPasos += 1
    else:
        pantalla.blit(SoldadoQuieto[CuentaPasos // 1], (int(XPersonaje), int(YPersonaje)))
        CuentaPasos += 1


JuegoActivo = True

while JuegoActivo:
    reloj.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            JuegoActivo = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and XPersonaje > VelocidadMovimiento:
        XPersonaje -= VelocidadMovimiento
        MoverIzquierda = True
        MoverDerecha = False
    elif keys[pygame.K_d] and XPersonaje < ANCHO - VelocidadMovimiento:
        XPersonaje += VelocidadMovimiento
        MoverIzquierda = False
        MoverDerecha = True
    else:
        MoverIzquierda = False
        MoverDerecha = False

    pygame.display.update()
    RecargarPantalla()


pygame.quit()
