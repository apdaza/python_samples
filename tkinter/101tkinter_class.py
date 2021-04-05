import sys

try:
    import tkinter as tk
except ImportError:
    raise ImportError("Se requiere el modulo Tkinter")

class UI(tk.Frame):
    """Docstring."""
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """Aqui colocariamos los widgets."""
        self.parent.title("Un titulo para la ventana")

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("800x600")
    APP = UI(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()
