from random import randint

def generar_numero(tam):
    aleatorio = []
    while len(aleatorio)<tam:
        n = randint(1,9)
        if n not in aleatorio:
            aleatorio.append(n)
    return aleatorio

def contar_picas(a, n):
    cont = 0
    for i in range(len(n)):
        if n[i] in a and n[i] != a[i]:
            cont += 1
    return cont

def contar_fijas(a, n):
    cont = 0
    for i in range(len(n)):
        if n[i] in a and n[i] == a[i]:
            cont += 1
    return cont

aleatorio = generar_numero(3)
print aleatorio
intentos = 0
matriz = []
while intentos < 5:
    numero = [int(x) for x in list(raw_input("ingrese un numero: "))]

    if len(numero) != len(aleatorio):
        print "numero no valido"
        intentos -= 1
    else:
        matriz.append([numero,contar_picas(aleatorio, numero),contar_fijas(aleatorio, numero)])
        if numero == aleatorio:
            print "picas: 0, fijas: 3 - > gana"
            break
        else:
            print "picas = " + str(contar_picas(aleatorio, numero))
            print "fijas = " + str(contar_fijas(aleatorio, numero))
        
    intentos += 1

for i in matriz:
    print "para " + str(i[0]) + " picas = " + str(i[1]) + " fijas = " + str(i[2])
