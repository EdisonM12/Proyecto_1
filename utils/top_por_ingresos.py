def top_productos_por_ingresos():
    productos = {}

    n = int(input("¿Cuántos productos quieres registrar para el ranking?: "))

    for i in range(n):
        producto = input(f"\nNombre del producto {i+1}: ")
        ingreso = float(input(f"Ingresos generados por {producto}: $"))
        productos[producto] = ingreso


    ranking = sorted(productos.items(), key=lambda x: x[1], reverse=True)

    print("\nTop de Productos por Ingresos\n")
    print(f"{'Posición':<10}{'Producto':<20}{'Ingresos ($)':<12}")
    print("-" * 45)

    for i, (producto, ingreso) in enumerate(ranking, start=1):
        print(f"{i:<10}{producto:<20}{ingreso:<12.2f}")

    total = sum(productos.values())
    mejor = ranking[0]
    print("\nTotal de ingresos:", total)
    print(f"Producto más rentable: {mejor[0]} con ${mejor[1]:.2f}")