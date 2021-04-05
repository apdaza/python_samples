import sys
PYTHON_VERSION = sys.version_info.major

if PYTHON_VERSION < 3:
    try:
        import Tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo Tkinter")
else:
    try:
        import tkinter as tk
    except ImportError:
        raise ImportError("Se requiere el modulo tkinter")

def win2():
    tl = tk.Toplevel(root, bg="Orange")
    tl.title("Modificar Datos")
    tl.geometry('600x400')
    tl.focus_set()
    tl.grab_set()
    tl.transient(master=root)

    inf = tk.StringVar(tl)
    entry1 = tk.Entry(tl, textvariable=inf)
    entry1.grid(row=0, column=1)
    label1 = tk.Label(tl, text='Hija', bg="red")
    label1.grid(row=0, column=0)


root = tk.Tk()
root.geometry('200x100')
boton = tk.Button(root, text="Abrir", command=win2).pack()
root.mainloop()
