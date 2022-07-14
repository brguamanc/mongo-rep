from bson import json_util
from flask import Flask, request, Response, jsonify
import database as dbase
from mensaje import Mensaje
from flask_cors import CORS,cross_origin

db = dbase.dbConnection()


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors=CORS(app)
#Rutas de la aplicación

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    mensajes = {"Mensaje":"Bienvenido al api de MongoDB"}
    return mensajes


@app.route('/mongo_audit', methods=['POST'])
def addMensaje():
    mensajes = db['reportes']
    message = request.json['message']
    datetime = request.json['datetime']

    if message and datetime:
        mensaje = Mensaje(message, datetime)
        
        id = mensajes.insert_one(mensaje.toDBCollection())
        response = {
            'id': str(id),
            'message': message,
            'datetime': datetime
        }
        return response
    else: 
        return notFound()

@app.route('/mongo_audit', methods=['GET'])
def getMensaje():
    mensajes = db['reportes']
    mensajesReceived = mensajes.find()    
    response = json_util.dumps(mensajesReceived)
    return Response(response, mimetype='application/json')
    
@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado '+ request.url,
        'status':'404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response



if __name__ == '__main__':
    app.run(host="0.0.0.0")
