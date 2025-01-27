'''flask operation using list(get, post items in list)'''
import os
import secrets
from flask import Flask, jsonify
from flask_smorest import Api
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

from REST_API_ROLF.resources.item import blp as ItemBlueprint 
from REST_API_ROLF.resources.store import blp as StoreBlueprint
from REST_API_ROLF.resources.tag import blp as TagBlueprint
from REST_API_ROLF.resources.user import blp as UserBlueprint

from REST_API_ROLF.db import db
import REST_API_ROLF.models
from REST_API_ROLF.block_list import BLOCKLIST

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


def create_app(db_url=None):        #factory pattern
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST_API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL","sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)  #connect app to database


    migrate = Migrate(app, db)
 
    '''****************'''
    with app.app_context():  #if you have to run migration then comment this.
        db.create_all()      
    '''*****************'''   


    api = Api(app)          #connect your app to flask_smorest

    # app.config["JWT_SECRET_KEY"] = secrets.SystemRandom().getrandbits(128)
    app.config["JWT_SECRET_KEY"] = "Vinod"
    jwt = JWTManager(app)               #connect app to JWT



    '''#when we get jwt this fun will run and check if the token is in BLOCKLST or not
    #if it returns true then request is terminated. user get message "token has revoked." '''
    @jwt.token_in_blocklist_loader
    def check_if_token_in_blocklist(jwt_header, jwt_payload):
        return jwt_payload["jti"] in BLOCKLIST
    

    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return(jsonify({"description":"the token has revoked","error":"token_revoked"}),401)



    '''when we expect fresh token but if you get refresh token
      it will check out through this below if it is not correct then fun will give error.'''
    
    @jwt.needs_fresh_token_loader
    def token_not_fresh_callback(jwt_header, jwt_payload):
        return(jsonify({"description":"The token is not fresh",
                        "error":"Fresh token required"}),401)




    '''below are the error handling for jwt. if we got an error then we can use like below to add description to error msg
      which is optional. jwt gives you error msgs. but just for description  '''
    
    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return(jsonify({"message":"token has been expired", "error":"token_expired"}),401)

    @jwt.invalid_token_loader
    def invalid_token_loader(error):
        return(jsonify({"message":"signature verification failed","error":"Invalid_token"}),401)
    
    @jwt.unauthorized_loader
    def missing_token_callback(error):
        return(jsonify({"description":"Request does not contains an access token",
                        "error":"authorization required"}),401)


    api.register_blueprint(ItemBlueprint)
    api.register_blueprint(StoreBlueprint)
    api.register_blueprint(TagBlueprint)
    api.register_blueprint(UserBlueprint)

    return app

