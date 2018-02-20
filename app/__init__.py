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


<<<<<<< HEAD
from app import routes, models,forms
=======
from app import routes, models
>>>>>>> f580bdd940fc8c650fff3e2797721455681d9d91
