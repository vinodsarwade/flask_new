# from marshmallow import Schema,fields

# class ItemSchema(Schema):
#     id = fields.Str(dump_only=True)      #dump_only used to send data only. not used for validation.
#     name = fields.Str(required=True)
#     price = fields.Float(required= True)
#     store_id = fields.Str(required=True)

# class ItemUpdateSchema(Schema):
#     name = fields.Str()
#     price = fields.Float()


# class StoreSchema(Schema):
#     id = fields.Str(dump_only=True)
#     name = fields.Str(required=True)


'''for adding schemas to db. we are doing some changes bcz we have 1:N relationship from both items and stores table.'''
#if you have to use dict as a database then uncomment above


from marshmallow import Schema, fields

class PlainItemSchema(Schema):
    id = fields.Int(dump_only=True)      #dump_only used to send data only. not used for validation.
    name = fields.Str(required=True)
    price = fields.Float(required= True)


class PlainStoreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class PlainTagSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int()


class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)  #it is used for imput but not included in output.
    store = fields.Nested(PlainStoreSchema(), dump_only=True) #it will be included in output but cannot be used for input.
    tags = fields.List(fields.Nested(PlainTagSchema()),dump_only=True)


class StoreSchema(PlainStoreSchema): #This schema extends PlainStoreSchema to include relationships with items and tags. It represents a store and its associated data.
    items = fields.List(fields.Nested(PlainItemSchema()),dump_only=True)
    tags = fields.List(fields.Nested(PlainTagSchema()),dump_only=True)



class TagSchema(PlainTagSchema):
    store_id = fields.Int(load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    items = fields.List(fields.Nested(PlainItemSchema()),dump_only=True)



class TagAndItemSchema(Schema):
    message = fields.Str()
    item = fields.Nested(ItemSchema)
    tags = fields.Nested(TagSchema)



class UserSchema(Schema):
    id = fields.Int(dump_only= True)   #id dont need while loging but in output it will get
    username = fields.Str(required=True)
    password = fields.Str(required=True,load_only=True)     #password is used only for input/payload/logging but it will not return pasword.