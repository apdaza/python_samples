import sqlite3
bd = sqlite3.connect("base_de_datos.db")
print("Base de datos abierta")
bd.close()