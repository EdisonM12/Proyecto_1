
from Crud.Crud_Inventario import registrar_movimiento  # Importa tu CRUD de movimientos
import json
from tabulate import tabulate
from tabulate import tabulate
import json

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

        venta = input("\nEscoja los productos que va a comprar (IDs separados por comas): ").strip()
        if not venta:
            print("No ingresó ningún producto.")
            continue

        ids_compra_cant = []


        for x in venta.split(","):
            x = x.strip()
            if not x.isdigit():
                print(f"Entrada inválida: {x}")
                continue
            prod_id = int(x)
            producto = next((p for p in productos_list if p["id"] == prod_id), None)
            if not producto:
                print(f"No existe el producto con ID {prod_id}")
                continue


            while True:
                cant_input = input(f"Cantidad de '{producto['nombre']}' a comprar (Stock disponible: {producto['stock']}): ")
                if cant_input.isdigit() and 1 <= int(cant_input) <= producto['stock']:
                    cantidad = int(cant_input)
                    break
                else:
                    print("Cantidad inválida o mayor al stock disponible. Intente de nuevo.")

            ids_compra_cant.append((prod_id, cantidad))


        for id_producto, cantidad in ids_compra_cant:
            producto = next((p for p in productos_list if p["id"] == id_producto), None)
            if producto:
                total_general += producto["precio"] * cantidad
                productos_comprados.append([producto['nombre'], cantidad, f"${producto['precio']*cantidad}"])
                registrar_movimiento(id_producto, "VENTA", cantidad)

                producto['stock'] -= cantidad

        continuar = input("\n¿Desea seguir comprando? (s/n): ").strip().lower()
        if continuar != 's':
            break

    if productos_comprados:
        print("\n=== RESUMEN FINAL DE COMPRA ===")
        print(tabulate(productos_comprados, headers=["Nombre", "Cantidad", "Precio"], tablefmt="grid"))
        print(f"\n{'TOTAL:':>20} ${total_general}")
    else:
        print("\nNo se seleccionaron productos.")
