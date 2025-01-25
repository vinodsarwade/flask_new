from REST_API_ROLF.db import db

class StoreModel(db.Model):
    __tablename__ = "stores"                    #create table called "stores" for this object of class.

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
   
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade = "all, delete")   
    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")


    #cascade is used to delete all items in store when store gets deleted.
    #if store deleted then it's all items are get deleted. 
    
    '''without creating an store we can create an item but it's store is null.bcz SQLITE supports that feature.
    but in good practice first create store then add items in store by giving store_id, means all items are added in that store.
    but if we create an item without creating an store then we can't delete that store.need to delete item using item_id.
    
    so cascade deleting is used to delete all the children items when parent item in deleted. i.e: if store gets deletd then it's all items are auto deleted.
    '''
