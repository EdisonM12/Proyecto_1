import json
from tabulate import tabulate


def mostrar_prod():
    archivo1 = "../data/Productos.json"
    with open(archivo1, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Acceder a la lista de productos
    productos_list = data["productos"]

    ids_compra_total = []
    total_general = 0
    productos_comprados = []  # Ahora guardará listas en lugar de strings

    # Ciclo para seguir comprando
    while True:
        print("\n=== PRODUCTOS DISPONIBLES ===")

        tablaP = []
        for producto in productos_list:
            tablaP.append([producto["id"], producto["nombre"], f"${producto['precio']}"])

        print(tabulate(tablaP, headers=["ID", "Nombre", "Precio"], tablefmt="grid"))

        venta = input("\nEscoja los productos que va a comprar (IDs separados por comas): ")
        ids_compra = []

        for x in venta.split(","):
            x = x.strip()
            if x.isdigit():
                ids_compra.append(int(x))

        # Procesar la compra actual
        for producto in productos_list:
            if producto["id"] in ids_compra:
                total_general += producto["precio"]
                productos_comprados.append([producto['nombre'], f"${producto['precio']}"])
                ids_compra_total.extend(ids_compra)

        # Preguntar si desea seguir comprando
        continuar = input("\n¿Desea seguir comprando? (s/n): ").strip().lower()

        if continuar != 's':
            break

    # Mostrar resumen final
    if productos_comprados:
        print("\n=== RESUMEN FINAL DE COMPRA ===")
        print(tabulate(productos_comprados, headers=["Nombre", "Precio"], tablefmt="grid"))
        print(f"\n{'TOTAL:':>20} ${total_general}")
    else:
        print("\nNo se seleccionaron productos.")


def menu_compra():
    while True:
        print("\n--- MENÚ DE COMPRAS ---")
        print("1. Mostrar productos y comprar")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_prod()
        elif opcion == "2":
            print("Saliendo del menú...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


# Ejecutar el menú
if __name__ == "__main__":
    menu_compra()