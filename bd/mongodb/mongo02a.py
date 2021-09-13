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

database_entry=[
        {'name':'Hannibal', 'surname':'Lecter', 'city':'New York'},
        {'name':'Norman', 'surname':'Bates', 'city':'Los Ángeles'},
        {'name':'Michael', 'surname':'Myers', 'city':'Haddonfield'}
    ]

try:
    destination = 'USERS'
    collection = client[MONGODB_DATABASE][destination]
    collection.insert(database_entry)
    print("Data saved at %s collection in %s database: %s" % (destination, MONGODB_DATABASE, database_entry))
except Exception as error:
    print("Error saving data: %s" % str(error))