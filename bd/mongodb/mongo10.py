import pymongo
from bson import ObjectId

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = '27017'
MONGODB_TIMEOUT = 1000
MONGODB_DATABASE = 'TEST'

URI_CONNECTION = "mongodb://" + MONGODB_HOST + ":" + MONGODB_PORT +  "/"

try:
    client = pymongo.MongoClient(URI_CONNECTION, serverSelectionTimeoutMS=MONGODB_TIMEOUT, maxPoolSize=10)
    client.server_info()
    print('OK -- Connected to MongoDB at server %s' % (MONGODB_HOST))
except pymongo.errors.ServerSelectionTimeoutError as error:
    print('Error with mongoDB connection: %s' % error)
except pymongo.errors.ConnectionFailure as error:
    print('Could not connect to MongoDB: %s' % error)

try:
    destination = 'USERS'
    collection = client[MONGODB_DATABASE][destination]
    condition = {'_id': ObjectId('613f413e4a24c1b1156905eb')}
    values = { "$set": { "address": "Canyon 123" } }
    collection.update_one(condition,values)
    result = collection.find_one(condition)
    if result is None:
        print("None document found!!")
    else:
        print(result)
except Exception as error:
    print("Error getting data: %s" % str(error))