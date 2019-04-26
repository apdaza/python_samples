# -*- coding: utf-8 -*-
"""
¡Hola, Mundo!
Programa ¡Hola, Mundo! en diversas versiones de Python: Python 2.x:
"""
print "Hola Mundo python 2"
"""
Python 3.x:
"""
print("Hola Mundo python 3");

"""
Fuertemente tipado
El fuertemente tipado 28 significa que el tipo de valor no cambia repentinamente. Un string (Página 45) que contie-
ne solo dígitos no se convierte mágicamente en un número. Cada cambio de tipo requiere una conversión explícita.
"""
# varible "valor1" es integer, varible "valor2" es string
valor1, valor2 = 2, "5"
# el metodo int() es para convertir a integer
total = valor1 + int(valor2)
# el metodo str() es para convertir a string
print "El total es: " + str(total)

"""
Tipado dinámico
El tipado dinámico 29 significa que los objetos en tiempo de ejecución (valores) tienen un tipo, a diferencia del
tipado estático donde las variables tienen un tipo.
"""
# "variable" guarda un valor integer
variable = 11
print variable, type(variable)
# "variable" guarda un valor string
variable = "activo"
print (variable), type(variable)

"""
Ejemplo de asignar valor a variable
"""
c = "Hola Mundo" # cadenas de caracteres
print type(c) # comprobar tipo de dato
e = 23 # número entero
print type(e) # comprobar tipo de dato

a, b, c = 5, 3.2, "Hola"
print a
print b
print c
"""
asignar el mismo valor a múltiples variables al mismo tiempo
"""
x = y = z = True
print x, y, z

"""
Palabras reservadas
Existen ciertas palabras que tienen significado especial para el intérprete de Python. Estas no pueden utilizarse
para ningún otro fin (como ser nombrar valores) excepto para el que han sido creadas. Estas son:

and, as, assert, break, class, continue, def, del, elif, else, except,
exec, finally, for, from, global, if, import, in, is, lambda, not,
or, pass, print, raise, return, try, while, with, yield.

Puede verificar si una palabra esta reservada utilizando el módulo integrado keyword
"""
import keyword
print keyword.iskeyword('as')
print keyword.iskeyword('x')
"""
Para obtener una lista de todas las palabras reservadas
"""
import keyword
print keyword.kwlist
"""
Sentencia del
"""
cadena, numero, lista = "Hola Plone", 123456, [7,8,9,0]
tupla = (11, "Chao Plone", True, None)
diccionario = {"nombre":"Leonardo","apellido":"Caballero"}

print vars()
del numero, lista, tupla, diccionario
print vars()

"""
Sentencia global
La sentencia global es una declaración que se mantiene para todo el bloque de código actual. Eso significa que
los identificadores listados son interpretados como globales.
"""
variable1 = "variable original"
def variable_global():
    global variable1
    variable1 = "variable global modificada"

print variable1
variable_global()
print variable1

"""
Operadores de asignaciones
"""
#Operador =
x = 5; print x
#Operador +=
r = 5; r = r + 10; print r
#Operador -=
r = 5; r -= 10; print r
#Operador *=
r = 5; r *= 10; print r
#Operador /=
r = 5; r /= 10; print r
#Operador **=
r = 5; r **= 10; print r
#Operador //=
r = 5; r //= 10; print r
#Operador %=
r = 5; r %= 10; print r

a, b, c = 21, 10, 0
print "Valor de variable 'a':", a
print "Valor de variable 'b':", b
c = a + b
print "Operador = | El valor de variable 'c' es ", c
c += a
print "Operador += | El valor de variable 'c' es ", c
c *= a
print "Operador *= | El valor de variable 'c' es ", c
c /= a
print "Operador /= | El valor de variable 'c' es ", c
c = 2
c %= a
print "Operador %= | El valor de variable 'c' es ", c
c **= a
print "Operador **= | El valor de variable 'c' es ", c
c //= a
print "Operador //= | El valor de variable 'c' es ", c

"""
Operadores aritméticos
El orden de precedencia de ejecución de los operadores aritméticos es:
1. Exponente: **
2. Negación: -
3. Multiplicación, División, División entera, Módulo: * , /, //, %
4. Suma, Resta: +, -
"""
print 3 + 2
print 4 - 7
print -7
print 2 * 6
print 2 ** 6
print 3.5 / 2
print 3.5 // 22
print 7 % 2
print 2**1/12
print 2**(1/12)

"""
Operadores relacionales
"""
#Operador ==
print 5 == 3
print 5 == 5
print "Plone" == 5
print "Plone" == "Plone"
print type("Plone") == str
#Operador !=
print 5 != 3
print "Plone" != 5
print "Plone" != False
#Operador <
print 5 < 3
#Operador >
print 5 > 3
#Operador <=
print 5 <= 3
#Operador >=
print 5 >= 3

a, b, a1, b1, c1 = 5, 5, 7, 3, 3
cadena1, cadena2 = 'Hola', 'Adiós'
lista1, lista2 = [1, 'Lista Python', 23], [11, 'Lista Python', 23]
#Ejemplo de operador relacional Igual
c = a == b
print c
cadenas = cadena1 == cadena2
print cadenas
listas = lista1 == lista2
print listas
#Ejemplo de operador relacional Diferente
d = a1 != b
print d
cadena0 = cadena1 != cadena2
print cadena0
#Ejemplo de operador relacional Menor que
f = b1 < a1
print f
#Ejemplo de operador relacional Mayor que
e = a1 > b1
print e
#Ejemplo de operador relacional Menor o igual que
h = b1 <= c1
print h
#Ejemplo de operador relacional Mayor o igual que
g = b1 >= c1
print g

"""
tipos de datos
"""
#Enteros
entero = 23
print entero, type(entero)
entero = 23L
print entero, type(entero)
entero = 0712 #octal
print entero, type(entero)
entero = 0x23AF #hexa
print entero, type(entero)
#Coma flotante
float_1, float_2, float_3 = 0.348, 10.5, 1.5e2
print float_1, type(float_1)
print float_2, type(float_2)
print float_3, type(float_3)
real = 0.56e-3
print real, type(real)
#complejos
complejo = 2.1 + 7.8j
print complejo, complejo.imag, complejo.real, type(complejo)
complejo = 3.14j
print complejo, complejo.imag, complejo.real, type(complejo)
#booleanos
aT, aF = True, False
print "El valor es", aT, "de tipo:", type(aT), "\n"
print "El valor es", aF, "de tipo:", type(aF)
aAnd = True and False
print "SI es Verdadero Y Falso, es", aAnd, "de", type(aAnd), "\n"
aOr = True or False
print "SI es Verdadero O Falso, es", aOr, "de", type(aOr), "\n"
aNot = not True
print "Si NO es Verdadero, es", aNot, "de", type(aNot), "\n"
#cadenas
cadena = "hola mundo"
print cadena, type(cadena)
a, b = "uno", "dos"
print a + b
c = "tres"
print c * 3

"""
Formateo de cadenas
Python soporta múltiples formas de formatear una cadena de caracteres.
%c = str, simple carácter.
%s = str, cadena de carácter.
%d = int, enteros.
%f = float, coma flotante.
%o = octal.
%x = hexadecimal.
"""
tipo_calculo = "raíz cuadrada de dos"
valor = 2**0.5
print "el resultado de %s es %f" % (tipo_calculo, valor)
print "el resultado de %s es %.8f" % (tipo_calculo, valor)
print "CMS: %s, ¿Activar S o N?: %c" % ("Plone", "S")
print "N. factura: %d, Total a pagar: %f" % (345, 658.23)
print "Tipo Octal: %o, Tipo Hexadecimal: %x" % (027, 0x17)

#formateo con format()
tipo_calculo = "raíz cuadrada de dos"
valor = 2**0.5
print "el resultado de {} es {}".format(tipo_calculo, valor)
print "el resultado de {0} es {1}".format(tipo_calculo, valor)
tipo_calculo = "raíz cuadrada de dos"
print "el resultado de {nombre} es {resultado}".format(nombre=tipo_calculo, resultado=2**0.5)
print "{:>30}".format("raíz cuadrada de dos") #Alinear una cadena de caracteres a la derecha en 30 caracteres
print "{:30}".format("raíz cuadrada de dos") #Alinear una cadena de caracteres a la izquierda en 30 caracteres (crea espacios a la derecha)
print "{:^30}".format("raíz cuadrada de dos") #Alinear una cadena de caracteres al centro en 30 caracteres
print "{:.9}".format("raíz cuadrada de dos") #Truncamiento a 9 caracteres
print "{:>30.9}".format("raíz cuadrada de dos") #Alinear una cadena de caracteres a la derecha en 30 caracteres con truncamiento de 9
tipo_calculo = "raíz cuadrada de dos"
valor = 2**0.5
print "el resultado de {0} es {resultado:.4f}".format(tipo_calculo, resultado=valor)
#formateo de Enteros
print "{:4d}".format(10)
print "{:4d}".format(100)
print "{:4d}".format(1000)
print "{:04d}".format(10)
print "{:04d}".format(100)
print "{:04d}".format(1000)
#formateo de flotantes
print "{:7.3f}".format(3.1415926)
print "{:7.3f}".format(153.21)
print "{:07.3f}".format(3.1415926)
print "{:07.3f}".format(153.21)

"""
Tipo listas
Entre las secuencias, el más versátil, es la lista, para definir una, usted debe escribir es entre corchetes, separando
sus elementos con comas cada uno. La lista en Python son variables que almacenan arrays, internamente cada posición puede ser un tipo de datos
distinto.
Las listas en Python son:
heterogéneas: pueden estar conformadas por elementos de distintos tipo, incluidos otras listas.
mutables: sus elementos pueden modificarse.
"""
factura = ['pan', 'huevos', 100, 1234]
print factura
['pan', 'huevos', 100, 1234]
print factura[0], factura[2]
print len(factura)
print factura[-1], factura[-3]
print factura[-len(factura)]
#cambiar elementos
factura[1] = "carne"
print factura
#agregar elementos
versiones_plone = [2.5, 3.6, 4, 5]
print versiones_plone
versiones_plone.append(6)
print versiones_plone
versiones_plone += [7.0]
#contando elementos
print versiones_plone
print "6 ->", versiones_plone.count(6)
print "5 ->", versiones_plone.count(5)
#agregando iterables
versiones_plone = [2.1, 2.5, 3.6]
print versiones_plone
versiones_plone.extend([4, 6])
print versiones_plone
versiones_plone.extend(range(7,10))
print versiones_plone
#indice de un elementos
print versiones_plone.index(4)
#insertando un elemento
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print versiones_plone
versiones_plone.insert(2, 3.7)
print versiones_plone
#extraer un elemento
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print versiones_plone.pop()
print versiones_plone
print versiones_plone.pop(2)
print versiones_plone
#remover un elemento
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print versiones_plone
versiones_plone.remove(2.5)
print versiones_plone
#invertir lista
versiones_plone = [2.1, 2.5, 3.6, 4, 5, 6]
print versiones_plone
versiones_plone.reverse()
print versiones_plone
#ordenado de lista
versiones_plone = [4, 2.5, 5, 3.6, 2.1, 6]
print versiones_plone
versiones_plone.sort()
print versiones_plone
"""
Ejemplo de iterar sobre listas
"""
mensaje = "Hola, como estas tu?"
print mensaje.split() # retorna una lista
for palabra in mensaje.split():
    print palabra

preguntas = ['nombre', 'objetivo', 'sistema operativo']
respuestas = ['Leonardo', 'aprender Python y Plone', 'Linux']
for pregunta, respuesta in zip(preguntas, respuestas):
    print '¿Cual es tu {0}?, la respuesta es: {1}.'.format(pregunta, respuesta)

"""
Tipo tuplas
Las tuplas son objetos de tipo secuencia, específicamente es un tipo de dato lista inmutable. Esta no
puede modificarse de ningún modo después de su creación.
"""
valores = ("Python", True, "Zope", 5)
print "True ->", valores.count(True)
print valores.index(True)

tecnologias = ('Zope', 'Plone', 'Pyramid')
for i in range(0, len(tecnologias)):
    print i, tecnologias[i]

"""
Tipo diccionarios
El diccionario, define una relación uno a uno entre claves y valores.
"""
diccionario = {
    "clave1":234,
    "clave2":True,
    "clave3":"Valor 1",
    "clave4":[1,2,3,4]
    }
print diccionario, type(diccionario)
print type(diccionario['clave1'])
print type(diccionario['clave2'])
print type(diccionario['clave3'])
print type(diccionario['clave4'])
#acceder a valor
versiones = dict(python=2.7, zope=2.13, plone=5.1, django=2.1)
print versiones['zope']
#Asignar valor a clave
versiones = {'python': 2.7, 'zope': 2.13, 'plone': None}
print versiones['plone']
versiones['plone'] = 5.1
print versiones
print versiones['plone']
print 'plone' in versiones
print 'flask' in versiones

#Este método remueve todos los elementos desde el diccionario.
versiones = dict(python=2.7, zope=2.13, plone=5.1)
print versiones
versiones.clear()
print versiones

#Este método devuelve una copia superficial del tipo diccionario:
versiones = dict(python=2.7, zope=2.13, plone=5.1)
otro_versiones = versiones.copy()
print versiones == otro_versiones
#Este método devuelve el valor en base a una coincidencia de búsqueda en un diccionario
versiones = dict(python=2.7, zope=2.13, plone=5.1)
print versiones.get('plone')
#Este método devuelve el valor True si el diccionario tiene presente la clave enviada como argumento.
versiones = dict(python=2.7, zope=2.13, plone=5.1)
print versiones.has_key('plone')
#Este método devuelve una lista de pares de diccionarios (clave, valor), como 2 tuplas.
versiones = dict(python=2.7, zope=2.13, plone=5.1)
print versiones.items()
#Este método devuelve un iterador sobre los elementos (clave, valor) del diccionario.
versiones = dict(python=2.7, zope=2.13, plone=5.1)
for clave,valor in versiones.iteritems():
    print clave,valor
