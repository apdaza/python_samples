import sqlite3
try:
	bd = sqlite3.connect("libros.db")
	cursor = bd.cursor()
	autor = input("\nAutor: ")
	genero = input("\nGénero: ")
	precio = float(input("\nPrecio: "))
	titulo = input("\nTítulo: ")
	sentencia = "INSERT INTO libros(autor, genero, precio, titulo) VALUES (?,?,?,?)"
	cursor.execute(sentencia, [autor, genero, precio, titulo])
	bd.commit()
	print("Guardado correctamente")
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)
finally:
    bd.close()