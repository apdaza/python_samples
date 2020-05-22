#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from fabricas import *

app = Flask(__name__)

@app.route('/')
def principal():
   fabrica = FabricaBarbaros()
   arma = fabrica.crear_arma()
   escudo = fabrica.crear_escudo()
   montura = fabrica.crear_montura()

   lista = []

   lista.append(montura.retornar_info())
   lista.append(escudo.retornar_info())
   lista.append(arma.retornar_info())
   return render_template('showall.html', msg = "products loaded successfully", rows = lista)

if __name__ == '__main__':
   app.run(debug = True)
