from dataclasses import dataclass, field
from producto import Producto

@dataclass
class Categoria:
    id: int
    nombre: str
    activo: bool = True
    productos: list[Producto]= field(default_factory=list)

    def agregar_producto(self, producto: Producto):
        if producto not in self.productos:
          self.productos.append(producto)

    def eliminar_productos(self, producto: Producto):
        if producto not in self.productos:
            return  False
        self.productos.remove(producto)


    def __str__(self):
        return f"el producto {Producto} pertenece ala categoria {self.nombre}"

