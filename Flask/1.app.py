from flask import Flask
'''
It creates an instance of a Flask class,
which will be your WSGI(web server Gateway Interface) application.
'''

## WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome to the Flask App."

@app.route("/index")
def index_page():
    return "welcome to the index page of flask app"


if __name__=="__main__":
    app.run(debug=True)
