import json
from itertools import product
import os

from models.proveedor import Proveedor

archivo= "data/Proveedores.json"

def cargar_datos():
    if not os.path.exists(archivo) or os.path.getsize(archivo) == 0:
        return []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            return [Proveedor.from_dict(p) for p in data.get("proveedor", [])]
    except FileNotFoundError:
        return []

def guardar_datos(proveedores):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump({"proveedor": [p.to_dict() for p in proveedores]}, f, indent=4, ensure_ascii=False)

def crear_proveedor(proveedor):
    proveedores = cargar_datos()
    proveedores.append(proveedor)
    guardar_datos(proveedores)

def obtener_proveedor():
    return cargar_datos()

def actualizar_proveedor(id, nombre=None, cedula=None, telefono=None, direccion=None, empresa=None):
    proveedores = cargar_datos()
    for p in proveedores:
        if p.id == id:
            if nombre: p.nombre = nombre
            if cedula: p.cedula = cedula
            if telefono: p.telefono = telefono
            if direccion: p.direccion = direccion
            if empresa: p.empresa = empresa
            break
    guardar_datos(proveedores)

def eliminar_proveedor(id):
    proveedores = cargar_datos()
    proveedores = [p for p in proveedores if p.id != id]
    guardar_datos(proveedores)

