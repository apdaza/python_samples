'''
Created on 20/02/2009
@author: Chuidiang


Ejemplo de socket en python. Un servidor que acepta clientes.
Si el cliente envia "hola", el servidor contesta "pues hola".
Si el cliente envia "adios", el servidor contesta "pues adios" y
cierra la conexion.
El servidor no acepta multiples clientes simultaneamente.
'''

import socket
from threading import Thread

class Gost():
    __instance = None

    def __new__(cls):
        if Gost.__instance is None:
            Gost.__instance = object.__new__(cls)
        return SoyUnico.__instance

    def __init__(self):
        self.x = 100
        self.y = 200

    def mover(self):
        self.x = self.x+10
        self.x = self.x % 800
        self.y = 200

    def getPos(self):
        return str(self.x)+","+str(self.y)

class Cliente(Thread):
    def __init__(self, server, socket_cliente, datos_cliente, gost, hermanos = []):
        Thread.__init__(self)
        self.server = server
        self.socket = socket_cliente
        self.datos = datos_cliente
        self.gost = gost
        self.hermanos = hermanos

    def send_msg(self, msg):
        self.socket.send(msg)

    def set_hermanos(self, hermanos):
        self.hermanos = hermanos

    # Bucle para atender al cliente.
    def run(self):
      # Bucle indefinido hasta que el cliente envie "adios"
      seguir = True
      while seguir:
         # Espera por datos
         peticion = self.socket.recv(1024)
         print peticion
         #self.socket.send(peticion)

         # Contestacion a "hola"
         if ("hola"==peticion):
             print str(self.datos)+ " envia hola: contesto"
             self.socket.send(str(self.gost.getPos()))

         # Contestacion y cierre a "adios"
         elif ("adios"==peticion):
             print str(self.datos)+ " envia adios: contesto y desconecto"
             self.socket.send("pues adios")
             self.socket.close()
             print "desconectado "+str(self.datos)
             seguir = False
         if ("cerrar" == peticion):
             print "ok..."
             self.server.shutdown(socket.SHUT_RDWR)
             break
         else:
            print str(self.datos)+ " envia otra cosa: y no me importa"
            self.socket.sendall(self.gost.getPos())
            self.gost.mover()
            """if self.hermanos != []:
                for i in self.hermanos:
                    i.socket.sendall(peticion)"""




if __name__ == '__main__':
   #contador = 0
   # Se prepara el servidor
   server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   server.bind(("", 5050))
   server.listen(10)
   print "Esperando clientes..."
   hilos = []
   gost = Gost()
   # bucle para atender clientes
   while 1:

      # Se espera a un cliente
      socket_cliente, datos_cliente = server.accept()
      #contador = contador + 1
      # Se escribe su informacion
      print "conectado "+str(datos_cliente)

      # Se crea la clase con el hilo y se arranca.
      hilos.append(Cliente(server, socket_cliente, datos_cliente, gost))
      hilos[-1].start()
      gost.x=gost.x+10

      """for i in hilos:
          i.set_hermanos(hilos)"""
