from datetime import date
from app import ma
from marshmallow import validates, ValidationError, fields
from models import (
    User, Marca, Tipo_prenda, Local, Stock, Promocion, Prenda,
    Temporada, Color, Talle
)

# Schema para el modelo de Usuario
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

# Schema para Marca
class MarcaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Marca
        
    id = ma.auto_field()
    nombre = ma.auto_field()

# Schema para Tipo de Prenda
class Tipo_prendaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tipo_prenda
        
    id = ma.auto_field()
    nombre = ma.auto_field()

# Schema para Local
class LocalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Local
        
    id = ma.auto_field()
    nombre = ma.auto_field()

# Schema para Stock
class StockSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Stock
        
    id = ma.auto_field()
    cantidad = ma.auto_field()
    local_id = ma.auto_field()

# Schema para Promocion con validación en el descuento
class PromocionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Promocion
        
    id = ma.auto_field()
    descuento = ma.auto_field()

    @validates('descuento')
    def validate_descuento(self, value):
        if value < 0 or value > 100:
            raise ValidationError("El descuento debe estar entre 0 y 100.")
        return value

# Schema para Temporada
class TemporadaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Temporada
        
    id = ma.auto_field()
    nombre = ma.auto_field()

# Schema para Color
class ColorSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Color
        
    id = ma.auto_field()
    color = ma.auto_field()

# Schema para Talle
class TalleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Talle
        
    id = ma.auto_field()
    talle = ma.auto_field()

# Schema para Prenda
class PrendaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Prenda

    id = ma.auto_field()
    nombre = ma.auto_field(required=True)
    precio = ma.auto_field(required=True)
    
    # Relacionar con entidades relacionadas como strings
    color = fields.String(required=True)
    temporada = fields.String(required=True)
    marca = fields.String(required=True)

    @validates('precio')
    def validate_precio(self, value):
        if value <= 0:
            raise ValidationError("El precio debe ser mayor a cero.")
        return value
