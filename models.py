from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password_hash = db.Column(db.String(300), nullable=False)
    is_admin = db.Column(db.Boolean(0))
    
    def __str__(self):
        return self.username

class Marca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre =  db.Column(db.String(50), nullable=False)
    
    def __str__(self):
        return self.nombre

class Tipo_prenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    
    def __str__(self):
        return f"Tipo prenda{self.nombre}"
    
class Local(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __str__(self):
        return f"Local {self.nombre}"

class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    activo = db.Column(db.Boolean(0))


    
    local_id = db.Column(db.Integer, db.ForeignKey('local.id'), nullable=False)

    local = db.relationship('Local', backref=db.backref('stock', lazy=True))

    def __str__(self):
        return self.cantidad
    
class Promocion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descuento = db.Column(db.Integer)

    def __str__(self):
        return self.descuento
    
class Temporada(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre =  db.Column(db.String(20), nullable=False)
    
    def __str__(self):
        return self.nombre
    
class Color(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color =  db.Column(db.String(20), nullable=False)
    
    def __str__(self):
        return self.color
    
class Talle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    talle = db.Column(db.String(5), nullable=False)
    
    def __str__(self):
        return self.talle
    
class Prenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Integer)

    talle_id = db.Column(db.Integer, db.ForeignKey('talle.id'), nullable=False)
    color_id = db.Column(db.Integer, db.ForeignKey('color.id'), nullable=False)
    temporada_id = db.Column(db.Integer, db.ForeignKey('temporada.id'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)
    marca_id = db.Column(db.Integer, db.ForeignKey('marca.id'), nullable=False)
    tipo_prenda_id = db.Column(db.Integer, db.ForeignKey('tipo_prenda.id'), nullable=False)
    promocion_id = db.Column(db.Integer, db.ForeignKey('promocion.id'), nullable=False)

    talle = db.relationship('Talle', backref=db.backref('prenda', lazy=True))
    color = db.relationship('Color', backref=db.backref('prenda', lazy=True))
    temporada = db.relationship('Temporada', backref=db.backref('prenda', lazy=True))
    stock = db.relationship('Stock', backref=db.backref('prenda', lazy=True))
    marca = db.relationship('Marca', backref=db.backref('prenda', lazy=True))
    tipo_prenda = db.relationship('Tipo_prenda', backref=db.backref('prenda', lazy=True))
    promocion = db.relationship('Promocion', backref=db.backref('prenda', lazy=True))

