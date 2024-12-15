from flask import Flask,render_template

## WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1> hey! welcome to flask app<h1><html>"

@app.route("/index")
def index_page():
    return render_template("index.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
