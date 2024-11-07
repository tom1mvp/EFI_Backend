from flask import Blueprint, request, make_response, jsonify
from app import db
from models import Prenda, Marca, Temporada, Color, Promocion  # Eliminé Tipo_prenda porque no parece usarse
from schemas import PrendaSchema

prenda_bp = Blueprint('prendas', __name__)

# Obtener todas las prendas (nueva ruta GET)
@prenda_bp.route("/prenda", methods=['GET'])
def obtener_prendas():
    try:
        prendas = Prenda.query.all()
        return jsonify(PrendaSchema(many=True).dump(prendas)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Crear una nueva prenda
@prenda_bp.route("/prenda", methods=['POST'])
def crear_prenda():
    data = request.get_json()
    errors = PrendaSchema().validate(data)
    
    if errors:
        return make_response(jsonify(errors), 400)

    try:
        # Obtener o crear cada entidad relacionada por su nombre
        marca = Marca.query.filter_by(nombre=data['marca']).first()
        if not marca:
            marca = Marca(nombre=data['marca'])
            db.session.add(marca)
        
        temporada = Temporada.query.filter_by(nombre=data['temporada']).first()
        if not temporada:
            temporada = Temporada(nombre=data['temporada'])
            db.session.add(temporada)
        
        color = Color.query.filter_by(color=data['color']).first()
        if not color:
            color = Color(color=data['color'])
            db.session.add(color)
        
        promocion = None
        if 'promocion' in data:
            promocion = Promocion.query.filter_by(descuento=data['promocion']).first()
            if not promocion:
                promocion = Promocion(descuento=data['promocion'])
                db.session.add(promocion)

        # Crear el registro de Prenda
        nueva_prenda = Prenda(
            nombre=data['nombre'],
            precio=data['precio'],
            color=color,
            temporada=temporada,
            marca=marca,
        )

        db.session.add(nueva_prenda)
        db.session.commit()
        return jsonify(PrendaSchema().dump(nueva_prenda)), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Actualizar una prenda existente
@prenda_bp.route("/prenda/actualizar/<int:id>", methods=['PUT'])
def actualizar_prenda(id):
    prenda = Prenda.query.get(id)
    
    if not prenda:
        return jsonify({"Error": "Prenda no encontrada"}), 404
    
    data = request.get_json()
    errors = PrendaSchema().validate(data, partial=True)  # Permitir actualizaciones parciales
    if errors:
        return make_response(jsonify(errors), 400)

    try:
        # Actualizar entidades relacionadas por nombre si existen en los datos
        if 'marca' in data:
            marca = Marca.query.filter_by(nombre=data['marca']).first()
            if not marca:
                marca = Marca(nombre=data['marca'])
                db.session.add(marca)
            prenda.marca = marca
        
        if 'temporada' in data:
            temporada = Temporada.query.filter_by(nombre=data['temporada']).first()
            if not temporada:
                temporada = Temporada(nombre=data['temporada'])
                db.session.add(temporada)
            prenda.temporada = temporada
        
        if 'color' in data:
            color = Color.query.filter_by(color=data['color']).first()
            if not color:
                color = Color(color=data['color'])
                db.session.add(color)
            prenda.color = color

        # Actualizar campos directamente si existen en los datos
        prenda.nombre = data.get('nombre', prenda.nombre)
        prenda.precio = data.get('precio', prenda.precio)

        db.session.commit()
        return jsonify(PrendaSchema().dump(prenda)), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Eliminar una prenda por ID
@prenda_bp.route("/prenda/eliminar/<int:id>", methods=['DELETE'])
def eliminar_prenda(id):
    prenda = Prenda.query.get(id)
    
    if not prenda:
        return jsonify({"Error": "Prenda no encontrada"}), 404
    
    try:
        db.session.delete(prenda)
        db.session.commit()
        return jsonify({"message": "Prenda eliminada con éxito"}), 200
    except:
        return jsonify({"Error": "No se pudo eliminar la prenda"}), 500
