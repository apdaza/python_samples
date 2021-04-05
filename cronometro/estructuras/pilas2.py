class Nodo:
    def __init__(self, valor, anterior = None):
        self.valor = valor
        self.anterior = anterior

def apilar(pila, elemento):
    if pila == None:
        pila = elemento
    else:
        elemento.anterior = pila
        pila = elemento
    return pila

def desapilar(pila):
    if pila == None:
        elemento = None
    else:
        elemento = pila.valor
        pila = pila.anterior
    return elemento, pila

def mostrar_pila(pila):
    if pila == None:
        pass
    else:
        print(pila.valor) 
        mostrar_pila(pila.anterior)   

pila = None

pila = apilar(pila, Nodo(5))
pila = apilar(pila, Nodo(2))
pila = apilar(pila, Nodo(15))
pila = apilar(pila, Nodo(8))

mostrar_pila(pila)
print("Desapilando elementos:")
elemento, pila = desapilar(pila)
print(elemento)
elemento, pila = desapilar(pila)
print(elemento)

print("pila:")
mostrar_pila(pila)