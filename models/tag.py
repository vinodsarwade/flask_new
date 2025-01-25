from REST_API_ROLF.db import db


class TagModel(db.Model):
    __tablename__ = "tags"                    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    store_id = db.Column(db.String(), db.ForeignKey("stores.id"), nullable=False)
    
    #onr-many (tag associated to store, return store)
    store = db.relationship("StoreMotagsdel", back_populates="")

    #many-many relatonship
    items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")