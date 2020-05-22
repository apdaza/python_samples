#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fabricas import *

def prueba():
    fabrica = FabricaBarbaros()
    arma = fabrica.crear_arma()
    escudo = fabrica.crear_escudo()
    montura = fabrica.crear_montura()

    print(montura.retornar_info())
    print(escudo.retornar_info())
    print(arma.retornar_info())


if __name__ == '__main__':
    prueba()
