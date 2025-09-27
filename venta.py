class Venta:
    def _init_(self, id_venta, cliente, fecha):
        self.id_venta = id_venta
        self.cliente = cliente
        self.fecha = fecha
        self.productos = []
        self.total = 0.0

    def agregar_producto(self, id_producto, cantidad, precio_unitario):
        self.productos.append({"id": id_producto, "cantidad": cantidad, "precio": precio_unitario})

    def calcular_total(self):
        self.total = sum(item["cantidad"] * item["precio"] for item in self.productos)
        return self.total

    def generar_factura(self):
        return f"Factura #{self.id_venta} para {self.cliente.mostrar_info()} - Total: ${self.total}"