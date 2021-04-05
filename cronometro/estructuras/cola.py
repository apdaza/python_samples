cola = []

def encolar(cola, elemento):
    cola.append(elemento)

def desencolar(cola):
    return cola.pop(0)

print("Encolando elementos:")
print(cola)
encolar(cola, 5)
encolar(cola, 2)
encolar(cola, 15)
encolar(cola, 8)
print(cola)

print("Desencolando elementos:")
print(cola)
print(desencolar(cola))
print(desencolar(cola))
print(desencolar(cola))
print(desencolar(cola))
print(cola)