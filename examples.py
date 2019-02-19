from flask import Flask, render_template, request
from forms.forms import RegistrationForm, LoginForm

app = Flask(__name__)


# Mapping Multiple URLs
@app.route('/')
@app.route('/<user>')
def home(user=None):
    return render_template('user.html', user=user)


# This is how to use external html
@app.route('/home')
def hello_world():
    return render_template('home.html')


# How to use variables within the URL
@app.route('/user/<username>')
def user(username):
    return "Hey there %s" % username


# Can also use other variable types within URL
@app.route('/id/<int:user_id>')
def identification(user_id):
    return "Your ID number is: %d" % user_id


# How to check whether the request is GET or POST
@app.route('/index')
def index():
    return 'Method used: %s' % request.method


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably using GET"


# Passing Objects into Templates
@app.route('/shopping')
def shopping():
    food = ['Cheese', 'Pasta', 'Beef', 'Crumpet']
    return render_template('shopping.html', food=food)


# Registration Page
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


# Login Page
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run()
