from dataclasses import dataclass, field
from models.producto import Producto

@dataclass
class Categoria:
    id: int
    nombre: str
    activo: bool = True
    productos: list["Producto"]= field(default_factory=list)

    def agregar_producto(self, producto: "Producto"):
        if producto not in self.productos:
          self.productos.append(producto)

    def eliminar_productos(self, producto: "Producto"):
        if producto not in self.productos:
            return  False
        self.productos.remove(producto)


    def __str__(self):
        nombres_productos = ', '.join([p.nombre for p in self.productos])
        return f"Categoría {self.nombre} con productos: {nombres_productos if nombres_productos else 'ninguno'}"