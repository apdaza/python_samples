import random
numero = []

while True:
    cantidad = int(input("ingrese la cantidad de digitos con los que desea jugar"))
    if cantidad in [3,4,5]:
        break
    
while len(numero) < cantidad:
    digito = random.randint(0,9)
    if digito not in numero:
        numero.append(digito)

print(numero)

while True:
    while True:
        intento = input("Ingrese un numero")

        usuario = []
        for i in intento:
            if int(i) not in usuario:
                usuario.append(int(i))

        if len(usuario) != len(numero):
            print("intento no valido")
        else:
            break
        
    fijas = 0
    picas = 0
    for i in range(len(numero)):
        if numero[i] == usuario[i]:
            fijas += 1

    for i in range(len(numero)):
        for j in range(len(usuario)):
            if numero[i] == usuario[j] and i != j:
                picas += 1
            
    print("fijas = " + str(fijas))
    print("picas = " + str(picas))
    if fijas == cantidad:
        print("felicitaciones")
        break
