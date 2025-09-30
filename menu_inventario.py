from Crud import Cru_producto
from Crud import Crud_Inventario
from Menu import esperar
import sys
import Menu
def menus():
    while True:
        print("╔══════════════════════════════════════════╗")
        print("║============  MENÚ INVENTARIO  ===========║")
        print("║  1. Registrar movimiento (COMPRA/VENTA)  ║")
        print("║  2. Listar movimientos                   ║")
        print("║  3. Actualizar movimiento                ║")
        print("║  4. Eliminar movimiento                  ║")
        print("║  5. regresar al menu anterior            ║")
        print("║  6. Salir                                ║")
        print("╚══════════════════════════════════════════╝")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_producto = int(input("Ingrese ID del producto: "))
                tipo = input("Tipo de movimiento (COMPRA/VENTA): ").upper()
                cantidad = int(input("Cantidad: "))
                Crud_Inventario.registrar_movimiento(id_producto, tipo, cantidad)
            except ValueError:
                print(" Datos inválidos, intente de nuevo.")

        elif opcion == "2":
            movimientos = Crud_Inventario.listar_movimientos()
            if not movimientos:
                print(" No hay movimientos registrados.")
            else:
                for m in movimientos:
                    print(m)

        elif opcion == "3":
            try:
                id_mov = int(input("Ingrese ID del movimiento a actualizar: "))
                tipo = input("Nuevo tipo (ENTER para no cambiar): ")
                cantidad = input("Nueva cantidad (ENTER para no cambiar): ")
                cantidad = int(cantidad) if cantidad else None
                Crud_Inventario.actualizar_movimiento(id_mov, tipo if tipo else None, cantidad)
                print(" Movimiento actualizado.")
            except ValueError:
                print(" Datos inválidos.")

        elif opcion == "4":
            try:
                id_mov = int(input("Ingrese ID del movimiento a eliminar: "))
                Crud_Inventario.eliminar_movimiento(id_mov)
            except ValueError:
                print(" ID inválido.")
        elif opcion == "5":
            esperar("Regresando al menú anterior",3)
            return Menu.menu()


        elif opcion == "6":
            esperar(" Saliendo del sistema...",3)
            sys.exit()

        else:
            print(" Opción inválida, intente de nuevo.")


if __name__ == "__main__":
    menus()
