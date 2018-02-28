from flask import render_template,send_file,request,redirect,url_for,flash,jsonify
from app import app
from flask_login import current_user, login_user, logout_user
from app.models import User
from app import db
from app.forms import RegistrationForm, LoginForm

# TODO: Implement main stock page:
@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

# TODO: Implement Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    signup = RegistrationForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        flash('You have logged in!')
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', LoginForm=form,RegistrationForm=signup)

@app.route('/logout',methods=['GET'])
def logout():
    if request.method == 'GET':
        print('LOGOUT')
    print("LOGOUT")
    flash('You have logged out!')
    logout_user()
    return redirect(url_for('login.html'))

@app.route('/signup', methods=['POST'])
def signup():
    form = RegistrationForm(request.form)
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

# TODO: Implement Users Page
@app.route('/users')
def userPage():
    return "Users Page is Here and will be dynamic."

#TODO: Implment Resources Page
@app.route('/resources')
def resources():
    return render_template('resources.html')

# TODO: Implement Dynamic Currency Page
@app.route('/currency')
def currency():
    return render_template('currency.html')
