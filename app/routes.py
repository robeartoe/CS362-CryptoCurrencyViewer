from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Stocks Page"

@app.route('/login')
def login():
    return "Login Page"

@app.route('/signup')
def signup():
    return "Signup Page"

@app.route('/users')
def userPage():
    return "Users Page is Here and will be dynamic."
