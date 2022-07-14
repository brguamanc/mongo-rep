from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://asistencia_mongodb:cputn_2022@cluster0.20mqbce.mongodb.net/?retryWrites=true&w=majority'

ca = certifi.where()


def dbConnection():
    try:
        client = MongoClient(MONGO_URI)
        db = client["asistenciacp"] #database
    except ConnectionError:
        print('Error de conexiòn con la bdd')
    return db
#result = myCollection.insert_one(myTask)
#print(result)