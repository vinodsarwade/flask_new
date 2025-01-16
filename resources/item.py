import uuid
from flask import request
from flask.views import MethodView  ##to create class and class methods
from flask_smorest import abort, Blueprint

from REST_API_ROLF.db import items
from REST_API_ROLF.marshmallow_schema import ItemSchema ,ItemUpdateSchema


# Blueprint in flask_smorest is used to devide an API in multiple segments.

blp = Blueprint("items", __name__, description= "Operation on items.")

# @blp.route("/item/<string:item_id>")
# class Item(MethodView):
#     def get(self, item_id):
#         try:
#             return items[item_id]
#         except KeyError:
#             abort(404, message = "item not found")
    

#     def delete(self, item_id):
#         try:
#             del items[item_id]
#             return{"messgae":"item deleted successfully."}
#         except KeyError:
#             abort(404, message = "item not found.")


#     def put(self,item_id):
#         item_data =request.get_json()
#         if "name" not in item_data or "price" not in item_data:
#             abort(400, message = "Bad request.ensure name and price are included in payload.")
#         try:
#             item = items[item_id]
#             item |= item_data
#         except KeyError:
#             abort(404, message = "item not found.")


# @blp.route("/item")
# class Itemlist(MethodView):

#     def get(self):
#         return {"items":list(items.values())}

#     def post(self):
#         item_data = request.get_json()    #json in data

#         if("price"not in item_data                #validation of payload
#         or "store_id"not in item_data 
#         or "name"not in item_data
#         ):
#             abort(400, message= "Bad request. ensure name store_id and price are include in JSON payload.")

#         for item in items.values():      #validation for item already exist in database.
#             if(item_data["name"] == item["name"] and
#             item_data["store_id"] == item["store_id"]
#             ):
#                 abort(400, message = "Item already exists.")
        
#         item_id = uuid.uuid4().hex    
#         item = {**item_data, "id":item_id}
#         items[item_id] = item
#         return item


'''adding marshmallow for validation of client input(incoming data ie. payload)
ex: when we hit post request we send a payload this payload will be checked by schemas.if true then only 
validation done. here we don't require "request.get_json" to store and use data.
marshmallow autometically take data validate it and then pass in function.'''


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message = "item not found")
    

    def delete(self, item_id):
        try:
            del items[item_id]
            return{"messgae":"item deleted successfully."}
        except KeyError:
            abort(404, message = "item not found.")


    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self,item_data, item_id):       #after validation used that data in item_data.
        # item_data =request.get_json()
        try:
            item = items[item_id]
            item |= item_data         
        except KeyError:
            abort(404, message = "item not found.")


@blp.route("/item")
class Itemlist(MethodView):
    @blp.response(200,ItemSchema(many=True))
    def get(self):
        # return {"items":list(items.values())}
        return items.values()


    @blp.arguments(ItemSchema)
    @blp.response(200, ItemSchema)
    def post(self, item_data):    #same as request.get_json. Itemschema will validate item data and we used item_data var as a argumet which has schema validated data to your request.
        # item_data = request.get_json()   
        for item in items.values():      #validation for item already exist in database.
            if(item_data["name"] == item["name"] and
            item_data["store_id"] == item["store_id"]
            ):
                abort(400, message = "Item already exists.")
        
        item_id = uuid.uuid4().hex    
        item = {**item_data, "id":item_id}
        items[item_id] = item
        return item