import uuid
from flask import request
from flask.views import MethodView         #to create class and class methods
from flask_smorest import abort, Blueprint
from db import items


# Blueprint in flask_smorest is used to devide an API in multiple segments.

blp = Blueprint("items", __name__, description= "Operation on items.")

@blp.route("/item/<string:item_id>")
class Item(MethodView):
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


    def put(self,item_id):
        item_data =request.get_json()
        if "name" not in item_data or "price" not in item_data:
            abort(400, message = "Bad request.ensure name and price are included in payload.")
        try:
            item = items[item_id]
            item |= item_data
        except KeyError:
            abort(404, message = "item not found.")


@blp.route("/item")
class Itemlist(MethodView):

    def get(self):
        return {"items":list(items.values())}

    def post(self):
        item_data = request.get_json()    #json in data

        if("price"not in item_data                #validation of payload
        or "store_id"not in item_data 
        or "name"not in item_data
        ):
            abort(400, message= "Bad request. ensure name store_id and price are include in JSON payload.")

        for item in items.values():      #validation for item already exist in database.
            if(item_data["name"] == item["name"] and
            item_data["store_id"] == item["store_id"]
            ):
                abort(400, message = "Item already exists.")
        
        item_id = uuid.uuid4().hex    
        item = {**item_data, "id":item_id}
        items[item_id] = item
        return item