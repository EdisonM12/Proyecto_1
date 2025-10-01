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
    servicio = ProductosServicie()
    while True:
        print("\n--- MENÚ ADMINISTRADOR ---")
        print("1. Agregar producto")
        print("2. Listar productos")
        print("3. Modificar producto")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- Registrar nuevo producto ---")
            id = pedir_entero("ID: ")
            nombre = input("Nombre: ")
            precio = pedir_flotante("Precio: ")
            costo = pedir_flotante("Costo: ")
            cantidad = pedir_entero("Cantidad: ")
            stock = pedir_entero("Stock: ")
            stock_minimo = pedir_entero("Stock mínimo: ")
            cat_id = pedir_entero("ID de Categoria: ")
            cat_nombre = input("Nombre de categoria: ")
            categoria = Categoria(cat_id, cat_nombre)
            try:
                producto = servicio.crear_producto(id, nombre, precio, costo, cantidad, stock, stock_minimo, categoria)
                print(" Producto creado:", producto)
            except ValueError as e:
                print(" Error:", e)
            # Tu función existente



        elif opcion == "2":
            producto2 = servicio.lsitar_producto()
            print("lista de productos: ", producto2)
            # Tu función existente



        elif opcion == "3":
            print("\n--- Registrar nuevo producto ---")
            id = pedir_entero("ID: ")
            nombre = input("Nombre: ")
            precio = pedir_flotante("Precio: ")
            costo = pedir_flotante("Costo: ")
            cantidad = pedir_entero("Cantidad: ")
            stock = pedir_entero("Stock: ")
            stock_minimo = pedir_entero("Stock mínimo: ")
            cat_id = pedir_entero("ID de Categoria: ")
            cat_nombre = input("Nombre de categoria: ")

            categoria = Categoria(cat_id, cat_nombre)

            producto3 = servicio.actualizar_producto(id,nombre,precio,costo, cantidad, stock, stock_minimo, categoria)

            print(" Producto actualizado:", producto3)


        elif opcion == "4":
            id = pedir_entero("ID: ")
            producto1 = servicio.eliminar_producto(id)
            print("Producto Eliminado :", producto1)  # Tu función existente
            # Tu función existente


        elif opcion == "5":
            print("Saliendo del menú...")
            break
        else:
            print("Opción inválida, intente de nuevo.")
