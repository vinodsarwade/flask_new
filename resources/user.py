from flask.views import MethodView  
from flask_smorest import abort, Blueprint
from sqlalchemy.exc import SQLAlchemyError
from passlib.hash import pbkdf2_sha256          #hashing pass
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity,jwt_required, get_jwt #creating access token for jwt.

from REST_API_ROLF.db import db
from REST_API_ROLF.models import UserModel
from REST_API_ROLF.marshmallow_schema import UserSchema
from REST_API_ROLF.block_list import BLOCKLIST


blp = Blueprint("users", __name__, description= "Operation on users.")


@blp.route("/register")
class UserRegister(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(UserModel.username == user_data['username']).first():
            abort(409, message ="A user with that username already exist.")

        user = UserModel(
            username = user_data["username"],
            password = pbkdf2_sha256.hash(user_data["password"])
        )
        db.session.add(user)
        db.session.commit()
        return {"message":"user created successfully."}, 201
    


@blp.route("/login")
class Userlogin(MethodView):
    @blp.arguments(UserSchema)
    def post(self, user_data):
        user = UserModel.query.filter(UserModel.username == user_data["username"]).first()

        if user and pbkdf2_sha256.verify(user_data["password"], user.password):
            access_token = create_access_token(identity=str(user.id),fresh=True)       #identity must be an string bcz in access token sub param is getting only data which is type of string. otherwise you get an error"sub must be string"
            refresh_token = create_refresh_token(identity=str(user.id))
            return {"access_token": access_token, "refresh_token": refresh_token}
        abort(401, message="Invalid credentials")



'''when you need to hit /refresh route you need refresh token which you get once login.
refresh token is used bcz, each access token has expiry so everytime you need to log in again for access token and hit a request.
but adding refresh token to route we can get info every time.
when an access token has expired everytime a client generate refresh token. 
but if you want to set a limit how many times refresh token will be generate ,for that we can use BLOCKLIST.
refresh token will generate only once here then added to BLOCKLIST.next time if you hit route then will get error.'''

@blp.route("/refresh")
class Tokenrefresh(MethodView):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        new_token = create_access_token(identity=current_user, fresh=False)

        jti = get_jwt()["jti"]     #generate refresh token only once./expiry time only once.
        BLOCKLIST.add(jti)

        return{"access_token":new_token}




'''to call this endpoint you need access token. you can get access token after login only.
once you hit/logout it will logged you out. and store that access token in BLOCKLIST file.
after you logout you can not access endpoint which required JWT.still if you try to access any route
in app.py file {'token_in_blocklist_loader'}check if the token is present or not in BLOCKLIST.if present
return true and terminate the request. if you need to access then you need to log in again and get token.'''

@blp.route("/logout")
class UserLogout(MethodView):
    @jwt_required()
    def post(self):
        jti = get_jwt()["jti"]
        BLOCKLIST.add(jti)
        return {"message":"Successfully logged out"}


@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user
    
    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message":"user deleted successfully"},200