
# flask app example
# ensure that you never name the flask server as flask.py

# hosting options
# by default, the sesrver is only accessible from your own computer
# [ $ flask run --host=0.0.0.0 ] - this tells flask to listen on all public IPs

from flask import Flask, escape, request

app = Flask(__name__) #single file, use __name__, __main__ is another arguement if you have imported modules

@app.route('/') #tell flask which URL should trigger what function
def index():
    return 'Index Page'

@app.route('/hello/<greeting>')
def hello(greeting):
    return f"{greeting} Hello World!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

# hosting static files
# create a folder called static in your package or next to your module
# files will be available at the '/static' end point
# to generate URLs for static files, use the 'static' endpoint name like so:
# url_for('static', filename='style.css')

# dynamic urls
# you can use variables inside your urls to get what your user types in