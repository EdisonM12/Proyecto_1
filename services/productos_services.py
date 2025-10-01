from models.producto import Producto
from services.producto_repository import ProductoRepository
from Crud import Cru_producto


class ProductosServicie:
    def __init__(self):
        self.repo = ProductoRepository()

    def crear_producto(self, id,nombre,precio,costo,cant, stock ,stock_minimo, categoria):

        producto = Producto(id,nombre,precio,costo,cant,stock,stock_minimo,categoria)
        Cru_producto.crear_productos(producto)
        return producto

    def lsitar_producto(self):
        return Cru_producto.obtener_productos()

    def actualizar_producto(self, id, nombre = None,precio = None,costo=None,cant = None,stock = None,stock_minimo = None, categoria= None):
        Cru_producto.actualizar_productos(id, nombre, precio,costo, cant, stock, stock_minimo, categoria= None)

    def eliminar_producto(self,id):
        Cru_producto.eliminar_productos(id)
