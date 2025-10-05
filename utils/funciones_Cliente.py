
from Crud.Crud_Inventario import registrar_movimiento  # Importa tu CRUD de movimientos
import json
from tabulate import tabulate

def mostrar_prod():
    archivo1 = "data/Productos.json"
    with open(archivo1, "r", encoding="utf-8") as f:
        data = json.load(f)

    productos_list = data["productos"]
    total_general = 0
    productos_comprados = []

    while True:
        print("\n=== PRODUCTOS DISPONIBLES ===")
        tablaP = [[p["id"], p["nombre"], f"${p['precio']}", p["stock"]] for p in productos_list]
        print(tabulate(tablaP, headers=["ID", "Nombre", "Precio", "Stock"], tablefmt="grid"))

        venta = input("\nEscoja los productos que va a comprar (IDs separados por comas): ")
        ids_compra_cant = []

        for x in venta.split(","):
            x = x.strip()
            if "-" in x:  # Permite indicar cantidad: "1-3" -> ID 1, cantidad 3
                prod_id, cant = x.split("-")
                if prod_id.isdigit() and cant.isdigit():
                    ids_compra_cant.append((int(prod_id), int(cant)))
            elif x.isdigit():
                ids_compra_cant.append((int(x), 1))  # Por defecto cantidad 1

        # Procesar compra y registrar en Kardex
        for id_producto, cantidad in ids_compra_cant:
            producto = next((p for p in productos_list if p["id"] == id_producto), None)
            if producto:
                total_general += producto["precio"] * cantidad
                productos_comprados.append([producto['nombre'], cantidad, f"${producto['precio']*cantidad}"])
                registrar_movimiento(id_producto, "COMPRA", cantidad)

        continuar = input("\n¿Desea seguir comprando? (s/n): ").strip().lower()
        if continuar != 's':
            break

    # Mostrar resumen final
    if productos_comprados:
        print("\n=== RESUMEN FINAL DE COMPRA ===")
        print(tabulate(productos_comprados, headers=["Nombre", "Cantidad", "Precio"], tablefmt="grid"))
        print(f"\n{'TOTAL:':>20} ${total_general}")
    else:
        print("\nNo se seleccionaron productos.")
