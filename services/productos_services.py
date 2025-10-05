from models.producto import Producto
from services.producto_repository import ProductoRepository
from Crud import Cru_producto
from tabulate import tabulate

class ProductosServicie:
    def __init__(self):
        self.repo = ProductoRepository()

    def crear_producto(self, nombre,precio,costo,cant, stock ,stock_minimo, categoria):

        producto = Producto(nombre,precio,costo,cant,stock,stock_minimo,categoria)
        Cru_producto.crear_productos(producto)
        return producto

    def lsitar_producto(self):

        productos = Cru_producto.obtener_productos()

        if not productos:
            print("No hay productos registrados.")
            return


        tabla = []
        for p in productos:
            tabla.append([
                p.nombre,
                p.precio,
                p.costo,
                p.cant,
                p.stock,
                p.stock_minimo,
                p.categoria.nombre if p.categoria else "Sin categoría"
            ])

        headers = ["NOMBRE", "PRECIO", "COSTO", "CANTIDAD", "STOCK", "STOCK MÍNIMO", "CATEGORÍA"]


        return(tabulate(tabla, headers=headers, tablefmt="grid"))

    def actualizar_producto(self,id, nombre = None,precio = None,costo=None,stock = None,stock_minimo = None, categoria= None):
        pro = Cru_producto.actualizar_productos(id, nombre, precio,costo, stock, stock_minimo, categoria)

        return pro


    def eliminar_producto(self,id):
        Cru_producto.eliminar_productos(id)
