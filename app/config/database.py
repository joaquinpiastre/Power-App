from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()

USER_DB = "postgres"
PASS_DB = "2603"
URL_DB = "localhost"
NAME_DB = "PowerAPP"
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'
# postgresql://postgres:2603@localhost/PowerAPP
