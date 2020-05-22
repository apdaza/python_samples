#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Arma(ABC):
    def retornar_info(self):
        return self.imagen, self.descripcion

class ArmaBarbaro(Arma):
    def __init__(self):
        self.imagen = "imagenes/barbaros/arma.png"
        self.descripcion = "arma de los barbaros"

class ArmaElfo(Arma):
    def __init__(self):
        self.imagen = "imagenes/elfos/arma.png"
        self.descripcion = "arma de los elfos"

class ArmaEnano(Arma):
    def __init__(self):
        self.imagen = "imagenes/enanos/arma.png"
        self.descripcion = "arma de los enanos"

class ArmaMago(Arma):
    def __init__(self):
        self.imagen = "imagenes/magos/arma.png"
        self.descripcion = "arma de los magos"

class Montura(ABC):
    def retornar_info(self):
        return self.imagen, self.descripcion

class MonturaBarbaro(Montura):
    def __init__(self):
        self.imagen = "imagenes/barbaros/montura.png"
        self.descripcion = "montura de los barbaros"

class MonturaElfo(Montura):
    def __init__(self):
        self.imagen = "imagenes/elfos/montura.png"
        self.descripcion = "montura de los elfos"

class MonturaEnano(Montura):
    def __init__(self):
        self.imagen = "imagenes/enanos/montura.png"
        self.descripcion = "montura de los enanos"

class MonturaMago(Montura):
    def __init__(self):
        self.imagen = "imagenes/magos/montura.png"
        self.descripcion = "montura de los magos"

class Escudo(ABC):
    def retornar_info(self):
        return self.imagen, self.descripcion

class EscudoBarbaro(Escudo):
    def __init__(self):
        self.imagen = "imagenes/barbaros/escudo.png"
        self.descripcion = "escudo de los barbaros"

class EscudoElfo(Escudo):
    def __init__(self):
        self.imagen = "imagenes/elfos/escudo.png"
        self.descripcion = "escudo de los elfos"

class EscudoEnano(Escudo):
    def __init__(self):
        self.imagen = "imagenes/enanos/escudo.png"
        self.descripcion = "escudo de los enanos"

class EscudoMago(Escudo):
    def __init__(self):
        self.imagen = "imagenes/magos/escudo.png"
        self.descripcion = "escudo de los magos"
