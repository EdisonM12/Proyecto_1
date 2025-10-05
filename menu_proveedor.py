from services.proveedor_services import ProveedorServices
from utils.validacion import pedir_flotante, pedir_entero

def mostrar_menu_admin():
    servicio = ProveedorServices()
    while True:
        print("╔══════════════════════════╗")
        print("║--- MENÚ ADMINISTRADOR ---║")
        print("║1. Agregar proveedor      ║")
        print("║2. Listar proveedor       ║")
        print("║3. Modificar proveedor    ║")
        print("║4. Eliminar proveedor     ║")
        print("║5. Salir                  ║")
        print("╚══════════════════════════╝")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Registrar nuevo proveedor ---")

            nombre = input("Nombre: ")
            cedula = pedir_entero("Cedula: ")
            telefono = pedir_entero("Telefono: ")
            direccion = input("Direccion: ")
            empresa = input("Empresa: ")
            try:
                pv1 = servicio.crear_proveedor( nombre, cedula, telefono, direccion, empresa)
                print(" Producto creado:", pv1)
            except ValueError as e:
                print(" Error:", e)




        elif opcion == "2":
            producto2 = servicio.listar_proveedor()
            print("lista de productos: ", producto2)




        elif opcion == "3":
            print("\n--- Actualizar Proveedor ---")
            id = pedir_entero("ID: ")
            nombre = input("Nombre: ")
            cedula = pedir_entero("Cedula: ")
            telefono = pedir_entero("telefono: ")
            direccion = input("Direccion: ")
            empresa = input("Empresa: ")

            pv = servicio.actualizar_proveedor( id , nombre, cedula, telefono, direccion, empresa)

            print(" Proveedor actualizado")


        elif opcion == "4":
            id = pedir_entero("ID: ")

            producto1 = servicio.eliminar_proveedor(id)
            print("Producto Eliminado ")




        elif opcion == "5":
            print("Saliendo del menú...")
            break
        else:
            print("Opción inválida, intente de nuevo.")
