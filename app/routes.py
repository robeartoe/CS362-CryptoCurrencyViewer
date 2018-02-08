from app import app

# TODO: Implement main stock page:
@app.route('/')
@app.route('/index')
def index():
    return "Stocks Page"
# TODO: Implement Login Page
@app.route('/login')
def login():
    return "Login Page"
# TODO: Implement Signup Page
@app.route('/signup')
def signup():
    return "Signup Page"
# TODO: Implement Users Page
@app.route('/users')
def userPage():
    return "Users Page is Here and will be dynamic."
