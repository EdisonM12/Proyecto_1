from dataclasses import dataclass, field
from models.producto import Producto


@dataclass
class Categoria:
    nombre: str
    activo: bool = True
    productos: list["Producto"]= field(default_factory=list)
    id: int = field( init = False)
    id_cat = 0

    def __post_init__(self):

        type(self).id_cat += 1
        self.id = type(self).id_cat

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