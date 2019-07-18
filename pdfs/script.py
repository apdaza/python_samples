import re
import os

rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE|re.DOTALL)

def count_pages(filename):
    data = file(filename,"rb").read()
    return len(rxcountpages.findall(data))

def conteo(ruta):
    lista = os.listdir(ruta)
    for i in lista:
        print count_pages(i)

if __name__=="__main__":
    conteo(str(input("ingrese la ruta")))
