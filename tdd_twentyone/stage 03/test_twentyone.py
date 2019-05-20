from twentyone import *
dealer = Dealer()

# Prueba la funcion para generar nueva mano
# Resultado: 2 (True)
def test_new_round():
    dealer.new_round()
    assert len(dealer.hand) == 2
