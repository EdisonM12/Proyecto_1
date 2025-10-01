
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Producto:
    id: int
    nombre: str
    precio: int
    costo: int
    cant: int
    stock: int
    stock_minimo: int
    categoria: "Categoria" = None

    def agregar_stock(self, cantidad: int):
        if cantidad < 0:
            raise ValueError('Coloque una cantidad correcta')
        self.stock += cantidad

    def validaciones_stcok(self):
        if self.stock <= self.stock_minimo:
            raise ValueError("colocar mas stock")

    def disminuir_stock(self, cantidad: int):
        if cantidad < 0:
            raise ValueError('Coloque una cantidad positiva')
        self.stock -= cantidad

    def validacion_Venta(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("debe agregar una cantidad valida")
        if cantidad > self.stock:
            raise ValueError("no hay suficiente inventario")
        self.disminuir_stock(cantidad)


    def to_dict(self) -> dict:

        data = asdict(self)
        if self.categoria is not None and hasattr(self.categoria, "to_dict"):
            data["categoria"] = self.categoria.to_dict()
        return data

    @classmethod
    def from_dict(cls, data: dict):

        cat_data = data.get("categoria")
        if cat_data is not None and "to_dict" not in cat_data:
            from categoria import Categoria
            data["categoria"] = Categoria.from_dict(cat_data)
        return cls(**data)

