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

if __name__ == "__main__":
    app.run(debug=True)
