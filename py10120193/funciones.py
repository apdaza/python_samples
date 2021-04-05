def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def mayor(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

def operacion(n1, n2):
    n1, n2 = n2, n1
    print(n1, n2)

def tabla(n):
    for i in range(1,11):
        print(str(n) + " * " + str(i) + " = " + str(n*i))

def tabla_a_lista(n):
    lista = []
    for i in range(1,11):
        lista.append(n*i)
    return lista, n, i

def tam_lista(lista):
    cont = 0
    while lista != []:
        lista.pop()
        cont += 1
    return cont

def tam_lista_rec(lista):
    if lista == []:
        return 0
    return 1 + tam_lista_rec(lista[1:])

def fibo(n):
    if n in [0,1]:
        return 1
    return fibo(n-1) + fibo(n-2)

def fibo2(n):
    n1 = 1
    n2 = 1
    if n in [0,1]:
        return 1
    else:
        for i in range(1,n):
            fibo = n1 + n2
            n1, n2 = n2, fibo
        return fibo

