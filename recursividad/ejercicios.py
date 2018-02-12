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
# 7. calcular la longitud de un número entero
# 8. determinar el mayor digito de un número entero positivo
# 9. invertir un número entero positivo
