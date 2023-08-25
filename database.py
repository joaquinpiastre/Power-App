from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

USER_DB = "postgres"
PASS_DB = "2603"
URL_DB = "localhost"
NAME_DB = "PowerApp"
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'