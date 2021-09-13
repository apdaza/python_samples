import pymongo

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
    condition = {}
    """
    sort("name", 1) -- ascendente
    sort("name", -1) -- descendente
    limit(x) -- cantidad de documentos que quiero
    """
    result = collection.find(condition).sort('surname', 1).limit(1)
    print("Documents found: %d" % collection.count_documents(condition))
    print('')
    for entry_json in result:
        print("Found document at %s collection with next values:" % destination)
        for key in entry_json:
            print(' '  + key + ' : ' + str(entry_json[key]))
        print('')
except Exception as error:
    print("Error getting data: %s" % str(error))