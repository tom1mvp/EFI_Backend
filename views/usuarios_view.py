from flask import Blueprint, request, make_response, jsonify
from app import db

from models import User
from schemas import UserSchema

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route("/usuarios", methods=['GET'])
def mostrar_usuario():
    usuario_nombre = request.args.get('usuario_nombre')
    
    if usuario_nombre:
        buscar_usuario = User.query.filter_by(username=usuario_nombre).first()
        if buscar_usuario:
            return UserSchema().dump(buscar_usuario), 201
        else:
            return jsonify({"Error": "Usuario no encontrado"}), 404
    
    usuario = User.query.all()
    return UserSchema(many=True).dump(usuario), 200

@usuario_bp.route("/usuarios/crear", methods=['POST'])
def crear_usuario():
    data = request.get_json()
    nuevo_usuario = User(username=data['username'])
    
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    return UserSchema().dump(nuevo_usuario), 201

@usuario_bp.route("/usuarios/eliminar/<int:id>", methods=['POST'])
def eliminar_usuario(id):
    usuario = User.query.get(id)

    if usuario is None:
        return jsonify({'Error': 'No se encontró el usuario'}), 404
    else:
        db.session.delete(usuario)
        db.session.commit()
        
        return jsonify({"message": "Se borró al usuario con éxito"}), 200

@usuario_bp.route("/usuario/actualizar/<int:id>", methods=['POST'])
def actualizar_usuario(id):
    usuario = User.query.get(id)
    
    if usuario is None:
        return jsonify({"Error": "El usuario no pudo ser encontrado"}), 404
    
    data = request.get_json()
    usuario.username = data.get('username', usuario.username)
    
    db.session.commit()
    return jsonify(UserSchema().dump(usuario)), 200
