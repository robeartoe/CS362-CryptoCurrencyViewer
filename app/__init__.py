from flask import Flask

app = Flask(__name__)
# This line will allow the app to auto update: Consider removing it for production use.
app.config['DEBUG'] = True


from app import routes
