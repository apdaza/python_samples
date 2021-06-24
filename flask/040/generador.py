import pandas as pd
from random import randint, choice

provincias = ['Bogotá', 'Cali', 'Chía', 'Cajicá', 'Cota', 'Fusa', 'Fagua', 'Cucuta',
              'Choco', 'Zipaquira', 'Pereira']
generos = ['F','M']
nombre = []
edad = []	
genero = []
provincia = []
hijos = []
mascotas = []

for i in range(1000):
    nombre.append('persona_'+str(i))
    edad.append(randint(20, 80))
    genero.append(choice(generos))
    provincia.append(choice(provincias))
    hijos.append(randint(0,5))
    mascotas.append(randint(0,10))

data = {'nombres':nombre, 'edades': edad, 'generos': genero, 
        'provincias': provincia, 'hijos': hijos, 'mascotas': mascotas}
destino = pd.DataFrame(data, columns = ['nombres', 'edades', 'generos',
                                        'provincias', 'hijos', 'mascotas'])

destino.to_csv('info2.csv')
 


