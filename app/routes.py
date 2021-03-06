from flask import render_template,send_file,request,redirect,url_for,flash,jsonify
from app import app
import json
from flask_login import current_user, login_user, logout_user,login_required
from app.models import User,UserCurrencies
from app import db
from app.forms import RegistrationForm, LoginForm
from app.CCApi import getCoinList,getPrices,getFullInfo

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

    currencies = UserCurrencies.query.filter_by(user_id=user.id).all()
    coinList = getCoinList()

    return render_template('user.html',user=user.username,currencies=currencies,coinInfo = coinList)

@app.route('/addCurrency',methods=['POST'])
@login_required
def addCurrency():
    ID =  request.form['currencyID']
    Amount = request.form['currencyAmount']
    symbol = request.form['currencySymbol']
    print(ID,Amount,symbol)
    user = User.query.filter_by(username=current_user.username).first_or_404()

    currency = UserCurrencies(currency=ID,user_id=user.id,amount = Amount,symbol=symbol)

    exists = db.session.query(UserCurrencies.user_id).filter_by(currency=ID).scalar()
    if ( exists is not None):
        print(exist)
        return json.dumps({'status':'error','ID':ID,'Amount':Amount})
    else:
        db.session.add(currency)
        db.session.commit()
        return json.dumps({'status':'OK','ID':ID,'Amount':Amount})

@app.route('/updateCurrency',methods=['POST'])
@login_required
def updateCurrency():
    status = request.form['status']
    print(status)
    user = User.query.filter_by(username=current_user.username).first_or_404()
    if status == "update":
        currency = db.session.query(UserCurrencies).filter_by(user_id=user.id,currency=request.form['currencyID']).first()
        currency.amount = request.form['currencyAmount']
        db.session.commit()
        return json.dumps({'status':'OK'})
    elif status == "delete":
        currency = db.session.query(UserCurrencies.user_id).filter_by(currency=request.form['currencyID']).delete()
        db.session.commit()
        return json.dumps({'status':'OK'})
    pass
#TODO: Implment Resources Page
@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/currency',methods=['GET'])
def currency():
    page = request.args.get('id')
    coinList = getCoinList()
    stats = getFullInfo(page)
    return render_template('currency.html',coinInfo = coinList,stats = stats)
