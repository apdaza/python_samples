#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#      tcpserver.py
#
#      Copyright 2014 Recursos Python - www.recursospython.com
#
#

from socket import socket, error
from threading import Thread


class Client(Thread):
    """
    Servidor eco - reenvía todo lo recibido.
    """

    def __init__(self, conn, addr):
        # Inicializar clase padre.
        Thread.__init__(self)

        self.conn = conn
        self.addr = addr

    def renvio(self, msg):
        self.conn.send(msg)

    def run(self):
        while True:
            try:
                # Recibir datos del cliente.
                input_data = self.conn.recv(1024)
            except error:
                print("[%s] Error de lectura." % self.name)
                break
            else:
                # Reenviar la información recibida.
                if input_data:
                    global cola
                    cola = input_data
                    self.conn.send(input_data)


def main():
    s = socket()

    cola = ""

    # Escuchar peticiones en el puerto 6030.
    s.bind(("localhost", 6030))
    s.listen(0)
    cli = []
    while True:
        conn, addr = s.accept()
        c = Client(conn, addr)
        cli.append(c)
        c.start()
        print("%s:%d se ha conectado." % addr)
        print len(cli)
        for i in cli:
            i.renvio(cola)
        cola = ""


if __name__ == "__main__":
    main()
