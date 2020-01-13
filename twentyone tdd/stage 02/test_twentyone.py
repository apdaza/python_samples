from twentyone import *
dealer = Dealer()

# Prueba la funcion para generar nueva mano
# Resultado: 2 (True)
def test_new_round():
    dealer.new_round()
    assert len(dealer.hand) == 2

# Prueba para verificar el valor total de una mano
# Resultado: 21 (True)
def test_get_hand_total():
    dealer.hand = ['A','J']
    assert dealer.get_hand_total() == 21

# Prueba para verificar el valor total de una mano
# Resultado: 18 (True)
def test_get_hand_total_noases():
    dealer.hand = ['3','Q','5']
    assert dealer.get_hand_total() == 18

# Prueba para verificar el valor total de una mano
# Resultado: 12 (True)
def test_get_hand_total_2ases():
    dealer.hand = ['A','J','A']
    assert dealer.get_hand_total() == 12
