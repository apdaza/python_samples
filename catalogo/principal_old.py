import sys
import pygame
import util
from pygame.locals import *
from random import *
from fabricas import *

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 800

def game():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Catalogo de personajes")
    background_image = util.cargar_imagen('imagenes/fondo.jpg')
    pygame.mouse.set_visible(False)

    contador = 0
    ejecutando = True

    fabrica = FabricaEnanos()
    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()
    montura = fabrica.crear_montura()

    montura.ubicar((50,30))
    escudo.ubicar((50,300))
    arma.ubicar((50,600))

    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
                sys.exit()
        teclas = pygame.key.get_pressed()

        if teclas[K_b]:
            fabrica = FabricaBarbaros()
        if teclas[K_e]:
            fabrica = FabricaEnanos()
        if teclas[K_m]:
            fabrica = FabricaMagos()
        if teclas[K_f]:
            fabrica = FabricaElfos()

        arma = fabrica.crear_arma()
        escudo = fabrica.crear_escudo()
        montura = fabrica.crear_montura()
        montura.ubicar((50,30))
        escudo.ubicar((50,300))
        arma.ubicar((50,600))

        screen.blit(background_image, (0, 0))
        montura.dibujar(screen)
        escudo.dibujar(screen)
        arma.dibujar(screen)

        pygame.display.update()
        pygame.time.delay(10)


if __name__ == '__main__':
    game()
