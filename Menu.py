from models.producto import Producto
from services.productos_services import ProductosServicie
from services.proveedor_services import ProveedorServices
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
            print("✅ Producto creado:", producto)
        except ValueError as e:
            print("❌ Error:", e)


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
            print("❌ Error:", e)

      elif op == "3":
          return False

      else:
          print("saliendo del sistema")

menu()



