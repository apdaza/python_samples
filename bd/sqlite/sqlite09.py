import sqlite3
try:
	bd = sqlite3.connect("libros.db")
	cursor = bd.cursor()
 
	busqueda = input("Escribe tu búsqueda: ")
	if not busqueda:
		print("Búsqueda inválida")
		exit()
 
	sentencia = "SELECT * FROM libros WHERE titulo LIKE ?;"
 
	cursor.execute(sentencia, [ "%{}%".format(busqueda) ])
	
	libros = cursor.fetchall()
	print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+".format("", "", "", ""))
	print("|{:^20}|{:^20}|{:^10}|{:^50}|".format("Autor", "Género", "Precio", "Título"))
	print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+".format("", "", "", ""))
 
 
	for autor, genero, precio, titulo in libros:
		print("|{:^20}|{:^20}|{:^10}|{:^50}|".format(autor, genero, precio, titulo))
	
 
	print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+".format("", "", "", ""))
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)
finally:
    bd.close()