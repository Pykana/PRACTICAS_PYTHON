import pygame
import math

# Inicializar Pygame
pygame.init()

# Configurar pantalla
pantalla = pygame.display.set_mode((600, 400))
pantalla.fill((255, 255, 255))  # Fondo blanco

# Colores
negro = (0, 0, 0)

# Definir la función de la parábola
def parabola(x):
    a = 0.01
    return a * (x - 300) ** 2 + 100  # Centrada en x=300, invertida y arriba en y=100

# Dibujar la parábola
puntos = []
for x in range(0, 600):
    y = parabola(x)
    puntos.append((x, int(y)))

# Conectar los puntos para formar la parábola
for i in range(len(puntos) - 1):
    pygame.draw.line(pantalla, negro, puntos[i], puntos[i + 1], 2)

# Actualizar la pantalla para mostrar el dibujo
pygame.display.flip()

# Mantener la ventana abierta hasta que se cierre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
