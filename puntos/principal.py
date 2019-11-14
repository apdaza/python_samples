from Punto import *

puntos = []
while True:
    opc = raw_input("desea capturar un punto: s-n ")
    if opc == 'n':
        break
    else:
        x = input("valor de x: ")
        y = input("valor de y: ")
        puntos.append(Punto())
        puntos[-1].setX(x)
        puntos[-1].setY(y)

distancia_total = 0
for x in range(len(puntos)):
    #puntos[x].mostrar()
    if puntos[x] != puntos[-1]:
        distancia_total += puntos[x].calcular_distancia(puntos[x+1])

print "la distancia total es: " + str(distancia_total)

menor = puntos[0].calcular_distancia(puntos[-1])
cercano = puntos[0]
for x in range(len(puntos)):
    #puntos[x].mostrar()
    if puntos[x] != puntos[-1]:
        distancia = puntos[x].calcular_distancia(puntos[-1])
        print "la distancia de p" + str(x+1) + " a p" + str(len(puntos)) + " es: " + str(distancia)
        if distancia < menor:
            menor = distancia
            cercano = puntos[x]

print "el punto mas cercano es: " + str(cercano.mostrar())
