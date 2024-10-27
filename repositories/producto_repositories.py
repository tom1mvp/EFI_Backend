from app import db

from models import Marca,Tipo_prenda,Stock,Prenda,User

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
    
class PrendaRepository:
    def get_all(self):
        return Prenda.query.all()
    #Obtiene todas las prendas
    def get_by_id(self, prenda_id):
        return Prenda.query.get(prenda_id)
    #Obtiene por id
    def create(self, nombre, precio, talle_id, color_id, temporada_id, stock_id, marca_id, tipo_prenda_id, promocion_id):
        nueva_prenda = Prenda(
            nombre=nombre,
            precio=precio,
            talle_id=talle_id,
            color_id=color_id,
            temporada_id=temporada_id,
            stock_id=stock_id,
            marca_id=marca_id,
            tipo_prenda_id=tipo_prenda_id,
            promocion_id=promocion_id
        )
        db.session.add(nueva_prenda)
        db.session.commit()
        return nueva_prenda
    #crea la prenda

    def update(self, prenda_id, nombre=None, precio=None, talle_id=None, color_id=None, temporada_id=None, stock_id=None, marca_id=None, tipo_prenda_id=None, promocion_id=None):
        prenda = Prenda.query.get(prenda_id)
        if not prenda:
            return None

        if nombre is not None:
            prenda.nombre = nombre
        if precio is not None:
            prenda.precio = precio
        if talle_id is not None:
            prenda.talle_id = talle_id
        if color_id is not None:
            prenda.color_id = color_id
        if temporada_id is not None:
            prenda.temporada_id = temporada_id
        if stock_id is not None:
            prenda.stock_id = stock_id
        if marca_id is not None:
            prenda.marca_id = marca_id
        if tipo_prenda_id is not None:
            prenda.tipo_prenda_id = tipo_prenda_id
        if promocion_id is not None:
            prenda.promocion_id = promocion_id

        db.session.commit()
        return prenda
        #actualiza la prenda

    def delete(self,prenda_id):
        prenda = Prenda.query.all(prenda_id)
        if prenda:
            db.session.delete(prenda)
            db.session.commit()
        return prenda

class UserRepository:
    