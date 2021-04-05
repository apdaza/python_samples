from ventiuna import *

mazo = [(v,p) for v in ['A','2','3','4','5','6','7','8','9','J','Q','K'] for p in ['C','D','T','P']]

mano = asignar_mano(mazo, 3)

print(mano, sumar_mano(mano))
