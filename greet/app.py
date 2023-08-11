from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def greet():
    return 'welcome'

@app.route('/welcome/home')
def greet_from_home():
    return 'welcome home'

@app.route('/welcome/back')
def regreet():
    return 'welcome back'