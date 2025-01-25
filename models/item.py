from REST_API_ROLF.db import db

#sqlalchemy is used to turning table rows/column in to python object.(ORM)

class ItemModel(db.Model):
    __tablename__ = "items"                    #create table called "Items" for this object of class.

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float, unique=False, nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)

    #one-many
    store = db.relationship("StoreModel", back_populates="items")

    #many-many
    tags = db.relationship("TagModel", back_populates="items", secondary="items_tags")  #secondary is used to add many-many relationship between 2 columns.