from flask import Flask ,request

app = Flask(__name__)
stores = [
    {
        "name":"electronics",
        "items":[
            {
                "name":"mobile",
                "price":1234
            },
            {
                "name":"laptop",
                "price":6789
            }
        ] 
    }
]
@app.route("/store")
def get_store():
    return stores


@app.route("/store",methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {"name":data['name'], "items":[]}
    stores.append(new_store)
    return new_store,200


@app.route("/store/<string:name>/item",methods=['POST'])
def create_item(name):
    data = request.get_json()    #json in data
    for store_name in stores:
        print(store_name['name'])
        if store_name['name'] == name:
            new_item_toAdd = {"name":data["name"], "price":data["price"]}
            store_name['items'].append(new_item_toAdd)
            return new_item_toAdd, 200       
    return f"{name} store not found"


@app.route("/store/<string:name>")
def get_store_name(name):
    for store in stores:
        if store['name'] == name:
            return store
    return f"{name} not found"


@app.route("/store/<string:name>/item",methods=['GET'])
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return {"items": store['items']}
    return f"{name} not found",404


if __name__ == "__main__":
    app.run(debug=True)
