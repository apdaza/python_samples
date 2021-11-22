from calculadora import Calculadora

class TestCalculadora:
    def test_suma(self):
        calculadora = Calculadora()
        assert 5 == calculadora.sumar(3, 2)

    def test_resta(self):
        calculadora = Calculadora()
        assert 3 == calculadora.restar(5, 2)

    def test_producto(self):
        calculadora = Calculadora()
        assert 15 == calculadora.multiplicar(5, 3)

    def test_division(self):
        calculadora = Calculadora()
        assert 5 == calculadora.dividir(10, 2)