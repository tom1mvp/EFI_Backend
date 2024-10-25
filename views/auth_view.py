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
            expires_delta=timedelta(minutes=100),
            additional_claims=dict(
                admin=user.is_admin
            )
        )
        return jsonify({"Token": access_toke})
    return jsonify({"Error": "NO MATCH"})

@auth_bp.route("/users", methods=['POST', 'GET'])
@jwt_required()
def user():
    additional_data = get_jwt()
    admin = additional_data.get('admin')
    
    if request.method == 'POST':
        if admin is True:
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")
            is_admin = data.get("isAdmin", False)  # Obtener isAdmin del body

            # Verifica si el nombre de usuario ya existe
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                return jsonify({"Error": "El nombre de usuario ya existe"}), 400

            password_hash = generate_password_hash(
                password=password,
                method='pbkdf2',
                salt_length=8
            )
            try:
                new_user = User(
                    username=username,
                    password_hash=password_hash,  # Solo almacenar el hash
                    is_admin=is_admin  # Almacenar el valor de isAdmin
                )
                db.session.add(new_user)
                db.session.commit()
                
                return jsonify({"Usuario Creado": username}), 201
            except Exception as e:
                print(f"Error al crear el usuario: {e}")
                return jsonify({"Error": "Algo salió mal"}), 500

    
        return jsonify({"Mensaje": "Usted no se encuentra habilitado para crear un usuario"}), 403
    
    # Manejo para GET
    users = User.query.all()
    return UserSchema().dump(obj=users, many=True)