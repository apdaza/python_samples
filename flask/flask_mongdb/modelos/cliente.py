import pymongo as pm
from bson import ObjectId

HOST = "127.0.0.1"
PORT = "27017"

DATABASE = "clasemod2"
COLLECTION = 'clientes'

URI_CONECTION = "mongodb://" + HOST + ":" + PORT +"/"

def consultar():
    data = {}
    try:
        cliente = pm.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {}
        data = coleccion.find(condicion)
    except Exception as error:
        print(error)
    finally:
        return data

def consultar_id(id):
    data = {}
    try:
        cliente = pm.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {'_id': ObjectId(id)}
        data = coleccion.find_one(condicion)
    except Exception as error:
        print(error)
    finally:
        return data


def insertar(data):
    try:
        cliente = pm.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        coleccion.insert_one(data)
    except Exception as error:
        print(error)

def actualizar(id, data):
    try:
        cliente = pm.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {'_id': ObjectId(id)}
        valores = {'$set': data}
        coleccion.update_one(condicion, valores)
    except Exception as error:
        print(error)
    
def eliminar_id(id):
    try:
        cliente = pm.MongoClient(URI_CONECTION)
        coleccion = cliente[DATABASE][COLLECTION]
        condicion = {'_id': ObjectId(id)}
        coleccion.delete_one(condicion)
    except Exception as error:
        print(error)
    