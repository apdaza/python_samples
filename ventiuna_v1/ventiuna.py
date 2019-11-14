from random import randint
def valor_carta(carta):
    if carta[0] in ['J','Q','K']:
        return 10
    if carta[0] == 'A':
        return 1
    return int(carta[0])

def asignar_mano(mazo, cant):
    mano = []
    for i in range(cant):
        mano.append(mazo.pop(randint(0,len(mazo)-1)))
    return mano

def sumar_mano_temp(mano):
    if mano == []:
        return 0
    return valor_carta(mano[0]) + sumar_mano_temp(mano[1:])

def sumar_mano(mano):
    valor = sumar_mano_temp(mano)
    for i in mano:
        if i[0] == 'A' and valor < 11:
            valor += 10
    return valor



