import sqlite3
try:
	bd = sqlite3.connect("nombre *//incorrecto...")
	print("Base de datos abierta correctamente")
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)