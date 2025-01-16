import uuid
from flask import request
from flask.views import MethodView         #to create class and class methods
from flask_smorest import abort, Blueprint
from db import stores


# Blueprint in flask_smorest is used to devide an API in multiple segments.

blp = Blueprint("stores", __name__, description= "Operation on stores.")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message = "store not found")


    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message":"store deleted."}
        except KeyError:
            abort(404,message="store not found to delete.")


@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores":list(stores.values())}

    def post(self):
        store_data = request.get_json()
        if "name" not in store_data:          #validation check for name is given or not in payload.
            abort(400, message = "Bad request. Ensure name icluded in JSON payload.")

        for store in stores.values():       #validation for store name already present or not.
            if store_data["name"] == store["name"]:
                abort(400, message= "Store name already exists.") 

        store_id = uuid.uuid4().hex                #(universal unique id)
        store = {**store_data, "id":store_id}
        stores[store_id] = store            #add newly created store in stores dict with store_id as key and store(with all data) as a value.
        return store
    

        