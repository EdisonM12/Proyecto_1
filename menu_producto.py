from models.categoria import Categoria
from services.productos_services import ProductosServicie
from utils.validacion import pedir_flotante, pedir_entero


def mostrar_menu_admin():
    servicio = ProductosServicie()
    while True:
        print("╔══════════════════════════╗")
        print("║--- MENÚ ADMINISTRADOR ---║")
        print("║1. Agregar producto       ║")
        print("║2. Listar productos       ║")
        print("║3. Modificar producto     ║")
        print("║4. Eliminar producto      ║" )
        print("║5. Salir                  ║")
        print("╚══════════════════════════╝")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Registrar nuevo producto ---")
            nombre = input("Nombre: ")
            precio = pedir_flotante("Precio: ")
            costo = pedir_flotante("Costo: ")
            stock = pedir_entero("Stock: ")
            stock_minimo = pedir_entero("Stock mínimo: ")
            cat_nombre = input("Nombre de categoria: ")
            categoria = Categoria( cat_nombre)
            try:
                producto = servicio.crear_producto( nombre, precio, costo, stock, stock_minimo, categoria)
                print(" Producto creado:", producto)
            except ValueError as e:
                print(" Error:", e)




        elif opcion == "2":
            producto2 = servicio.lsitar_producto()
            print("lista de productos: ", producto2)



        elif opcion == "3":
            print("\n--- Actualizar nuevo producto ---")
            id = pedir_entero("ID: ")
            nombre = input("Nombre: ")
            precio = pedir_flotante("Precio: ")
            costo = pedir_flotante("Costo: ")
            stock = pedir_entero("Stock: ")
            stock_minimo = pedir_entero("Stock mínimo: ")
            cat_id = pedir_entero("ID de Categoria: ")
            cat_nombre = input("Nombre de categoria: ")

            categoria = Categoria(cat_id, cat_nombre)

            producto3 = servicio.actualizar_producto(id, nombre,precio,costo, stock, stock_minimo, categoria)

            print(" Producto actualizado")


        elif opcion == "4":
            id = pedir_entero("ID: ")
            producto1 = servicio.eliminar_producto(id)
            print("Producto Eliminado")



        elif opcion == "5":
            print("Saliendo del menú...")
            break
        else:
            print("Opción inválida, intente de nuevo.")
