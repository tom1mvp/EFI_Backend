from datetime import timedelta
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
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
    
    if user and check_password_hash(pwhash=user.password_hash, password=password):
        access_token = create_access_token(
            identity=username,
            expires_delta=timedelta(minutes=100),
            additional_claims={"admin": user.is_admin}
        )
        return jsonify({"Token": access_token}), 200
    
    return jsonify({"Error": "No se encontró coincidencia"}), 401

@auth_bp.route("/users", methods=['POST', 'GET'])
@jwt_required()
def user():
    additional_data = get_jwt()
    admin = additional_data.get('admin')

    if request.method == 'POST':
        if not admin:
            return jsonify({"Mensaje": "No tiene permiso para crear usuarios"}), 403

        try:
            data = request.get_json()
            username = data.get("username")
            password = data.get("password")
            is_admin = data.get("isAdmin", False)  # Considera cambiar a is_admin en el frontend también

            # Verificar existencia de usuario
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                return jsonify({"Error": "El nombre de usuario ya existe"}), 400

            # Crear hash de contraseña
            password_hash = generate_password_hash(password=password, method='pbkdf2', salt_length=8)

            # Crear nuevo usuario
            new_user = User(username=username, password_hash=password_hash, is_admin=is_admin)
            db.session.add(new_user)
            db.session.commit()

            return jsonify({"Usuario Creado": username}), 201

        except Exception as e:
            return jsonify({"Error": "Error interno al crear el usuario"}), 404

    elif request.method == 'GET':
        try:
            users = User.query.all()
            if admin:
                return jsonify(UserSchema().dump(users, many=True)), 201
            else:
                return jsonify(MinimalUserSchema().dump(users, many=True)), 201
        except Exception as e:
            return jsonify({"Error": "Error interno al obtener los usuarios"}), 404