import sys

try:
    import Tkinter as tk
except ImportError:
    raise ImportError("Se requiere el modulo Tkinter")

def funcion():
    print("Excelente")

root = tk.Tk()
etiqueta = tk.Label(root, text="Ejemplo simple de Label")
etiqueta.pack()
root.mainloop()
