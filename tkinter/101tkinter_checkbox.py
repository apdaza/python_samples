import sys

try:
    import Tkinter as tk
except ImportError:
    raise ImportError("Se requiere el modulo Tkinter")

def funcion():
    print int_var.get()

root = tk.Tk()
int_var = tk.IntVar()
check = tk.Checkbutton(root, text="Probando", variable=int_var, command=funcion, cursor="hand2")
check.pack()
root.mainloop()
