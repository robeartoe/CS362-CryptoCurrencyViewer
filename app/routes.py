from flask import render_template,send_file,request,redirect,url_for,flash,jsonify
from app import app
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from app import db
from app.forms import RegistrationForm
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
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
# TODO: Implement Signup Page NOTE: Will not be get, just post.
@app.route('/signup')
def signup():
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Signup', form=form)

# TODO: Implement Users Page
@app.route('/users')
def userPage():
    return "Users Page is Here and will be dynamic."

@app.route('/resources')
def resources():
    return render_template('resources.html')
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
