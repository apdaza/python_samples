from flask import Flask, render_template, request, redirect, url_for
from modelos.cliente import *


app = Flask(__name__)

@app.route("/")
def listar():
    data = consultar()
    return render_template('listar.html', data = data)

@app.route('/agregar', methods = ['POST', 'GET'])
def agregar():
    if request.method == 'GET':
        return render_template('agregar.html')
    else:
        info = request.form
        data = {
            'nombre': info['nombre'],
            'apellido': info['apellido'],
            'telefono': info['telefono'],
            'direccion': info['direccion']
        }
        insertar(data)
        return redirect(url_for('listar'))

@app.route('/editar/<id>', methods = ['POST', 'GET'])
def editar(id):
    if request.method == 'GET':
        data = consultar_id(id)
        return render_template('editar.html', data = data)
    else:
        info = request.form
        data = {
            'nombre': info['nombre'],
            'apellido': info['apellido'],
            'telefono': info['telefono'],
            'direccion': info['direccion']
        }
        actualizar(id, data)
        return redirect(url_for('listar'))


@app.route('/eliminar/<id>', methods = ['GET'])
def eliminar(id):
    if request.method == 'GET':
        eliminar_id(id)
        return redirect(url_for('listar'))


if __name__ == "__main__":
    app.run(debug = True)