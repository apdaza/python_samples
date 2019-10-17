numero = int(input("ingrese un numero a validar: "))

dias = ["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]

if numero < 1 or numero > 7:
    print("el numero no es un dia valido")
else:
    print("el numero corresponde a " + dias[numero - 1])
