import pygame
from pygame.sprite import Sprite
from pygame import *


class HeroeRemoto(Sprite):
    instance = None

    def __new__(cls, *args, **kargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls, *args, **kargs)
        return cls.instance

    def __init__(self):
        Sprite.__init__(self)
        self.sentido = 0
        self.cont = 0
        self.velocidad = 10
        self.vida = 100
        self.puntos = 0
        self.walls = []
        self.enemigos = []

    def ubicar(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_sprites(self, sprites):
        self.imagenes = sprites
        self.image = self.imagenes[self.sentido][0]
        self.rect = self.image.get_rect()
        self.rect.move_ip(32, 32)

    def set_mensajes(self, mensajes):
        self.msgs = mensajes
        self.msg = self.msgs[0]

    def getPos(self):
        return (self.rect.x, self.rect.y)

    def update(self,movimiento):
        x = int(movimiento.split(",")[0])
        y = int(movimiento.split(",")[1])
        self.ubicar((x,y))
        
    def draw(self, screen):
        fuente = pygame.font.Font(None, 20)
        texto_heroe = fuente.render(str(self.msg), 1, (200, 200, 50))
        screen.blit(self.image, self.rect)
        screen.blit(texto_heroe, (self.rect.x - 20, self.rect.y - 15))
