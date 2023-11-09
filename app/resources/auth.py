from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services import UserService
from app.mapping.user_schema import UserSchema


auth = Blueprint('auth', __name__)
user_service = UserService()
user_schema = UserSchema()

@auth.route('/register', methods=['POST'])
def register_user():
    name = request.json.get("name", None)
    password = request.json.get("password", None)
    service = UserService()

    if service.find_by_username(name):
        return jsonify({"error": "Username already exists"}), 400

    new_user = service.create(name, password)
    return jsonify(user_schema.dump(new_user)), 201

@auth.route('/login', methods=['POST'])
def login():
    name = request.json.get("name", None)
    password = request.json.get("password", None)
    service = UserService()
    
    if service.check_auth(name,password):
        user = service.find_by_name(name)
        list_roles = [role.name for role in user.roles] #TODO: PROBLEMA
        
        access_token = create_access_token(user_schema.dump(user), additional_claims={"roles": list_roles})
        return jsonify[{"token": access_token, "id": user.id}]

@auth.route('/logout', methods=['POST'])
def logout():
    user_service.logout_user()
    return {"message": "Usuario deslogueado"}, 200