import json

from models.producto import Producto

archivo = r"C:\Users\Edison\Desktop\Proyecto_Poo\Proyecto_1\data\Productos.json"


def alerta_de_stock_minimo():
    """Muestra un mensaje de alerta para productos con stock bajo"""
    with open(archivo, "r", encoding="utf-8") as f:
        data = json.load(f)
    productos = data["productos"]
    for fa in productos:
        if fa["stock"] <= fa["stock_minimo"]:
            print(f"Alerta: El producto '{fa['nombre']}' tiene stock mínimo ({fa['stock']})")


def listar_stock_minimo():
    """Lista productos con stock menor o igual al mínimo y los ordena por stock"""
    list1 = []

    with open(archivo, "r", encoding="utf-8") as f:
        data = json.load(f)
    productos = data["productos"]
    # Filtrar productos
    list1 = [p for p in productos if p["stock"] <= p["stock_minimo"]]

    # Ordenar por stock de menor a mayor
    list1.sort(key=lambda x: x["stock"])

    # Mostrar resultados
    if list1:
        print("\nProductos con stock mínimo:")
    else:
        print("\nNo hay productos con stock bajo.")

    return list1


def menu():
    while True:
        print("\n=== MENÚ ===")
        print("1. Alerta de stock mínimo")
        print("2. Listar productos con stock mínimo")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            alerta_de_stock_minimo()
        elif opcion == "2":
            listar_stock_minimo()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecutar menú
menu()
