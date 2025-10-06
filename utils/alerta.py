import json
from colorama import Fore, Style, init

from models.producto import Producto

archivo = "data\Productos.json"


def alerta_de_stock_minimo():

    with open(archivo, "r", encoding="utf-8") as f:
        data = json.load(f)
    productos = data["productos"]
    for fa in productos:
        if fa["stock"] <= fa["stock_minimo"]:
            print(Fore.RED + f"Alerta: El producto '{fa['nombre']}' tiene stock mínimo ({fa['stock']})")


def listar_stock_minimo():

    list1 = []

    with open(archivo, "r", encoding="utf-8") as f:
        data = json.load(f)
    productos = data["productos"]

    list1 = [p for p in productos if p["stock"] <= p["stock_minimo"]]

    list1.sort(key=lambda x: x["stock"])


    if list1:
        print("\nProductos con stock mínimo:")
    else:
        print("\nNo hay productos con stock bajo.")

    return list1


