from models.producto import Producto
from services.productos_services import ProductosServicie
from services.proveedor_services import ProveedorServices

import json


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
            menu()
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
            break
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

      op = input("Escoja una opcion que desea escoger: ")

      if op == "1" :
        print("\n--- Registrar nuevo producto ---")
        id = int(input("ID: "))
        nombre = input("Nombre: ")
        precio = float(input("Precio: "))
        cantidad = int(input("Cantidad: "))
        stock = int(input("Stock: "))
        stock_minimo = int(input("Stock mínimo: "))

        try:
            producto = servicio.crear_producto(id, nombre, precio, cantidad, stock, stock_minimo)
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
          return False

      else:
          print("saliendo del sistema")

login()



