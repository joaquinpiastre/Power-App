from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from app.config import config
import os

ma = Marshmallow()
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    config_name = os.getenv('FLASK_ENV')
    app = Flask(__name__)
    f = config.factory(config_name if config_name else 'development')
    app.config.from_object(f)
    
    ma.init_app(app)
    f.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from app.resources import home, user
    app.register_blueprint(home, url_prefix='/api/v1')
    app.register_blueprint(user, url_prefix='/api/v1')
        
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}
    
    return app
