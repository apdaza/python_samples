def producto_recursivo(n, m):
    if m == 0:
        return 0
    if m == 1:
        return n
    return n + producto_recursivo(n, (m - 1))

def division_recursiva(n, m):
    if n < m:
        return 0
    return 1 + division_recursiva((n - m), m)

def potencia_recursiva(n, m):
    if m == 0:
        return 1
    if m == 1:
        return n
    return n * potencia_recursiva(n, (m - 1))
