from flask import Flask,render_template, request

## WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1> hey! welcome to flask app<h1><html>"

@app.route("/index", methods=['GET'])
def index_page():
    return render_template("index.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

'''by default the method is 'GET' if we hit /form then it will redirect to form.html using render template.
then if we try to input some data then it is type of POST method.
if the method is 'POST' then it will return the 'name' from the form.html file.
'''
@app.route("/form",methods=['GET','POST']) 
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')   #by default redirect to form.html file


# in form.html we handled this route using action='/submit'
#once a post request received then it will redirect to submit page.
@app.route("/submit",methods=['GET','POST'])  
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')   #by default redirect to form.html file


if __name__=="__main__":
    app.run(debug=True)
