from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# This line will allow the app to auto update: Consider removing it for production use.
app.config['DEBUG'] = True


from app import routes,models,forms
