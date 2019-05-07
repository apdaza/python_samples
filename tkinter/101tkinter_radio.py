import sys

try:
    import Tkinter as tk
except ImportError:
    raise ImportError("Se requiere el modulo Tkinter")

def prueba():
    print("Se ha elegido la opcion" + variable.get())

root = tk.Tk()
variable = tk.StringVar()
radiobutton1 = tk.Radiobutton(text="Opcion 1", variable=variable, value=1, command=prueba, activebackground="#555555", activeforeground="#AAAAAA")
radiobutton2 = tk.Radiobutton(text="Opcion 2", variable=variable, value=2, command=prueba, activebackground="#555555", activeforeground="#AAAAAA")
radiobutton3 = tk.Radiobutton(text="Opcion 3", variable=variable, value=3, command=prueba, activebackground="#555555", activeforeground="#AAAAAA")
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
root.mainloop()
