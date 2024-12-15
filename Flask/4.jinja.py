## variable rule
## Building URL dynamically
## jinja 2 template engine   

'''jinja template is used to read the data from backend in html file.
{{  }} expression to print output in html file
{%...%} conditions, for loops
{#...#} single line comments
'''

from flask import Flask,render_template, request, redirect,url_for

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


#HTTP verbs
@app.route("/submit",methods=['GET','POST'])  
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html') 

# ##variable rule
# @app.route('/success/<score>')   #this route will take one parameter as a score. you need to give it when you hitting the /success url. EX: /success/55
# def success(score):
#     return "The marks you got is" + score   


# @app.route('/success/<int:score>')   #we assigned the parameter is only type of int.
# def success(score):
#     return "The marks you got is" + str(score)    #score is a int so we can't concatnate the int object with str. so we need to convert it to string. ex: str(score)


#jinja 2
@app.route('/success/<int:score>')   
def success(score):         
    res = ""
    if score >= 50:
        res = "Pass"
    else:
        res = "Fail"                         #here we need to return the result  PASS or FAIl(from backend) to in a html file for that used JINJA templates 
    return render_template('result.html',result = res)   # the result is passed to html file using 'render_template'...and that passed result in html file read using jinja templates.
                                                   #ex: res passed in result.html --> it is read using jinja in result.html file. 


#for loop
@app.route('/successres/<int:score>')   
def successres(score):         
    res = ""
    if score >= 50:
        res = "Pass"
    else:
        res = "Fail"         
    exp = {'score':score,'res':res}                
    return render_template('result1.html',result = exp) 

#if condition
@app.route('/successif/<int:score>')   
def successif(score):         
    return render_template('if.html',result = score)


#building dynamic url
#url_for()
'''if we called getresult it will render get_html page. of the request is POST then saved unser input 
in variable. find total score of subjects and result will redirect to '/successres' using url_for() fun'''

@app.route('/getresult',methods=['GET','POST'])
def get_result():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])

        total_score = (science+maths+c+data_science)/4
    else:
        return render_template('get_result.html')
    return  redirect(url_for('successres',score= total_score))   #dynamic url using url_for()

if __name__=="__main__":
    app.run(debug=True)
