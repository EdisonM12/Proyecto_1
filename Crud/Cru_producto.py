import json

from models.producto import Producto

archivo= "data/Productos.json"

def cargar_datos():
     try:
        with open(archivo, "r") as f:
            data = json.load(f)
            return [Producto(**p) for p in data.get("productos", []) ]
     except FileNotFoundError:
         return []

def guardar_datos(productos):
    with open(archivo, "w") as f:
        json.dump({"productos": [p.__dict__ for p in productos]}, f, indent=4)

def crear_productos(producto):
    productos = cargar_datos()
    productos.append(producto)
    guardar_datos(productos)

def obtener_productos():
    return cargar_datos()


def actualizar_productos(id, nombre= None, precio=None, cant=None, stock=None, stock_minimo=None ):
    productos = cargar_datos()
    for p in productos:
     if p.id == id:
        if nombre: p.nombre = nombre
        if precio: p.precio = precio
        if cant: p.cant = cant
        if stock: p.stock = stock
        if stock_minimo: p.stock_minimo = stock_minimo
        break
    guardar_datos(productos)

def eliminar_productos(id):
    productos = cargar_datos()
    productos= [p for p in productos if p.id != id]
    guardar_datos(productos)
