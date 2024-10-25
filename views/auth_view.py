from datetime import timedelta

from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    get_jwt,
    jwt_required
)

from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from app import db
from models import User
from schemas import UserSchema, MinimalUserSchema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.authorization
    username = data.username
    password = data.password
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(
        pwhash=user.password_hash, password=password
    ):
        access_toke = create_access_token(
            identity=username,
            expires_delta=timedelta(minutes=10),
            additional_claims=dict(
                admin=username.is_admin
            )
        )
        return jsonify({"Token": access_toke})
    return jsonify({"Error": "NO MATCH"})

@auth_bp.route("/users", methods=['POST', 'GET'])
def user():
    additional_data = get_jwt()
    print(additional_data)
    admin = additional_data.get('admin')
    
    if request.method == 'POST':
        if admin is True:
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")
        
            password_hasheed = generate_password_hash(
                password=password,
                method='pbkdf2',
                salt_length=8
            )
            try:
                new_user = User(
                    username=username,
                    password=password,
                    password_hash=password_hasheed
                )
                db.session.add(new_user)
                db.session.commit()
                
                return jsonify({"Usuario Creado": username}), 201
            except:
                return jsonify({"Error": "Algo salio mal"})
    
        return jsonify(mensagge="Usted no se encuentra habilitado para crear un usuario")
    
    users = User.query.all()
    print(admin is True)
    
    if admin is True:
        return UserSchema().dump(obj=users, many=True)
    else:
        return MinimalUserSchema().dump(obj=users, many=True)