# -*- coding: utf-8 -*-
# 1. calcular el producto de dos números mediantes sumas
def producto_recursivo(n, m):
    if m == 0:
        return 0
    if m == 1:
        return n
    return n + producto_recursivo(n, (m - 1))

#2. calcular la división de dos números sin dividir (restando)
def division_recursiva(n, m):
    if n < m:
        return 0
    return 1 + division_recursiva((n - m), m)

# 3. calcular la potencia de dos números
def potencia_recursiva(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n
    return n * potencia_recursiva(n, (m - 1))

# 4. calcular el término n de la serie de fibonacci
def fibo_recursivo(n):
    if n <= 1:
        return 1
    return fibo_recursivo(n -1) + fibo_recursivo(n -2)

# 5. determinar la suma de los dígitos de un número entero positivo
def suma_digitos_recursivo(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos_recursivo(int(n/10))

# 6. determinar si un numero es palíndromo
def ultimo_digito(n):
    return n % 10

def primer_digito(n):
    if n < 10:
        return n
    return primer_digito(int(n / 10))

def quitar_extremos(n):
    pass

def palindromo_recursivo(n):
    if n < 10:
        return True
    return (primer_digito(n) == ultimo_digito(n)) and palindromo_recursivo(quitar_extremos(n))

# 7. calcular la longitud de un número entero
def long_numero(n):
    if n < 10:
        return 1
    return 1 + long_numero(n // 10)

# 8. determinar el mayor digito de un número entero positivo
def mayor_digito(n):
    if n < 10:
        return n
    if (n % 10) > mayor_digito(n // 10):
        return (n % 10)
    return + mayor_digito(n // 10)

# 9. invertir un número entero positivo
def invertir(n):
    if (n) < 10:
        return n
    return (n % 10) * 10 ** long_numero(n // 10) + invertir(n // 10)

def invertir_str(n):
    if (n) < 10:
        return str(n)
    return (str(n)[-1]) + invertir_str(n // 10)


print invertir(1234)

##arbol binario
class Nodo:
    def __init__(self, val, izq = None, der = None):
        self.valor = val
        self.izquierda = izq
        self.derecha = der

def arbol():
    return Nodo(15, Nodo(10), Nodo(25))

#1. buscar un valor en un arbol binario ordenado
def buscar(arbol, valor):
    if arbol == None:
        return False
    if valor < arbol.valor:
        return buscar(arbol.izquierda, valor)
    return buscar(arbol.derecha, valor)

#2. insertar un valor en un arbol binario ordenado
def insertar(arbol, valor):
    if arbol == None:
        return Nodo(valor)
    if valor < arbol.valor:
        return Nodo(arbol.valor, insertar(arbol.izquierda, valor), arbol.derecha)
    return Nodo(arbol.valor, arbol.izquierda, insertar(arbol.derecha, valor))

#3. recorrido en inorden
def inorden(arbol):
    if arbol == None:
        return []
    return inorden(arbol.izquierda) + [arbol.valor] + inorden(arbol.derecha)

#4. recorrido en preorden
def preorden(arbol):
    if arbol == None:
        return []
    return [arbol.valor] + preorden(arbol.izquierda) + preorden(arbol.derecha)

#5. recorrido en postorden
def postorden(arbol):
    if arbol == None:
        return []
    return [arbol.valor] + postorden(arbol.izquierda) + postorden(arbol.derecha)

#6. insertar lista de valores en un arbol binario ordenado
def lista_arbol(arbol, lista):
    if lista == []:
        return arbol
    return lista_arbol(insertar(arbol, lista[0]), lista[1:])
