class Compra:
    def _init_(self, id_compra, proveedor, fecha):
        self.id_compra = id_compra
        self.proveedor = proveedor
        self.fecha = fecha
        self.productos = []
        self.total = 0.0

    def agregar_producto(self, id_producto, cantidad, costo_unitario):
        self.productos.append({"id": id_producto, "cantidad": cantidad, "costo": costo_unitario})

    def calcular_total(self):
        self.total = sum(item["cantidad"] * item["costo"] for item in self.productos)
        return self.total