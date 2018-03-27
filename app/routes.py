from flask import render_template,send_file,request,redirect,url_for,flash,jsonify
from app import app
from flask_login import current_user, login_user, logout_user,login_required
from app.models import User
from app import db
from app.forms import RegistrationForm, LoginForm
from app.CCApi import getCoinList,getPrices,getFullInfo

# TODO: Implement main stock page:
@app.route('/',methods=['GET','POST'])
@app.route('/index', methods=['GET','POST'])
def index():
    page = request.args.get('page',1,type=int)

    coinList = getCoinList()
    coins = getPrices(page)
    if page > 1:
        prevURL = url_for('index',page=page-1)
    else:
        prevURL = None
    nextURL = url_for('index',page=page+1)

    return render_template('home.html',currencies = coins,coinInfo = coinList,nextURL=nextURL,prevURL=prevURL)

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
    flash('You have logged out!')
    logout_user()
    return redirect(url_for('login'))

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
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html',user=user)

@app.route('/addCurrency',methods=['POST'])
@login_required
def addCurrency():
    coin = request.args.get('coin')

    pass

#TODO: Implment Resources Page
@app.route('/resources')
def resources():
    return render_template('resources.html')

# TODO: Implement Dynamic Currency Page
@app.route('/currency',methods=['GET','POST'])
def currency():
    page = request.args.get('id')

    coinList = getCoinList()
    stats = getFullInfo(page)

    return render_template('currency.html',coinInfo = coinList,stats = stats)
