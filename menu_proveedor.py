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

def mostrar_menu_admin():
    servicio = ProveedorServices()
    while True:
        print("\n--- MENÚ ADMINISTRADOR ---")
        print("1. Agregar proveedor")
        print("2. Listar proveedor")
        print("3. Modificar proveedor")
        print("4. Eliminar proveedor")
        print("5. Salir")

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
            # Tu función existente



        elif opcion == "2":
            producto2 = servicio.listar_proveedor()
            print("lista de productos: ", producto2)
            # Tu función existente



        elif opcion == "3":
            print("\n--- Registrar nuevo producto ---")
            nombre = input("Nombre: ")
            cedula = pedir_entero("Precio: ")
            telefono = pedir_entero("Costo: ")
            direccion = input("Cantidad: ")
            empresa = input("Stock: ")

            pv = servicio.actualizar_proveedor( nombre, cedula, telefono, direccion, empresa)

            print(" Producto actualizado:", pv)


        elif opcion == "4":
            producto1 = servicio.eliminar_proveedor(id)
            print("Producto Eliminado :", producto1)  # Tu función existente
            # Tu función existente


        elif opcion == "5":
            print("Saliendo del menú...")
            break
        else:
            print("Opción inválida, intente de nuevo.")
