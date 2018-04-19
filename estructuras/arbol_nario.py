class Nodo():
    def __init__(self, valor, hijos=[]):
        self.valor = valor
        self.hijos = hijos

def buscar(arbol, valor):
	if arbol == None:
		return False
	elif arbol.valor == valor:
		return True
	else:
		return buscar_en_hijos(arbol.hijos, valor)

def buscar_en_hijos(lista, valor):
	if lista == []:
		return False
	else:
		return buscar(lista[0], valor) or buscar_en_hijos(lista[1:], valor)

def recorrer_profundidad(arbol, recorridos):
    if arbol == None:
        return []
    return [recorrer_profundidad_hijos(arbol.hijos, recorridos + [arbol.valor])]

def recorrer_profundidad_hijos(lista, recorridos):
    if lista == []:
        return recorridos
    return recorrer_profundidad(lista[0],recorridos) + recorrer_profundidad_hijos(lista[1:], recorridos)

arbol = Nodo(10,[Nodo(20,[Nodo(40),
							Nodo(44)]),
				  Nodo(50,[Nodo(150)]),
				  Nodo(100),
				  Nodo(1000,[Nodo(2000),Nodo(3000),Nodo(5000)])])

#print buscar(arbol, 20)
#print buscar(arbol, 3000)

print [x for x in recorrer_profundidad(arbol,[]) if len(x) > 1]
