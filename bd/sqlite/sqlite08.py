import sqlite3
try:
	bd = sqlite3.connect("libros.db")
	cursor = bd.cursor()
	sentencia = "SELECT * FROM libros;"
 
	cursor.execute(sentencia)
	
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