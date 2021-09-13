import sqlite3
try:
 
	#Conectar a la base de datos
	bd = sqlite3.connect("libros.db")
	cursor = bd.cursor()
 
	#Listar los libros
 
	sentencia = "SELECT *,rowid FROM libros;"
 
	cursor.execute(sentencia)
	
	libros = cursor.fetchall()
	print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
	print("|{:^20}|{:^20}|{:^10}|{:^50}|{:^10}|".format("Autor", "Género", "Precio", "Título", "Rowid"))
	print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
 
 
	for autor, genero, precio, titulo, rowid in libros:
		print("|{:^20}|{:^20}|{:^10}|{:^50}|{:^10}|".format(autor, genero, precio, titulo, rowid))
	
 
	print("+{:-<20}+{:-<20}+{:-<10}+{:-<50}+{:-<10}+".format("", "", "", "", ""))
 
	#Pedir id del libro a editar
	id_libro = input("\nEscribe el id del libro que quieres eliminar: ")
	if not id_libro:
		print("No escribiste nada")
		exit()
 
	#Sentencia para eliminar
	sentencia = "DELETE FROM libros WHERE rowid = ?;"
 
	#Eliminar el libro
	cursor.execute(sentencia, [id_libro])
	bd.commit()
	print("Eliminado con éxito")
 
except sqlite3.OperationalError as error:
	print("Error al abrir:", error)
finally:
    bd.close()