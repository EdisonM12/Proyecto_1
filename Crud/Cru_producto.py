import json
from models.producto import  Producto
from models.categoria import Categoria
import os

archivo= "data/Productos.json"

def cargar_datos():
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            productos = []
            for p in data.get("productos", []):
                cat = None
                if p.get("categoria"):
                    cat = Categoria(id=p["categoria"]["id"], nombre=p["categoria"]["nombre"])
                producto = Producto(
                    id=p["id"],
                    nombre=p["nombre"],
                    precio=p["precio"],
                    costo=p["costo"],
                    cant=p["cantidad"],
                    stock=p["stock"],
                    stock_minimo=p["stock_minimo"],
                    categoria=cat
                )
                productos.append(producto)
            return productos
    except FileNotFoundError:
        return []

def guardar_datos(productos):
    data_serializable = []
    for p in productos:
        data_serializable.append({
            "id": p.id,
             "nombre": p.nombre,
             "precio": p.precio,
             "costo": p.costo,
             "cantidad": p.cant,
             "stock": p.stock,
            "stock_minimo": p.stock_minimo,
             "categoria": {
                      "id": p.categoria.id,
                        "nombre": p.categoria.nombre
                      } if p.categoria else None
        })
    with open(archivo, "w") as f:
        json.dump({"productos": data_serializable}, f, indent=4, ensure_ascii=False)




def crear_productos(producto):
    productos = cargar_datos()
    productos.append(producto)
    guardar_datos(productos)

def obtener_productos():
    return cargar_datos()


def actualizar_productos(id, nombre= None, precio=None, cant=None, costo= None,stock=None, stock_minimo=None, categoria=None ):
    productos = cargar_datos()
    for p in productos:
     if p.id == id:
        if nombre: p.nombre = nombre
        if precio: p.precio = precio
        if costo:p.costo=costo
        if cant: p.cant = cant
        if stock: p.stock = stock
        if stock_minimo: p.stock_minimo = stock_minimo
        if categoria: p.categoria = categoria
        break
    guardar_datos(productos)

def eliminar_productos(id):
    productos = cargar_datos()
    productos= [p for p in productos if p.id != id]
    guardar_datos(productos)
