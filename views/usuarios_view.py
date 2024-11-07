from flask import Blueprint, request, jsonify
from app import db
from models import User
from schemas import UserSchema
from werkzeug.security import generate_password_hash

usuario_bp = Blueprint('usuarios', __name__)


temporary_password_storage = {}

@usuario_bp.route("/users/eliminar/<int:id>", methods=['DELETE'])
def eliminar_usuario(id):
    usuario = User.query.get(id)
    if usuario is None:
        return jsonify({'Error': 'No se encontró el usuario'}), 404
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({"message": "Se borró al usuario con éxito"}), 200

@usuario_bp.route("/users/actualizar/<int:id>", methods=['PUT'])
def actualizar_usuario(id):
    usuario = User.query.get(id)
    if usuario is None:
        return jsonify({"Error": "El usuario no pudo ser encontrado"}), 404
    data = request.get_json()


    usuario.username = data.get('username', usuario.username)
    

    if 'password' in data and data['password']:
        plain_password = data['password']
        usuario.password = generate_password_hash(plain_password)
        temporary_password_storage[usuario.id] = plain_password 

    db.session.commit()
    user_data = UserSchema().dump(usuario)
    user_data["password"] = temporary_password_storage.get(usuario.id, "Contraseña no disponible")
    return jsonify(user_data), 200

@usuario_bp.route("/users/detalle/<int:id>", methods=['GET'])
def obtener_usuario(id):
    usuario = User.query.get(id)
    if usuario is None:
        return jsonify({'Error': 'Usuario no encontrado'}), 404

  
    user_data = UserSchema().dump(usuario)
    user_data["password"] = temporary_password_storage.get(usuario.id, "Contraseña no disponible")
    
    return jsonify(user_data), 200

@usuario_bp.route("/users", methods=['GET'])
def obtener_usuarios():
    usuarios = User.query.all()
    user_schema = UserSchema(many=True)
    user_data = user_schema.dump(usuarios)
    return jsonify(user_data), 200
