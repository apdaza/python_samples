from random import shuffle

def baraja():
    return [(x,y) for x in ['A','2','3','4','5','6','7','8','9','J','Q','K'] for y in ['Diamantes','Picas','Treboles','Corazones']]

def mazo(baraja):
    shuffle(baraja)
    return baraja

def valor_carta(carta):
    if carta[0] in ['J','Q','K']:
        return 10
    elif carta[0] == 'A':
        return 1
    else:
        return int(carta[0])

def evaluar_temp(mano):
    if mano == []:
        return 0
    else:
        return valor_carta(mano[0])+evaluar_temp(mano[1:])

def validar_as(mano):
    if mano == []:
        return False
    if mano[0][0] == "A":
        return True
    return validar_as(mano[1:])

def evaluar(mano):
    if validar_as(mano) and evaluar_temp(mano) <= 11:
        return evaluar_temp(mano) + 10
    return evaluar_temp(mano)

def mostrar_juego(mesa, jugador):
    print ("Mesa:____________________________________")
    print (mesa)
    print (evaluar(mesa))
    print ("")
    print ("Jugador:____________________________________")
    print (jugador)
    print (evaluar(jugador))
    print ("")

def jugar(mazo):
    jugador = []
    mesa = []
    turno = "jugador"
    if mazo == []:
        print("mazo vacio")
    else:
        mesa += [mazo.pop(),mazo.pop()]
        jugador += [mazo.pop(),mazo.pop()]
        while True:
            mostrar_juego(mesa, jugador)
            if evaluar(jugador) < 21 and turno == "jugador":
                if raw_input("desea otra carta: (s/n) ") == "s":
                    jugador += [mazo.pop()]
                else:
                    turno = "mesa"
            elif (evaluar(mesa) < evaluar(jugador) and evaluar(mesa) < 21 and evaluar(jugador) <= 21):
		        mesa += [mazo.pop()]
            else:
                return evaluar(mesa), evaluar(jugador)
