from datetime import date

from app import ma

from models import (
    User,
    Marca,
    Tipo_prenda,
    Local,
    Stock,
    Promocion,
    Prenda,
    Temporada,
    Color,
    Talle
)
from marshmallow import validates, ValidationError, fields

class UserSchema(ma.SQLAlchemySchema):

    class Meta:
        model = User

    id = ma.auto_field()
    username = ma.auto_field()
    password_hash = ma.auto_field()
    is_admin = ma.auto_field()

class MinimalUserSchema(ma.SQLAlchemySchema):

    class Meta:
        model = User

    username = ma.auto_field()

class MarcaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Marca
        
    id = ma.auto_field()
    nombre = ma.auto_field()

class Tipo_prendaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tipo_prenda
        
    id = ma.auto_field()
    nombre = ma.auto_field()

class LocalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Local
        
    id = ma.auto_field()
    nombre = ma.auto_field()

class StockSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Stock
        
    id = ma.auto_field()
    cantidad = ma.auto_field()
    local_id = ma.auto_field()

class PromocionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Promocion
        
    id = ma.auto_field()
    descuento = ma.auto_field()

class TemporadaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Temporada
        
    id = ma.auto_field()
    nombre = ma.auto_field()

class ColorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Color
        
    id = ma.auto_field()
    color = ma.auto_field()

class TalleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Talle
        
    id = ma.auto_field()
    talle = ma.auto_field()

class PrendaSchema(ma.SQLAlchemySchema):
    stock_items = fields.Nested(StockSchema, many=True) # Crea un subdirectorio donde muestra el stock (dentro de prenda)
    marca_items = fields.Nested(MarcaSchema, many=True) # Crea un subdirectorio donde muestra la marca (dentro de prenda)
    class Meta:
        model = Prenda

    id = ma.auto_field()
    nombre = ma.auto_field()
    precio = ma.auto_field()
    talle_id = ma.auto_field()
    color_id = ma.auto_field()
    temporada_id = ma.auto_field()
    stock_id = ma.auto_field()
    marca_id = ma.auto_field()
    tipo_prenda_id = ma.auto_field()
    promocion_id = ma.auto_field()

    @validates('precio')
    def validate_precio(self, value):
        if value <= 0:
            raise ValidationError("El precio no es valido")
        return value
