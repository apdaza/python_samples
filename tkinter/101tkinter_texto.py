import sys

try:
    import tkinter as tk
except ImportError:
    raise ImportError("Se requiere el modulo Tkinter")

def funcion():
    print("Excelente")

root = tk.Tk()
campo_de_texto = tk.Entry(root)
campo_de_texto.pack()
root.mainloop()
