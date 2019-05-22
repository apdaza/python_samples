from pygame.sprite import Sprite
from pygame import *
from util import *

FONT_SIZE = 30
class Arma(Sprite):
    def ubicar(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def dibujar(self, screen):
        fuente = font.Font(None, FONT_SIZE)
        texto = fuente.render(str(self.descripcion), 1, (20, 20, 50))
        screen.blit(self.imagen, self.rect)
        screen.blit(texto, (self.rect.x - 20, self.rect.y - 15))

class ArmaBarbaro(Arma):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/barbaros/arma.png")
        self.descripcion = "arma de los barbaros"
        self.rect = self.imagen.get_rect()

class ArmaElfo(Arma):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/elfos/arma.png")
        self.descripcion = "arma de los elfos"
        self.rect = self.imagen.get_rect()

class ArmaEnano(Arma):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/enanos/arma.png")
        self.descripcion = "arma de los enanos"
        self.rect = self.imagen.get_rect()

class ArmaMago(Arma):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/magos/arma.png")
        self.descripcion = "arma de los magos"
        self.rect = self.imagen.get_rect()

class Montura():
    def ubicar(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def dibujar(self, screen):
        fuente = pygame.font.Font(None, FONT_SIZE)
        texto = fuente.render(str(self.descripcion), 1, (20, 20, 50))
        screen.blit(self.imagen, self.rect)
        screen.blit(texto, (self.rect.x - 20, self.rect.y - 15))

class MonturaBarbaro(Montura):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/barbaros/montura.png")
        self.descripcion = "montura de los barbaros"
        self.rect = self.imagen.get_rect()

class MonturaElfo(Montura):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/elfos/montura.png")
        self.descripcion = "montura de los elfos"
        self.rect = self.imagen.get_rect()

class MonturaEnano(Montura):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/enanos/montura.png")
        self.descripcion = "montura de los enanos"
        self.rect = self.imagen.get_rect()

class MonturaMago(Montura):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/magos/montura.png")
        self.descripcion = "montura de los magos"
        self.rect = self.imagen.get_rect()

class Escudo():
    def ubicar(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def dibujar(self, screen):
        fuente = pygame.font.Font(None, FONT_SIZE)
        texto = fuente.render(str(self.descripcion), 1, (20, 20, 50))
        screen.blit(self.imagen, self.rect)
        screen.blit(texto, (self.rect.x - 20, self.rect.y - 15))

class EscudoBarbaro(Escudo):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/barbaros/escudo.png")
        self.descripcion = "escudo de los barbaros"
        self.rect = self.imagen.get_rect()

class EscudoElfo(Escudo):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/elfos/escudo.png")
        self.descripcion = "escudo de los elfos"
        self.rect = self.imagen.get_rect()

class EscudoEnano(Escudo):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/enanos/escudo.png")
        self.descripcion = "escudo de los enanos"
        self.rect = self.imagen.get_rect()

class EscudoMago(Escudo):
    def __init__(self):
        self.imagen = cargar_imagen("imagenes/magos/escudo.png")
        self.descripcion = "escudo de los magos"
        self.rect = self.imagen.get_rect()
