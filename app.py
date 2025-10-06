import sys
import time
import os
import platform


from utils.margen_ganancia import calcular_margen_producto

from services.productos_services import ProductosServicie
from services.proveedor_services import ProveedorServices
import json
import menu_inventario
from menu_producto import mostrar_menu_admin as menu_admin_producto
from menu_proveedor import mostrar_menu_admin as menu_admin_proveedor
from utils.funciones_Cliente import mostrar_prod
from utils.alerta import alerta_de_stock_minimo
from colorama import Fore, Style, init
from aaa import barra


archivo = "data/administrador.json"
with open(archivo, "r", encoding="utf-8") as f:
    data = json.load(f)


def limpiar_pantalla():

    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def esperar(mensaje: str = "", segundos: int = 3):
    print(f"\n{mensaje}")
    time.sleep(segundos)


def login_admin():

    limpiar_pantalla()
    print("\n╔════════════════════════════════════╗")
    print("║      LOGIN ADMINISTRADOR           ║")
    print("╚════════════════════════════════════╝\n")

    username = input(Style.BRIGHT + "Ingrese usuario: ")
    password = input("Ingrese contraseña: ")

    for user in data["users"]: #recorrer el json
        if user["username"] == username and user["password"] == password:
            esperar(f" Bienvenido {username}!", 2)
            menu_administrador()
            return

    print("\n Usuario o contraseña incorrectos.\n")
    esperar("", 2)

    login_admin()



def login():

    while True:
        limpiar_pantalla()
        print("\n")
        print(" ╔════════════════════════════════════╗")
        print(" ║=========  MENÚ PRINCIPAL  =========║")
        print(" ╠════════════════════════════════════╣")
        print(" ║  1. Administrador (requiere login) ║")
        print(" ║  2. Cliente (acceso directo)       ║")
        print(" ║  3. Salir                          ║")
        print(" ╚════════════════════════════════════╝")
        print()

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            barra()
            login_admin()
            alerta_de_stock_minimo()

        elif opcion == "2":
            esperar(" Ingresando como cliente...", 2)
            barra()

            menu_cliente()
        elif opcion == "3":
            esperar(" Saliendo del sistema....", 2)
            barra()
            limpiar_pantalla()
            sys.exit()
        else:
            print("\n Opción no válida, intente nuevamente.\n")
            esperar("", 1)


def menu_cliente():

    servicio = ProductosServicie()
    pro = ProveedorServices()

    while True:
        limpiar_pantalla()
        print("\n")
        print("╔══════════════════════════════════════╗")
        print("║========== MENÚ CLIENTE ==============║")
        print("╠══════════════════════════════════════╣")
        print("║       1. Comprar Productos           ║")
        print("║       2. Regresar al menú principal  ║")
        print("║       3. Salir                       ║")
        print("╚══════════════════════════════════════╝")
        print()

        op = input("Escoja una opción: ").strip()

        if op == "1":
            mostrar_prod()
        elif op == "2":
            esperar(" Regresando al menú principal...", 2)
            barra()

        elif op == "3":
            esperar(" Saliendo del sistema...", 2)
            barra()
            limpiar_pantalla()
            sys.exit()
        else:
            print("\n Opción no válida")
            esperar("", 1)


def menu_administrador():

    servicio = ProductosServicie()
    pro = ProveedorServices()

    while True:
        limpiar_pantalla()
        print("\n")
        print("╔═════════════════════════════════════════════════╗")
        print("║=============  MENÚ ADMINISTRADOR  ==============║")
        print("╠═════════════════════════════════════════════════╣")
        print("║  1. Ver productos y calcular margen de ganancia ║")
        print("║  2. Gestión de Productos                        ║")
        print("║  3. Gestión de Proveedores                      ║")
        print("║  4. Gestión de Inventario                       ║")
        print("║  5. Volver al menú principal                    ║")
        print("║  6. Salir                                       ║")
        print("╚═════════════════════════════════════════════════╝")
        print()

        op = input("Seleccione una opción: ").strip()

        if op == "1":
            esperar(" Calculando margen de los productos...", 2)
            barra()
            calcular_margen_producto()
        elif op == "2":
            esperar("Gestionando Productos...", 2)
            barra()
            menu_admin_producto()
        elif op == "3":
            menu_admin_proveedor()
        elif op == "4":
            esperar(" Cargando menú de inventario...", 2)
            barra()
            menu_inventario.menus()
        elif op == "5":
            esperar(" Regresando al menú principal...", 2)
            barra()
            login()
        elif op == "6":
            esperar(" Saliendo del sistema....", 2)
            barra()
            limpiar_pantalla()
            sys.exit()
        else:
            print("\n Opción no válida")
            esperar("", 1)


def main():

    try:
        login()
    except KeyboardInterrupt:
        print("\n\n Programa interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()