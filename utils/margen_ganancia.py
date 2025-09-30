# import json
#
# def calcular_margen_producto():
#
#     try:
#         with open("data/productos.json", "r", encoding="utf-8") as f:
#             data = json.load(f)
#     except FileNotFoundError:
#         print("Error: No se encontró el archivo 'data/productos.json'.")
#         return
#
#     productos = data.get("productos", [])
#
#
#     def calcular_margen(precio_venta, costo):
#         return (precio_venta - costo) / precio_venta if precio_venta != 0 else 0
#
#
#     for producto in productos:
#         nombre = producto.get("nombre", "Sin nombre")
#         precio_venta = producto.get("precio", 0)
#         costo = producto.get("costo", 0)
#
#         margen = calcular_margen(precio_venta, costo)
#
#         print(f"Producto: {nombre}")
#         print(f"  Precio venta: {precio_venta}")
#         print(f"  Costo real: {costo}")
#         print(f"  Margen de ganancia: {margen:.2%}\n")
#
#
# calcular_margen_producto()
#
import json
from tabulate import tabulate  # <-- importamos tabulate

def calcular_margen_producto():
    try:
        with open("data/productos.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'data/productos.json'.")
        return

    productos = data.get("productos", [])

    # Función para calcular margen
    def calcular_margen(precio_venta, costo):
        return (precio_venta - costo) / precio_venta if precio_venta != 0 else 0

    # Lista para guardar los datos de la tabla
    tabla = []
    for producto in productos:
        nombre = producto.get("nombre", "Sin nombre")
        precio_venta = producto.get("precio", 0)
        costo = producto.get("costo", 0)
        margen = calcular_margen(precio_venta, costo)

        # Agregamos los datos a la tabla
        tabla.append([
            nombre,
            f"{precio_venta:.2f}",
            f"{costo:.2f}",
            f"{margen:.2%}"
        ])

    # Encabezados de la tabla
    headers = ["Producto", "Precio Venta", "Costo Real", "Margen de Ganancia"]

    # Imprimir la tabla con formato grid
    print (tabulate(tabla, headers=headers, tablefmt="grid"))


