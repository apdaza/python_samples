from random import *

def crear_lista(tam):
    lista = []
    for i in range(tam):
        lista.append(randint(0,100))
    return lista


def verificar(lista, valor):
    if valor in lista:
        return True
    else:
        return False

def jugar(n, lista):
    bandera = False
    for i in range(n):
        if verificar(lista,input("ingrese un valor")):
            print "ganaste"
            bandera = True
            break
        else:
            print "lo siento"

    if bandera == False:
        print "los valores de la lista son:"
        print lista
