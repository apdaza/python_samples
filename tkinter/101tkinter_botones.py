import sys

try:
    import Tkinter as tk
except ImportError:
    raise ImportError("Se requiere el modulo Tkinter")

foreground = "red"
background = "blue"
activeforeground = "green"
activebackground = "black"
disabledforeground = "white"

root = tk.Tk()
root.geometry("300x100")
boton_normal = tk.Button(root, text="normal", state="normal",
                        foreground=foreground,
                        background=background,
                        activeforeground=activeforeground,
                        activebackground=activebackground,
                        disabledforeground=disabledforeground).pack()
boton_active = tk.Button(root, text="active", state="active",
                        foreground=foreground,
                        background=background,
                        activeforeground=activeforeground,
                        activebackground=activebackground,
                        disabledforeground=disabledforeground).pack()
boton_disabled = tk.Button(root, text="disabled", state="disabled",
                        foreground=foreground,
                        background=background,
                        activeforeground=activeforeground,
                        activebackground=activebackground,
                        disabledforeground=disabledforeground).pack()

root.mainloop()

root = tk.Tk()
