from ventiuna import *

m, j = jugar(mazo(baraja()))

if m < j and j <= 21:
    print "el jugador gana"
elif m <= 21:
    print "la casa gana"
else:
    print "el jugador gana"
