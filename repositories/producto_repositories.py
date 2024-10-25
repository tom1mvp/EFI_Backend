from app import db

from models import Marca,Tipo_prenda,Stock

class MarcaRepository:
    def get_all(self):
        return Marca.query.all()

    def create(self, nombre):
        nueva_marca = Marca(nombre=nombre)
        db.session.add(nueva_marca)
        db.session.commit()
        return nueva_marca

class Tipo_prendaRepository:
    def get_all(self):
        return Tipo_prenda.query.all()

    def create(self, nombre):
        nueva_tprenda = Tipo_prenda(nombre=nombre)
        db.session.add(nueva_tprenda)
        db.session.commit()
        return nueva_tprenda
    
class StockRepository:
    def get_all(self):
        return Stock.query.all()

    def create(self,cantidad):
        nuevo_stock = Stock(cantidad=cantidad)
        db.session.add(nuevo_stock)
        db.session.commit()
        return nuevo_stock