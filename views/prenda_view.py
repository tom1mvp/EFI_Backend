from flask import Blueprint, request, make_response, jsonify
from app import db

from models import Marca, Prenda, Tipo_prenda
from schemas import MarcaSchema, PrendaSchema, Tipo_prendaSchema


prenda_bp = Blueprint('prendas', __name__)

@prenda_bp.route('/marcas', methods=['GET'])
def mostrar_marcas():
    marca_nombre = request.args.get('marca_nombre')

    if marca_nombre:
        buscar_marca = Marca.query.filter_by(nombre=marca_nombre).first()
        if buscar_marca:
            return MarcaSchema().dump(buscar_marca), 201
        else:
            return jsonify({"Error": "Marca no encontrada"}), 404

    marcas = Marca.query.all()
    return MarcaSchema(many=True).dump(marcas)

@prenda_bp.route('/marcas/crear', methods=['POST'])
def crear_marca():
    data = request.get_json()
    nueva_marca = Marca(nombre=data['nombre'])
    
    db.session.add(nueva_marca)
    db.session.commit()
    
    return MarcaSchema().dump(nueva_marca), 201

@prenda_bp.route('/marcas/eliminar/<int:id>', methods=['POST'])
def eliminar_marca(id):
    marca = Marca.query.get(id)
    
    if marca is None:
        return jsonify({'Error': 'No se encontró la marca'}), 404
    else:
        db.session.delete(marca)
        db.session.commit()
        
        return jsonify({"message": "Se borró la marca con éxito"}), 200

@prenda_bp.route('/marcas/actualizar/<int:id>', methods=['POST'])
def actualizar_marca(id):
    marca = Marca.query.get(id)
    
    if marca is None:
        return jsonify({"Error": "Marca no encontrada"}), 404
    else:
        data = request.get_json()
        marca.nombre = data.get('nombre', marca.nombre)
        
        db.session.commit()
        return MarcaSchema().dump(marca)

@prenda_bp.route('/tipo',  methods=['GET'])
def mostrar_tipo_prendas():
    
    tipo_prenda_nombre = request.args.get('tipo_prenda_nombre')
    
    if tipo_prenda_nombre:
        buscar_tipo_prenda = Tipo_prenda.query.filter_by(nombre=tipo_prenda_nombre).first()
        if buscar_tipo_prenda:
            return Tipo_prendaSchema.dump(buscar_tipo_prenda)
        else:
            return jsonify({"Error": "Tipo de prenda no encontrada"}), 404
    
    tipo_prenda = Tipo_prenda.query.all()
    return Tipo_prendaSchema().dump(tipo_prenda, many=True)

@prenda_bp.route('/tipo/crear', methods=['POST'])
def crear_tipo():
    data = request.get_json()
    nuevo_tipo = Tipo_prenda(nombre=data['nombre'])
    
    db.session.add(nuevo_tipo)
    db.session.commit()
    
    return Tipo_prendaSchema().dump(nuevo_tipo), 201

@prenda_bp.route('/tipo/<int:id>', methods=['POST'])
def eliminar_tipo_prenda(id):
    tipo_prenda = Tipo_prenda.query.get(id)
    
    if tipo_prenda is None:
         return jsonify({'Error': 'No se encontró el tipo de prenda'}), 404
    else:
        db.session.delete(tipo_prenda)
        db.session.commit()
        return jsonify({"message": "Se borró el tipo de prenda con éxito"}), 200

@prenda_bp.route('/tipo/<int:id>', methods=['POST'])
def actualizar_tipo_prenda(id):
    tipo_prenda = Tipo_prenda.query.get(id)
    
    if tipo_prenda is None:
        return jsonify({"Error": "Tipo de prenda no encontrada"}), 404
    else:
        data = request.get_json()
        tipo_prenda.nombre = data.get('nombre', tipo_prenda.nombre)
        
        db.session.commit()
        return MarcaSchema().dump(tipo_prenda)

@prenda_bp.route("/prenda", methods=['GET'])
def mostrar_prenda():
    
    prenda_nombre = request.args.get('prenda_nombre')
    
    if prenda_nombre:
        buscar_prenda = Prenda.query.filter_by(nombre=prenda_nombre).first()
        if buscar_prenda:
            return PrendaSchema().dump(buscar_prenda)
        else:
            return jsonify({"Error": "La prenda buscada no  fue encontrada"}), 404
    prenda = Prenda.query.all()
    return PrendaSchema().dump(prenda)

@prenda_bp.route("/prenda/crear", methods=['POST'])
def crear_prenda():
    data = request.get_json()
    nueva_prenda = Prenda(nombre=data['nombre'])
    
    db.session.add(nueva_prenda)
    db.session.commit()
    
    return PrendaSchema().dump(nueva_prenda), 201

@prenda_bp.route("/prenda/<int:id>", methods=['POST'])
def eliminar_prenda(id):
    prenda = prenda.query.get(id)
    
    if prenda is None:
        return jsonify({'Error': 'No se encontró la prenda'}), 404
    else:
        db.session.delete(prenda)
        db.session.commit()
        return jsonify({"message": "Se borró la prenda con éxito"}), 200

@prenda_bp.route("/prenda/<int:id>", methods=['POST'])
def actualizar_prenda(id):
    prenda = Prenda.query.get(id)
    
    if prenda is None:
          return jsonify({"Error": "La prenda no fue encontrada"}), 404
    else:
        data = request.get_json()
        prenda.nombre = data.get('nombre', prenda.nombre)
        
        db.session.commit()
        return MarcaSchema().dump(prenda)