import sys

try:
    import Tkinter as tk
except ImportError:
    raise ImportError("Se requiere el modulo Tkinter")

def funcion():
    print("Excelente")

root = tk.Tk()
boton = tk.Button(root, text="Que te parece el ejemplo?", command=funcion)
boton.pack()
root.mainloop()
