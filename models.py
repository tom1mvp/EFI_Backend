from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(300), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    
    def _str_(self):
        return self.username


class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    
    def _str_(self):
        return self.nombre


class Tipo_prenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    
    def _str_(self):
        return f"Tipo prenda {self.nombre}"
    

class Local(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def _str_(self):
        return f"Local {self.nombre}"


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    activo = db.Column(db.Boolean, default=False)

    local_id = db.Column(db.Integer, db.ForeignKey('local.id'), nullable=False)
    local = db.relationship('Local', backref=db.backref('stock', lazy=True))

    def _str_(self):
        return str(self.cantidad)


class Promocion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descuento = db.Column(db.Integer)

    def _str_(self):
        return str(self.descuento)


class Temporada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)
    
    def _str_(self):
        return self.nombre


class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(20), nullable=False)
    
    def _str_(self):
        return self.color


class Talle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    talle = db.Column(db.String(5), nullable=False)
    
    def _str_(self):
        return self.talle

class Prenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)

    # Foreign key relationships
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    temporada_id = db.Column(db.Integer, db.ForeignKey('temporada.id'), nullable=False)

    # Relationships
    color = db.relationship('Color', backref=db.backref('prendas', lazy=True))
    marca = db.relationship('Marca', backref=db.backref('prendas', lazy=True))
    temporada = db.relationship('Temporada', backref=db.backref('prendas', lazy=True))

    def _str_(self):
        return f"{self.nombre} - {self.marca.nombre} - {self.color.color} - {self.temporada.nombre}"


    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'precio': self.precio,
            'talle': self.talle.talle if self.talle else None,
            'color': self.color.color if self.color else None,
            'temporada': self.temporada.nombre if self.temporada else None,
            'stock': self.stock.cantidad if self.stock else None,
            'marca': self.marca.nombre if self.marca else None,
            'tipo_prenda': self.tipo_prenda.nombre if self.tipo_prenda else None,
            'promocion': self.promocion.descuento if self.promocion else None
        }