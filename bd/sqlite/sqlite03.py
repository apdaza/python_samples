import sqlite3
try:
	bd = sqlite3.connect("base_de_datos.db")
	cursor = bd.cursor() #Con el cursor ya podemos interactuar completamente
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)
finally:
    bd.close()