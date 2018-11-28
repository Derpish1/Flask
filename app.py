from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/user/<username>')
def user(username):
    return "Hey there %s" % username


if __name__ == '__main__':
    app.run()
