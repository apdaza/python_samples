from productos import *

class Fabrica:
    def crear_arma(self):
        pass

    def crear_escudo(self):
        pass

    def crear_montura(self):
        pass

class FabricaEnanos(Fabrica):
    def crear_arma(self):
        return ArmaEnano()

    def crear_escudo(self):
        return EscudoEnano()

    def crear_montura(self):
        return MonturaEnano()

class FabricaBarbaros(Fabrica):
    def crear_arma(self):
        return ArmaBarbaro()

    def crear_escudo(self):
        return EscudoBarbaro()

    def crear_montura(self):
        return MonturaBarbaro()

class FabricaElfos(Fabrica):
    def crear_arma(self):
        return ArmaElfo()

    def crear_escudo(self):
        return EscudoElfo()

    def crear_montura(self):
        return MonturaElfo()

class FabricaMagos(Fabrica):
    def crear_arma(self):
        return ArmaMago()

    def crear_escudo(self):
        return EscudoMago()

    def crear_montura(self):
        return MonturaMago()

def cambiar_fabrica(contador):
    if contador == 0:
        return FabricaElfos()
    if contador == 1:
        return FabricaMagos()
    if contador == 2:
        return FabricaBarbaros()
    return FabricaEnanos()
