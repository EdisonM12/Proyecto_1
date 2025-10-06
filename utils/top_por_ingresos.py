import json
from tabulate import tabulate
import time
def esperar(mensaje: str = "", segundos: int = 3):
    print(f"\n{mensaje}")
    time.sleep(segundos)
def top_por_ingresos():
    archivo = "data/Productos.json"
    with open(archivo, "r") as archivo:
        json_data = json.load(archivo)

    productos = json_data.get("productos", [])
    producto_ordenado= sorted(productos, key=lambda x: x["costo"], reverse=False)
    encabezado = ["Nombre", "Precio", "Costo"]
    tabala = [[p["nombre"], p["precio"], p["costo"]]for p in producto_ordenado[:5]]
    print(tabulate(tabala , headers=encabezado, tablefmt="grid" ))
    esperar("", 5)




