

class Calculadora:
    def __init__(self):
        self.__valor1 = 0
        self.__valor2 = 0
        self.__resultado = 0

    def sumar(self):
        self.__resultado = self.__valor1 + self.__valor2

    def restar(self):
        self.__resultado = self.__valor1 - self.__valor2

    def multiplicar(self):
        self.__resultado = self.__valor1 * self.__valor2

    def dividir(self):
        self.__resultado = self.__valor1 / self.__valor2

    def get_resultado(self):
        return self.__resultado

    def set_valor1(self, valor):
        self.__valor1 = valor

    def set_valor2(self, valor):
        self.__valor2 = valor
