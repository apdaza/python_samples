class Nodo():
    def __init__(self, valor, hijos=[]):
        self.valor = valor
        self.hijos = hijos

def buscar_en_hijos(lista, valor):
    if lista == []:
        return False
    return buscar(lista[0], valor) or buscar_en_hijos(lista[1:], valor)

def buscar(arbol, valor):
    if arbol == None:
        return False
    if arbol.valor == valor:
        return True
    return buscar_en_hijos(arbol.hijos, valor)

arbol = Nodo('a', [Nodo('an',[Nodo('ana'),Nodo('ani')]),Nodo('al'),Nodo('as',[Nodo('asa')])])

print(buscar(arbol, 'asa'))