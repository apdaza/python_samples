# -*- coding: utf-8 -*-
import tkinter as tk

import Punto as pt

class FormularioDistancia:
    def __init__(self):
        self.punto1=pt.Punto()
        self.punto2=pt.Punto()
        self.ventana1=tk.Tk()
        self.ventana1.geometry("800x600")
        self.ventana1.title("Distancias")

        self.labelframe1=tk.LabelFrame(self.ventana1, text="Punto 1:")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=tk.Label(self.labelframe1, text="x1:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=tk.Entry(self.labelframe1, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2=tk.Label(self.labelframe1, text="y1:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.x1=tk.StringVar()
        self.entryx1=tk.Entry(self.labelframe1, textvariable=self.x1)
        self.entryx1.grid(column=1, row=1, padx=4, pady=4)

        self.labelframe2=tk.LabelFrame(self.ventana1, text="Punto 2:")
        self.labelframe2.grid(column=1, row=0, padx=5, pady=10)
        self.label1=tk.Label(self.labelframe2, text="x1:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=tk.Entry(self.labelframe2, textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1, row=0, padx=4, pady=4)
        self.label2=tk.Label(self.labelframe2, text="y1:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.x1=tk.StringVar()
        self.entryx1=tk.Entry(self.labelframe2, textvariable=self.x1)
        self.entryx1.grid(column=1, row=1, padx=4, pady=4)

        self.boton1=tk.Button(self.ventana1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

        self.ventana1.mainloop()


    def calcular(self):
        p1 = Punto()
        p1.setX(int(self.x1))
        p1.setY(int(self.y1))

        p2 = Punto()
        p2.setX(int(self.x2))
        p2.setY(int(self.y2))

        distancia = p1.calcular_distancia(p2)
        



aplicacion1=FormularioDistancia()
