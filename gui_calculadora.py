import calculadora as calc

c = calc.Calculadora()
c2 = calc.Calculadora2()
n1 = input("Ingrese el valor 1")
n2 = input("Ingrese el valor 2")

c.setValor1(n1)
c.setValor2(n2)
c2.setValor1(n1)
c2.setValor2(n2)

c.sumar()
c2.restar()
print (c.getResultado())
print (c2.getResultado())
