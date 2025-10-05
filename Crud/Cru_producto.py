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
                    cat = Categoria(nombre=p["categoria"]["nombre"])

                    cat.id = p["categoria"].get("id", 0)
                    Categoria.id_cat = max(Categoria.id_cat, cat.id)

                producto = Producto(
                    nombre=p["nombre"],
                    precio=p["precio"],
                    costo=p["costo"],
                    stock=p["stock"],
                    stock_minimo=p["stock_minimo"],
                    categoria=cat
                )

                producto.id = p.get("id", 0)
                Producto.id_contador = max(Producto.id_contador, producto.id)

                productos.append(producto)
            return productos
    except FileNotFoundError:
        return []



def guardar_datos(productos):
    data_serializable = []

    for idx, p in enumerate(productos):
        nuevo_id = idx + 1

        data_serializable.append({
            "id": nuevo_id,
            "nombre": p.nombre,
            "precio": p.precio,
            "costo": p.costo,
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


def actualizar_productos(id=None, nombre= None, precio=None, costo= None, stock=None, stock_minimo=None, categoria=None ):
    productos = cargar_datos()
    producto_actualizado = None
    for p in productos:
     if p.id == id:

        if nombre: p.nombre = nombre
        if precio: p.precio = precio
        if costo:p.costo=costo
        if stock: p.stock = stock
        if stock_minimo: p.stock_minimo = stock_minimo
        if categoria: p.categoria = categoria
        break
    guardar_datos(productos)
    return producto_actualizado

def eliminar_productos(id):
    productos = cargar_datos()
    productos= [p for p in productos if p.id != id]
    guardar_datos(productos)
