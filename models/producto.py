from dataclasses import dataclass
@dataclass
class Producto:
    id: int
    nombre: str
    precio: int
    cant: int
    stock: int
    stock_minimo: int
    categoria: "Categoria" = None

    def agregar_stock(self, cantidad : int):
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
         if(cantidad <= 0):
             raise ValueError("debe agregar una cantidad valida")
         if cantidad > self.stock:
             raise ValueError("no hay suficiente inventario")
         self.disminuir_stock(cantidad)

