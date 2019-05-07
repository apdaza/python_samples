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

root = tk.Tk()
root.mainloop()
