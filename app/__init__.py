from flask_cors import CORS
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    load_dotenv()
    
    print(os.environ("USER_DB"))
    
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ("USER_DB")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    

create_app()