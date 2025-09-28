

class ProveedorRepository:
    def __init__(self):
        self.proveedor= []

    def guardar(self, proveedor):
        self.proveedor.append(proveedor)

    def obtener(self):
        return self.proveedor
    