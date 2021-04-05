class Nodo:
    def __init__(self, valor, siguiente = None):
        self.valor = valor
        self.siguiente = siguiente

def encolar(cola, elemento):
    if cola == None:
        cola = elemento
    else:
        aux = cola
        while cola.siguiente != None:
            cola = cola.siguiente
        cola.siguiente = elemento
        cola = aux
    return cola

def desencolar(cola):
    if cola == None:
        elemento = None
    else:
        elemento = cola.valor
        cola = cola.siguiente
    return elemento, cola

def mostrar_cola(cola):
    if cola == None:
        pass
    else:
        print(cola.valor) 
        mostrar_cola(cola.siguiente)   

cola = None

cola = encolar(cola, Nodo(5))
cola = encolar(cola, Nodo(2))
cola = encolar(cola, Nodo(15))
cola = encolar(cola, Nodo(8))
cola = encolar(cola, Nodo(16))
cola = encolar(cola, Nodo(28))

mostrar_cola(cola)

print("desencolando elementos:")
elemento, cola = desencolar(cola)
print(elemento)
elemento, cola = desencolar(cola)
print(elemento)
print("quedan en cola")
mostrar_cola(cola)