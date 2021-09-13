import sqlite3
try:
	bd = sqlite3.connect("libros.db")
	cursor = bd.cursor()
	libros = [
		"""
		INSERT INTO libros
		(autor, genero, precio, titulo)
		VALUES
		('Stephen King', 'Terror', 115,'Cementerio de animales'),
		('Alfred Bester', 'Ciencia ficción', 200,'Las estrellas, mi destino'),
		('Margaret Atwood', 'Ciencia ficción', 150,'El cuento de la criada');
		"""
	]
	for sentencia in libros:
		cursor.execute(sentencia);
	bd.commit() #Guardamos los cambios al terminar el ciclo
	print("Libros insertados correctamente")
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)
finally:
    bd.close()