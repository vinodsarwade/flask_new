'''flask operation using list(get, post items in list)'''
# from flask import Flask ,request

# app = Flask(__name__)
# stores = [
#     {
#         "name":"electronics",
#         "items":[
#             {
#                 "name":"mobile",
#                 "price":1234
#             },
#             {
#                 "name":"laptop",
#                 "price":6789
#             }
#         ] 
#     }
# ]
# @app.route("/store")
# def get_store():
#     return stores


# @app.route("/store",methods=['POST'])
# def create_store():
#     data = request.get_json()
#     store = {"name":data['name'], "items":[]}
#     stores.append(store)
#     return store,200


# @app.route("/store/<string:name>/item",methods=['POST'])
# def create_item(name):
#     data = request.get_json()    #json in data
#     for store_name in stores:
#         print(store_name['name'])
#         if store_name['name'] == name:
#             new_item_toAdd = {"name":data["name"], "price":data["price"]}
#             store_name['items'].append(new_item_toAdd)
#             return new_item_toAdd, 200       
#     return f"{name} store not found"


# @app.route("/store/<string:name>")
# def get_store_name(name):
#     for store in stores:
#         if store['name'] == name:
#             return store
#     return f"{name} not found"


# @app.route("/store/<string:name>/item",methods=['GET'])
# def get_item_in_store(name):
#     for store in stores:
#         if store['name'] == name:
#             return {"items": store['items']}
#     return f"{name} not found",404


# if __name__ == "__main__":
#     app.run(debug=True)



'''flask operation using dictionary( get post add items in dict using key value. )'''


# import uuid
# from flask import Flask ,request
# from db import stores, items

# app = Flask(__name__)

# @app.route("/store")
# def get_store():
#     return {"stores":list(stores.values())}


# @app.route("/store",methods=['POST'])
# def create_store():
#     store_data = request.get_json()
#     store_id = uuid.uuid4().hex        #dfghj9ytrtyujk5678 (universal unique id)
#     store = {**store_data, "id":store_id}
#     stores[store_id] = store
#     return store,200


# @app.route("/item",methods=['POST'])
# def create_item():
#     item_data = request.get_json()    #json in data
#     if item_data["store_id"] not in stores:
#         return {"message": "Store not found"}, 404
#     item_id = uuid.uuid4().hex    
#     item = {**item_data, "id":item_id}
#     items[item_id] = item
#     return item,201


# @app.route("/item")
# def get_item():
#     return {"items":list(items.values())}


# @app.route("/store/<string:store_id>")
# def get_store_name(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         return{"message" : "store not found"}, 404


# @app.route("/item/<string:item_id>")
# def get_itemm(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         return{"message":"item not found"}, 404
    

# if __name__ == "__main__":
#     app.run(debug=True)


'''use flask smorest for automated error handling and  error documentation effectively. '''

# import uuid
# from flask import Flask ,request, jsonify
# from flask_smorest import abort         #flask smorest
# from db import stores, items

# app = Flask(__name__)

# @app.route("/store")
# def get_store():
#     return {"stores":list(stores.values())}


# @app.route("/store",methods=['POST'])
# def create_store():
#     store_data = request.get_json()

#     if "name" not in store_data:          #validation check for name is given or not in payload.
#         abort(400, message = "Bad request. Ensure name icluded in JSON payload.")

#     for store in stores.values():       #validation for store name already present or not.
#         if store_data["name"] == store["name"]:
#             abort(400, message= "Store name already exists.") 

#     store_id = uuid.uuid4().hex                #(universal unique id)
#     store = {**store_data, "id":store_id}
#     stores[store_id] = store            #add newly created store in stores dict with store_id as key and store(with all data) as a value.
#     return store

# @app.route("/store/<string:store_id>")
# def get_store_name(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         # return{"message" : "store not found"}, 404
#         abort(404, message = "store not found")

# @app.route("/store/<string:store_id>", methods=["DELETE"])
# def delete_store(store_id):
#     try:
#         del stores[store_id]
#         return {"message":"store deleted."}
#     except KeyError:
#         abort(404,message="store not found to delete.")


# @app.route("/item",methods=['POST'])
# def create_item():
#     item_data = request.get_json()    #json in data

#     if("price"not in item_data                #validation of payload
#        or "store_id"not in item_data 
#        or "name"not in item_data
#        ):
#         abort(400, message= "Bad request. ensure name store_id and price are include in JSON payload.")

#     for item in items.values():      #validation for item already exist in database.
#         if(item_data["name"] == item["name"] and
#            item_data["store_id"] == item["store_id"]
#            ):
#             abort(400, message = "Item already exists.")

#     if item_data["store_id"] not in stores:           #validation for store_id  in stores. if store_id is giving in payload. and that given id in payload will be checked in stores dict. if the store_id is present then only request get executed else abort.
#         # return {"message": "Store not found"}, 404
#         abort(404, message = "store not found")
    
#     item_id = uuid.uuid4().hex    
#     item = {**item_data, "id":item_id}
#     items[item_id] = item
#     return item,201

# @app.route("/item/<string:item_id>")
# def get_itemm(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         # return{"message":"item not found"}, 404
#         abort(404, message = "item not found")


# @app.route("/item/<string:item_id>", methods = ["DELETE"])
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"messgae":"item deleted successfully."}
#     except KeyError:
#         abort(404, message = "item not found.")
    

# @app.route("/item/<string:item_id>",methods = ["PUT"])
# def update_item(item_id):
#     item_data =request.get_json()
#     if "name" not in item_data or "price" not in item_data:
#         abort(400, message = "Bad request.ensure name and price are included in payload.")
#     try:
#         item = items[item_id]
#         item |= item_data
#     except KeyError:
#         abort(404, message = "item not found.")


# @app.route("/item")
# def get_item():
#     return {"items":list(items.values())}


# if __name__ == "__main__":
#     app.run(debug=True)



'''connect your flask app to blueprints and add swagger for documentation for your app. '''

from flask import Flask
from flask_smorest import Api

from resources.item import blp as ItemBlueprint
from resources.store import blp as StoreBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST_API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


api = Api(app)

api.register_blueprint(ItemBlueprint)
api.register_blueprint(StoreBlueprint)

