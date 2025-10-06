from Crud import Crud_Inventario
import time
from app import menu_administrador
from utils.top_por_ingresos import top_por_ingresos
import sys
from tabulate import tabulate
from aaa import barra
from app import limpiar_pantalla

def esperar(mensaje: str = "", segundos: int = 3):
    print(f"\n{mensaje}")
    time.sleep(segundos)

def menus():

    while True:
        print("╔══════════════════════════════════════════╗")
        print("║============  MENÚ INVENTARIO  ===========║")
        print("║  1. Listar movimientos                   ║")
        print("║  2. Eliminar movimiento                  ║")
        print("║  3. Top de productos por ingresos        ║")
        print("║  4. regresar al menu anterior            ║")
        print("║  5. Salir                                ║")
        print("╚══════════════════════════════════════════╝")

        opcion = input("Seleccione una opción: ")



        if opcion == "1":
            barra()
            movimientos = Crud_Inventario.listar_movimientos()
            if not movimientos:
                print(" No hay movimientos registrados.")
                return

            tabla = []
            for m in movimientos:
                for p in m.get("productos", []):
                    tabla.append([
                        m.get("id_mov", ""),
                        m.get("tipo", ""),
                        m.get("fecha", ""),
                        p.get("id_producto", ""),
                        p.get("nombre", ""),
                        p.get("cantidad", ""),
                        p.get("stock_anterior", ""),
                        p.get("stock_nuevo", ""),
                        m.get("cantidad_total", "")
                    ])

            headers = [
                "ID MOV",
                "TIPO",
                "FECHA",
                "ID PRODUCTO",
                "NOMBRE",
                "CANTIDAD",
                "STOCK ANTERIOR",
                "STOCK NUEVO",
                "CANTIDAD TOTAL"
            ]

            print(tabulate(tabla, headers=headers, tablefmt="fancy_grid"))
            esperar("",5)
            limpiar_pantalla()


        elif opcion == "2":
            barra()
            try:
                id_mov = int(input("Ingrese ID del movimiento a eliminar: "))
                Crud_Inventario.eliminar_movimiento(id_mov)
            except ValueError:
                print(" ID inválido.")

            barra()
            limpiar_pantalla()

        elif opcion == "3":
            barra()
            top_por_ingresos()
        elif opcion == "4":

            esperar("Regresando al menú anterior", 3)
            barra()
            limpiar_pantalla()
            menu_administrador()

        elif opcion == "5":
            barra()
            esperar(" Saliendo del sistema...",3)
            sys.exit()
        else:
            print(" Opción inválida, intente de nuevo.")

        limpiar_pantalla()

if __name__ == "_main_":
    menus()