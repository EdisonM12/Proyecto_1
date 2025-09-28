from models.proveedor import Proveedor
from services.proveedor_repository import ProveedorRepository
from Crud import Crud_proveedor

class ProveedorServices:
    def __init__(self):
        self.repo = ProveedorRepository()

    def crear_proveedor(self, id, nombre, cedula,telefono, direccion, empresa):
        proveedor = Proveedor(id, nombre, cedula, telefono, direccion, empresa)
        Crud_proveedor.crear_proveedor(proveedor)
        return proveedor

    def listar_proveedor(self):
        return Crud_proveedor.obtener_proveedor()

    def actualizar_proveedor(self, id= None , precio= None, cant= None, telefono= None, direccion= None, empresa= None):
        Crud_proveedor.actualizar_proveedor(id, precio, cant, telefono, direccion, empresa)

    def eliminar_proveedor(self, id):
        Crud_proveedor.eliminar_productos(id)


