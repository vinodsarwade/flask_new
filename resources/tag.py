from flask.views import MethodView  
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError

from REST_API_ROLF.db import db
from REST_API_ROLF.models import TagModel,StoreModel,ItemModel,ItemTags
from REST_API_ROLF.marshmallow_schema import TagSchema,TagAndItemSchema


blp = Blueprint("tags", __name__, description= "Operation on tags.")


@blp.route("/store/<string:store_id>/tag")
class TagInStore(MethodView):
    @blp.response(200, TagSchema(many=True))
    def get(self, store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store.tags.all()


    @blp.arguments(TagSchema)                 #payload validation using schema
    @blp.response(200, TagSchema)             #get responce from schema
    def post(self, tag_data, store_id):       #save payload in tag_data
        tag = TagModel(**tag_data, store_id=store_id)
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))
        
        return tag


#link the items to tag
@blp.route("/item/<string:item_id>/tag/<string:tag_id>")
class LinkTagsToItem(MethodView):
    @blp.response(201, TagSchema)
    def post(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)    #find or validate item_id and tag_id are present or not.
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.append(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message= "an error occured while inserting tag.")
        
        return tag


#unlink the items from tag
    @blp.response(201, TagAndItemSchema)
    def delete(self, item_id, tag_id):
        item = ItemModel.query.get_or_404(item_id)    #find or validate item_id and tag_id are present or not.
        tag = TagModel.query.get_or_404(tag_id)

        item.tags.remove(tag)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occured while deleting the tag")

        return {"message":"Item removed from tag", "item":item, "tag":tag}




@blp.route("/tag/<string:tag_id>")
class Tag(MethodView):
    @blp.response(200, TagSchema)
    def get(self, tag_id):
        try:
            tag = TagModel.query.get_or_404(tag_id)
        except Exception as e:
            abort(404, message=f"Tag with ID {tag_id} not found: {str(e)}")
        return tag



    #below are the extra responces we can add to your route if you needed.
    @blp.response(202, description="Deletes a tag if no item is tagged with it.",
                  example={"message":"Tag deleted"})
    
    @blp.alt_response(404, description="Tag not found")
    @blp.alt_response(400,description="Returned if the tag is assigned to one or more items. in this case the tag is not deleted.")



    def delete(self, tag_id):
        tag = TagModel.query.get_or_404(tag_id)

        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return{"message":"Tag deleted"}
        abort(400, messgae="Could not delete tag. Make sure tag is not associated with any items, try again.")