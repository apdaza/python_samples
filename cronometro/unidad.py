class UnidadDeTiempo:
    def __init__(self, tope = 59):
        self.valor = 0
        self.tope = tope

    def avanzar(self):
        if self.valor < self.tope:
            self.valor += 1
        else:
            self.valor = 0

    def borrar(self):
        self.valor = 0

if __name__ == '__main__':

    u = UnidadDeTiempo(11)

    for i in range(30):
        u.avanzar()
        print(u.valor)

    u.borrar()
    print(u.valor)
