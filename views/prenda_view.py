from flask import Blueprint, request, make_response, jsonify
from app import db

from models import Marca, Prenda, Tipo_prenda
from schemas import MarcaSchema, PrendaSchema, Tipo_prendaSchema


prenda_bp = Blueprint('prendas', __name__)

@prenda_bp.route('/marcas',  methods=['GET'])
def mostrar_marcas():
    marcas = Marca.query.all()
    return MarcaSchema().dump(marcas, many=True)
	
@prenda_bp.route('/tipo',  methods=['GET'])
def mostrar_tipo_prendas():
    tipo_prenda = Tipo_prenda.query.all()
    return Tipo_prendaSchema().dump(tipo_prenda, many=True)

@prenda_bp.route("/prenda", methods=['GET', 'POST'])
def prenda():
    if request.method == "POST":
        data = request.get_json()
        errors = PrendaSchema().validate(data)
        
        if errors:
            return make_response(jsonify(errors))
        
        nueva_prenda = Prenda (
			name = data.get('nombre_prenda'),
			precio = data.get('precio_prenda')
		)
        
        