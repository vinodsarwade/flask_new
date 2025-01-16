from REST_API_ROLF.db import db

class StoreModel(db.model):
    __tablename__ = "stores"                    #create table called "Items" for this object of class.

    id = db.Column(db.Interger, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
   