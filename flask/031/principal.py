from flask import Flask, request, flash, url_for, redirect, render_template, session
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco_preguntas.sqlite3'
app.config['SECRET_KEY'] = "123456789"

db = SQLAlchemy(app)
inspector = inspect(db.engine)


class categoria(db.Model):
   id = db.Column('cat_id', db.Integer, primary_key = True)
   cat_nombre = db.Column(db.String(100))
   cat_tipo = db.Column(db.Integer)

   def __init__(self, nombre, tipo):
       self.cat_nombre = nombre
       self.cat_tipo = tipo

class tipo_categoria(db.Model):
   id = db.Column('tca_id', db.Integer, primary_key = True)
   tca_nombre = db.Column(db.String(50))

   def __init__(self, nombre):
       self.cat_nombre = nombre  

class pregunta(db.Model):
   id = db.Column('pre_id', db.Integer, primary_key = True)
   pre_texto = db.Column(db.String(150))
   cat_id = db.Column(db.Integer) 
   com_id = db.Column(db.Integer)
   tpr_id = db.Column(db.Integer)

   def __init__(self, texto, categoria, tipo, competencia):
      self.pre_texto = texto
      self.cat_id = categoria
      self.com_id = competencia
      self.tpr_id = tipo


@app.route('/')
def home():
   entidades = db.engine.table_names()
   session['entidades'] = entidades
   return render_template('home.html')

@app.route('/list/<entidad>')
def list(entidad):
   campos = inspector.get_columns(entidad)
   nombres_campos = []
   for c in campos:
      nombres_campos.append(c['name'])

   session['campos'] = nombres_campos
   session['entidad'] = entidad
   return render_template('list.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)