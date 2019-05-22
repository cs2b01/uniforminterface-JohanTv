from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/datosUsuario')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.Usuarios)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

@app.route('/create_object_users', methods = ['GET'])

def create_test_books():
    db_session = db.getSession(engine)
    Usuarios = entities.Usuarios(codigo="201736950", nombre="Victor", apellido="Guerrero", password="buenosMadrugada")
    db_session.add(Usuarios)
    db_session.commit()
    return "¡Tengo un amigo mas!"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))
