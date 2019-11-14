from tkinter import *

class AppHolaMundo:

    def __init__(self, myParent):
        self.frame = Frame(myParent)
        self.frame.pack()

        self.label = Label(self.frame, text="Mi primer frame en tk")
        self.label.pack()

        self.cadena = StringVar()
        self.text = Entry(self.frame, textvariable=self.cadena)
        self.text.pack(side=LEFT)

        self.button = Button(self.frame, text="Aceptar")
        self.button.bind("<Button-1>", self.saludo)
        self.button.pack(side=RIGHT)

    def saludo(self, event):
        if self.cadena.get() != "":
            self.cadena.set("Hola " + self.cadena.get())
        else:
            self.cadena.set("Ingresa el nombre, por favor")


root = Tk()
app = AppHolaMundo(root)
root.mainloop()
