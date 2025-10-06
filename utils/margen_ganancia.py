import json
import time
from tabulate import tabulate  #
def esperar(mensaje: str = "", segundos: int = 3):
    print(f"\n{mensaje}")
    time.sleep(segundos)

def calcular_margen_producto():
    try:
        with open("data/productos.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'data/productos.json'.")
        return

    productos = data.get("productos", [])


    def calcular_margen(precio_venta, costo):
        return (precio_venta - costo) / precio_venta if precio_venta != 0 else 0


    tabla = []
    for producto in productos:
        nombre = producto.get("nombre", "Sin nombre")
        precio_venta = producto.get("precio", 0)
        costo = producto.get("costo", 0)
        margen = calcular_margen(precio_venta, costo)


        tabla.append([
            nombre,
            f"{precio_venta:.2f}",
            f"{costo:.2f}",
            f"{margen:.2%}"
        ])

    headers = ["Producto", "Precio Venta", "Costo Real", "Margen de Ganancia"]


    print (tabulate(tabla, headers=headers, tablefmt="grid"))
    esperar("Regresando al menu anterior",5)
