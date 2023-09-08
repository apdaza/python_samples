from tkinter import *
from cronometro import Cronometro
from threading import *
from time import sleep

class AppCronometro(Thread):

    def __init__(self):
        self.principal = Tk()
        self.crono = Cronometro()
        self.frame = Frame(self.principal)
        self.frame.pack()

        self.valor = StringVar()
        self.display = Label(self.frame, textvariable = self.valor, font = ('Helvetica', 20))
        self.display.pack(side=TOP)

        self.boton_iniciar = Button(self.frame, text = 'Iniciar/Parar', command = self.cambiar_estado)
        self.boton_iniciar.pack(side=LEFT)

        self.boton_borrar = Button(self.frame, text = 'Borrar', command = self.borrar)
        self.boton_borrar.pack(side=RIGHT)

        self.image = PhotoImage(file="crono.png")
        self.icono = Label(image = self.image)
        self.icono.pack(side=BOTTOM)

        Thread.__init__(self)
        self.start()

        self.principal.mainloop()

    def cambiar_estado(self):
        self.crono.cambiar_estado()

    def borrar(self):
        self.crono.borrar()

    def run(self):
        while True:
            if not self.crono.parado:
                self.crono.avanzar()
                sleep(0.1)
            self.valor.set(self.crono.retornar_tiempo())

    def callback(self):
        print("Hola")
        self.principal.quit()

if __name__ == '__main__':
    app = AppCronometro()
