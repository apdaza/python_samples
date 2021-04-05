from Tkinter import *
from calculadora import *
from log import *

class InterfazCalculadora():

    def __init__(self):
        color_boton=("gray77")
        color_alerta=("red")
        ancho_boton=11
        alto_boton=3
        self.root = Tk()
        self.root.title("CALCULADORA")
        self.calculadora = Calculadora()
        self.operador = ""

        self.frame = Frame(self.root)
        self.frame.configure(background="SkyBlue4")
        self.frame.pack()

        self.cadena = StringVar()
        self.display = Label(self.frame, textvariable=self.cadena, font=("Helvetica", 30),justify="left",bg="powder blue",width=15)
        self.display.grid(row=0,column=0,columnspan=4,padx=10,pady=10)

        fila = 1
        columna = 0


        Button(self.frame, text="7", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.digito("7")).grid(row=1,column=0)
        Button(self.frame, text="8", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.digito("8")).grid(row=1,column=1)
        Button(self.frame, text="9", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.digito("9")).grid(row=1,column=2)
        Button(self.frame, text="4", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.digito("4")).grid(row=2,column=0)
        Button(self.frame, text="5", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.digito("5")).grid(row=2,column=1)
        Button(self.frame, text="6", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.digito("6")).grid(row=2,column=2)
        Button(self.frame, text="1", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.digito("1")).grid(row=3,column=0)
        Button(self.frame, text="2", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.digito("2")).grid(row=3,column=1)
        Button(self.frame, text="3", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.digito("3")).grid(row=3,column=2)
        Button(self.frame, text="0", bg=color_boton,width=42,height=alto_boton, command = lambda:self.digito("0")).grid(row=4,column=0,columnspan=3)

        Button(self.frame, text="/", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.operacion("/")).grid(row=1,column=3)
        Button(self.frame, text="*", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.operacion("*")).grid(row=2,column=3)
        Button(self.frame, text="-", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.operacion("-")).grid(row=3,column=3)
        Button(self.frame, text="+", bg=color_boton,width=ancho_boton,height=alto_boton, command = lambda:self.operacion("+")).grid(row=4,column=3)
        Button(self.frame, text="C", bg=color_alerta,width=ancho_boton,height=alto_boton, command = lambda:self.operacion("C")).grid(row=5,column=3)
        Button(self.frame, text="=", bg=color_boton,width=42,height=alto_boton, command = lambda:self.operacion("=")).grid(row=5,column=0,columnspan=3)
        self.root.mainloop()

    @save_to_log
    def digito(self, txt):
        self.cadena.set(self.cadena.get()+txt)


    @save_to_log
    def operacion(self, txt):
        if txt in ["+","-","*","/"]:
            self.calculadora.set_valor1(int(self.cadena.get()))
            self.operador = txt
            self.cadena.set("")
        if txt == "=":
            self.calculadora.set_valor2(int(self.cadena.get()))
            if self.operador == "+":
                self.calculadora.sumar()
            if self.operador == "-":
                self.calculadora.restar()
            if self.operador == "/":
                self.calculadora.dividir()
            if self.operador == "*":
                self.calculadora.multiplicar()
            self.cadena.set(self.calculadora.get_resultado())
        if txt == "C":
            self.calculadora.set_valor1(0)
            self.calculadora.set_valor2(0)
            self.cadena.set("")
        

app = InterfazCalculadora()
