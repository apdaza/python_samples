import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "articulos.db")

class Articulos:

    def abrir(self):
        conexion=sqlite3.connect(db_path)
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into articulo(art_descripcion, art_precio) values (?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select art_descripcion, art_precio from articulo where art_id=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select art_id, art_descripcion, art_precio from articulo"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()
