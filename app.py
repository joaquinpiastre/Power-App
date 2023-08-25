from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db, FULL_URL_DB
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate()
migrate.init_app(app,db)

@app.route('/')
def home():
    print('home')
    return jsonify({'mensaje': 'Home'})

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email == 'test@example.com' and password == 'password':
        response = {'Mensaje': 'Inicio sesion correctamente'}
        return jsonify(response), 200
    else:
        response = {'Mensaje': 'Error'}
        return jsonify(response), 401

if __name__ == '__main__':
    app.run(debug=True)
