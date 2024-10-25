from repositories.producto_repositories import MarcaRepository,Tipo_prendaRepository,StockRepository


class MarcaService:
    def __init__(
        self, producto_repositories: MarcaRepository
    ):
        self._producto_repositories = producto_repositories

    def get_all(self):
        return self._producto_repositories.get_all()
    
    def create(self, nombre):
        marca = self._producto_repositories.create(nombre)
        return marca
    
    
    
class Tipo_prendaService:
    def __init__(
      self, producto_repositories: Tipo_prendaRepository
    ):
        self._producto_repositories = producto_repositories

    def get_all(self):
        return self._producto_repositories.get_all()
    
    def create(self, nombre):
        tipo_prenda = self._producto_repositories.create(nombre)
        return tipo_prenda
    
class StockService:
    def __init__(
      self, producto_repositories: StockRepository
    ):
        self._producto_repositories = producto_repositories

    def get_all(self):
        return self._producto_repositories.get_all()
    
    def create(self, cantidad):
        stock = self._producto_repositories.create(cantidad)
        return stock
    