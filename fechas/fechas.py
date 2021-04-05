"""
Dada una lista de fechas en formato YY:MM:DD pedir al usuario un valor en segudos e incrementar todas las horas de la lista con el valor de tiempos leidos
"""

def convertir_a_enteros(cadena):
    lista = cadena.split(":")
    return [int(x) for x in lista]

def lista_a_horas(lista):
    return [convertir_a_enteros(x) for x in lista]

def extraer_hora(s):
    h = s / 3600
    s = s % 3600
    m = s / 60
    s = s % 60
    return [h, m, s]

def incrementar(original, incremento):
    s = original[2] + incremento[2]
    if s >= 60:
        s = s - 60
        temp = 1
    else:
        temp = 0
    m = original[1] + incremento[1] + temp
    if m >= 60:
        m = m - 60
        temp = 1
    else:
        temp = 0
    h = original[0] + incremento[0] + temp
    return [h, m, s]

def completar(valor):
    if valor < 10:
        return "0" + str(valor)
    else:
        return str(valor)

def dar_formato(lista):
    if len(lista) == 1:
        return completar(lista[0])
    else:
        return completar(lista[0]) + ":" + dar_formato(lista[1:])

horas = ["12:10:20","05:30:40","18:45:55","20:15:25"]
segundos = int(input("ingrese los segundos"))
print [dar_formato(y) for y in [incrementar(x, extraer_hora(segundos)) for x in lista_a_horas(horas)]]
