import sys

from unicodedata import category

from Proyecto_1.utils.margen_ganancia import calcular_margen_producto
from models.categoria import Categoria
from models.producto import Producto
from services.productos_services import ProductosServicie
from services.proveedor_services import ProveedorServices

import json
import menu_inventario

# Leer usuarios desde el JSON
archivo="data/administrador.json"
with open(archivo, "r", encoding="utf-8") as f:
    data = json.load(f)

def login_admin() -> None:
    """Función para validar el login del administrador"""
    username = input("Ingrese usuario: ")
    password = input("Ingrese contraseña: ")

    for user in data["users"]:
        if user["username"] == username and user["password"] == password:
            menu_administrador()
            return
    print("\n Usuario o contraseña incorrectos.\n")

def login():
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Administrador (requiere login)")
        print("2. Cliente (acceso directo)")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            login_admin()
        elif opcion == "2":
            menu()
        elif opcion == "3":
            print("Saliendo del sistema....")
            sys.exit()
        else:
            print(" Opción no válida, intente nuevamente.\n")






def menu():
    servicio = ProductosServicie()
    pro = ProveedorServices()

    while True:
      print("\n=====================================")
      print("         ELIJA UNA OPCION                ")
      print("=====================================")
      print( "       1. Productos")
      print( "       2. Proveedor")
      print( "       3. Inventario")
      print( "       4. regresar al menu principal")
      print( "       5. Salir")


      op = input("Escoja una opcion que desea escoger: ")

      if op == "1" :
        print("\n--- Registrar nuevo producto ---")
        id = int(input("ID: "))
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        costo = float(input("Costo: "))
        cantidad = int(input("Cantidad: "))
        stock = int(input("Stock: "))
        stock_minimo = int(input("Stock mínimo: "))
        cat_id = int(input("id de Categoria: "))
        cat_nombre = input("Nombre de categoria: ")
        categoria = Categoria(cat_id, cat_nombre)

        try:
            producto = servicio.crear_producto(id, nombre, precio,costo, cantidad, stock, stock_minimo, categoria)
            print(" Producto creado:", producto)
        except ValueError as e:
            print(" Error:", e)


      elif op == "2":
        print("\n--- Registrar nuevo producto ---")
        id = int(input("ID: "))
        nombre = input("Nombre: ")
        cedula = int(input("Cedula: "))
        telefono = int(input("Telefono: "))
        direccion = input("Direccion: ")
        empresa = input("Empresa: ")

        try:
             proveedor1 = pro.crear_proveedor(id, nombre, cedula, telefono, direccion, empresa)
             print(f"Proveedor agregado {proveedor1}")
        except ValueError as e:
            print(" Error:", e)

      elif op == "3":
          return menu_inventario.menu()
      elif op == "4":
          return login()

      else:

          print("saliendo del sistema")
          sys.exit()

def menu_administrador():
    servicio = ProductosServicie()
    pro = ProveedorServices()
    while True:
        print("=== MENÚ ADMINISTRADOR ===")
        print("1. Ver productos y calcular margen de ganancia")
        print("2. Productos               ")
        print("3. Proveedor               ")
        print("4. Inventario              ")
        print("5. volver al menu principal")
        print("6. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            calcular_margen_producto()
        elif op == "2":
            print("\n--- Registrar nuevo producto ---")
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            costo = float(input("Costo: "))
            cantidad = int(input("Cantidad: "))
            stock = int(input("Stock: "))
            stock_minimo = int(input("Stock mínimo: "))
            cat_id = int(input("id de Categoria: "))
            cat_nombre = input("Nombre de categoria: ")
            categoria = Categoria(cat_id, cat_nombre)

            try:
                producto = servicio.crear_producto(id, nombre, precio,costo, cantidad, stock, stock_minimo, categoria)
                print(" Producto creado:", producto)
            except ValueError as e:
                print(" Error:", e)


        elif op == "3":
            print("\n--- Registrar nuevo producto ---")
            id = int(input("ID: "))
            nombre = input("Nombre: ")
            cedula = int(input("Cedula: "))
            telefono = int(input("Telefono: "))
            direccion = input("Direccion: ")
            empresa = input("Empresa: ")

            try:
                proveedor1 = pro.crear_proveedor(id, nombre, cedula, telefono, direccion, empresa)
                print(f"Proveedor agregado {proveedor1}")
            except ValueError as e:
                print(" Error:", e)

        elif op == "4":
            return menu_inventario.menu()
        elif op == "5":
            return login()

        else:
            print("Saliendo del sistema....")
            sys.exit()

def main():
    while True:
        login()
if __name__ == "__main__":
    main()





