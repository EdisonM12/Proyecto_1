import sys
import time
import os
import platform
from rich.console import Console
from unicodedata import category
from utils.margen_ganancia import calcular_margen_producto
from models.categoria import Categoria
from models.producto import Producto
from services.productos_services import ProductosServicie
from services.proveedor_services import ProveedorServices
import json
import menu_inventario
from menu_producto import mostrar_menu_admin as menu_admin_producto
from menu_proveedor import mostrar_menu_admin as menu_admin_proveedor
from utils.funciones_Cliente import mostrar_prod
from utils.validacion import pedir_entero, pedir_flotante

archivo = "data/administrador.json"
with open(archivo, "r", encoding="utf-8") as f:
    data = json.load(f)

console = Console()


def limpiar_pantalla():
    """Limpia la consola según el sistema operativo"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def esperar(mensaje: str = "", segundos: int = 3):
    print(f"\n{mensaje}")
    time.sleep(segundos)


def login_admin():
    """Login para administradores"""
    limpiar_pantalla()
    print("\n╔════════════════════════════════════╗")
    print("║      LOGIN ADMINISTRADOR           ║")
    print("╚════════════════════════════════════╝\n")

    username = input("Ingrese usuario: ")
    password = input("Ingrese contraseña: ")

    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            esperar(f"✅ Bienvenido {username}!", 2)
            menu_administrador()
            return

    print("\n❌ Usuario o contraseña incorrectos.\n")
    esperar("", 2)


def login():
    """Menú principal de selección de rol"""
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
            login_admin()
        elif opcion == "2":
            esperar("✅ Ingresando como cliente...", 2)
            menu_cliente()
        elif opcion == "3":
            esperar("👋 Saliendo del sistema....", 2)
            limpiar_pantalla()
            sys.exit()
        else:
            print("\n❌ Opción no válida, intente nuevamente.\n")
            esperar("", 1)


def menu_cliente():
    """Menú para clientes"""
    servicio = ProductosServicie()
    pro = ProveedorServices()

    while True:
        limpiar_pantalla()
        print("\n")
        print("╔══════════════════════════════════════╗")
        print("║========== MENÚ CLIENTE ==============║")
        print("╠══════════════════════════════════════╣")
        print("║       1. Comprar Productos           ║")
        print("║       2. Registrar Proveedor         ║")
        print("║       3. Ver Inventario              ║")
        print("║       4. Regresar al menú principal  ║")
        print("║       5. Salir                       ║")
        print("╚══════════════════════════════════════╝")
        print()

        op = input("Escoja una opción: ").strip()

        if op == "1":
            mostrar_prod()
        elif op == "2":
            limpiar_pantalla()
            print("\n--- Registrar nuevo proveedor ---")
            nombre = input("Nombre: ")
            cedula = pedir_entero("Cédula: ")
            telefono = pedir_entero("Teléfono: ")
            direccion = input("Dirección: ")
            empresa = input("Empresa: ")

            try:
                proveedor1 = pro.crear_proveedor( nombre, cedula, telefono, direccion, empresa)
                print(f"✅ Proveedor agregado: {proveedor1}")
                esperar("", 2)
            except ValueError as e:
                print(f"❌ Error: {e}")
                esperar("", 2)

        elif op == "3":
            esperar("📦 Cargando inventario...", 2)
            menu_inventario.menus()
        elif op == "4":
            esperar("🔙 Regresando al menú principal...", 2)
            return  # Regresa al menú principal
        elif op == "5":
            esperar("👋 Saliendo del sistema...", 2)
            limpiar_pantalla()
            sys.exit()
        else:
            print("\n❌ Opción no válida")
            esperar("", 1)


def menu_administrador():
    """Menú para administradores"""
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
            esperar("📊 Calculando margen de los productos...", 2)
            calcular_margen_producto()
        elif op == "2":
            menu_admin_producto()
        elif op == "3":
            menu_admin_proveedor()
        elif op == "4":
            esperar("📦 Cargando menú de inventario...", 2)
            menu_inventario.menus()
        elif op == "5":
            esperar("🔙 Regresando al menú principal...", 2)
            return  # Regresa al menú principal
        elif op == "6":
            esperar("👋 Saliendo del sistema....", 2)
            limpiar_pantalla()
            sys.exit()
        else:
            print("\n❌ Opción no válida")
            esperar("", 1)


def main():
    """Función principal que inicia el programa"""
    try:
        login()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()