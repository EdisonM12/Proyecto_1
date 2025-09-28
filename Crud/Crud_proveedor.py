import json
from itertools import product

from models.proveedor import Proveedor

archivo= "data/Proveedores.json"

def cargar_datos():
    try:
        with open(archivo, "r") as f: #abrir el archivo para cargar los datos
            data = json.load(f)
            return [Proveedor(**p) for p in data.get("preveedor", [])]
    except FileNotFoundError:
            return []

def guardar_datos(proveedor):
    with open(archivo, "w") as f:
        json.dump({"proveedor": [p.__dict__ for p in productos]}, f, indent=4)

def crear_proveedor(proveedor):
    proveedors = cargar_datos()
    proveedors.append(proveedor)
    guardar_datos(proveedors)

def obtener_proveedor():
    return cargar_datos()

def actualizar_proveedor(id, nombre: None, cedula: None, telefono: None, direccion: None, empresa: None ):
    proveedors = cargar_datos()
    for p in proveedors:
        if p.id == id:
            if nombre: p.nombre = nombre
            if cedula: p.cedula = cedula
            if telefono: p.telefono = telefono
            if direccion: p.direccion = direccion
            if empresa: p.empresa = empresa
    guardar_datos(proveedors)

def eliminar_productos(id):
    proveedors = cargar_datos()
    proveedors = [p for p in proveedors if p.id != id]
    guardar_datos(proveedors)

