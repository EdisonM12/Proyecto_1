

class ProductoRepository:
    def __init__(self):
        self.productos= []

    def guardar(self, producto):
        self.productos.append(producto)

    def obtener_datos(self):
        return self.productos
