from models.producto import Producto
from services.producto_repository import ProductoRepository
from Crud import Cru_producto


class ProductosServicie:
    def __init__(self):
        self.repo = ProductoRepository()

    def crear_producto(self, id,nombre,precio,cant, stock ,stock_minimo):

        producto = Producto(id,nombre,precio,cant,stock,stock_minimo)
        Cru_producto.crear_productos(producto)
        return producto

    def lsitar_producto(self):
        return Cru_producto.obtener_productos()

    def actualizar_producto(self, id, nombre = None,precio = None,cant = None,stock = None,stock_minimo = None):
        Cru_producto.actualizar_productos(id, nombre, precio, cant, stock, stock_minimo)

    def eliminar_producto(self,id):
        Cru_producto.eliminar_productos(id)
