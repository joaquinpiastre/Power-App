import os
from app import create_app
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

app = create_app()
app.app_context().push()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    