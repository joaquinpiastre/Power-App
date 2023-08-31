from flask import Flask, jsonify, request
from flask_cors import CORS
from database import db, FULL_URL_DB
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)

app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app = create_app(app)

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate()
migrate.init_app(app,db)

if __name__ == '__main__':
    app.run(debug=True, host='0, 0, 0, 0', port=5000)
