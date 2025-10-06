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
from utils.validacion import pedir_flotante, pedir_entero
from aaa import barra
from app import limpiar_pantalla

def mostrar_menu_admin():
    limpiar_pantalla()
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
            barra()
            limpiar_pantalla()
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
            barra()
            limpiar_pantalla()
            producto2 = servicio.listar_proveedor()
            print("lista de productos: ", producto2)




        elif opcion == "3":
            barra()
            limpiar_pantalla()
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
            barra()
            limpiar_pantalla()
            id = pedir_entero("ID: ")

            producto1 = servicio.eliminar_proveedor(id)
            print("Producto Eliminado ")




        elif opcion == "5":
            barra()
            limpiar_pantalla()
            print("Saliendo del menú...")
            break
        else:
            print("Opción inválida, intente de nuevo.")
