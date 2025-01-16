from REST_API_ROLF.db import db

#sqlalchemy is used to turning table rows to python object.

class ItemModel(db.model):
    __tablename__ = "items"                    #create table called "Items" for this object of class.

    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.float(Precision=2), unique=False, nullable=False)
    store_id = db.Column(db.Integer, unique=False, nullable=False)