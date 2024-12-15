#API

from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {'id':1, 'name':'Item1', 'description':'This is item 1'},
    {'id':2, 'name':'Item2', 'description':'This is item 2'}
]

@app.route('/')
def Home():
    return "Welcome to The Sample To Do List app"


#Get: retrive all the items
@app.route('/items',methods=['GET'])
def get_tems():
    return jsonify(items)


##Get: Retrive specific items by id
@app.route('/items/<int:item_id>',method=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id']==item_id))




if __name__ =="__main__":
    app.run(debug=True)