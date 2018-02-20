from flask import render_template,send_file,request,redirect,url_for,flash,jsonify
from app import app

# TODO: Implement main stock page:
@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

# TODO: Implement Dynamic Currency Page
@app.route('/currency')
def currency():
    return render_template('currency.html')


# TODO: Implement Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# TODO: Implement Signup Page NOTE: Will not be get, just post.
@app.route('/signup')
def signup():
    return "Signup Page"
# TODO: Implement Users Page
@app.route('/users')
def userPage():
    return "Users Page is Here and will be dynamic."

@app.route('/resources')
def resources():
    return render_template('resources.html')
