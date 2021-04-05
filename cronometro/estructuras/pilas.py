pila = []

def apilar(pila, elemento):
    pila.append(elemento)

def desapilar(pila):
    return pila.pop()

print("Apilando elementos:")
print(pila)
apilar(pila, 5)
apilar(pila, 2)
apilar(pila, 15)
apilar(pila, 8)
print(pila)

print("Desapilando elementos:")
print(pila)
print(desapilar(pila))
print(desapilar(pila))
print(desapilar(pila))
print(desapilar(pila))
print(pila)
