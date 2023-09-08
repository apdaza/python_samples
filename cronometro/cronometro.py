from unidad import UnidadDeTiempo

class Cronometro:
    def __init__(self):
        self.hora = UnidadDeTiempo(23)
        self.minuto = UnidadDeTiempo()
        self.segundo = UnidadDeTiempo()

        self.parado = True

    def avanzar(self):
        self.segundo.avanzar()
        if self.segundo.valor == 0:
            self.minuto.avanzar()
            if self.minuto.valor == 0:
                self.hora.avanzar()

    def borrar(self):
        self.hora.borrar()
        self.minuto.borrar()
        self.segundo.borrar()

        self.parado = True

    def cambiar_estado(self):
        self.parado = not self.parado

    def retornar_tiempo(self):
        return "{:02d}:{:02d}:{:02d}".format(self.hora.valor,
                                             self.minuto.valor,
                                             self.segundo.valor)
if __name__ == '__main__':
    c = Cronometro()

    for i in range(100):
        c.avanzar()
        print(c.retornar_tiempo())



    
