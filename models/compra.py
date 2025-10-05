

class Compra:
    id = 0
    def _init_(self, id_compra, proveedor, fecha):
        Compra.id += 1
        self.id = Compra.id
        self.proveedor = proveedor
        self.fecha = fecha
        self.productos = []
        self.total = 0.0


    def agregar_producto(self, id_producto, cantidad, costo_unitario):
        self.productos.append({"id": id_producto, "cantidad": cantidad, "costo": costo_unitario})

    def calcular_total(self):
        self.total = sum(item["cantidad"] * item["costo"] for item in self.productos)
        return self.total