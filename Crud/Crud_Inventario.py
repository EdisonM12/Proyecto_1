import json
import os
from datetime import datetime
from Crud import Cru_producto
from tabulate import tabulate
KARDEX_JSON = "data/Kardex.json"

def cargar_movimientos():
    if not os.path.exists(KARDEX_JSON) or os.path.getsize(KARDEX_JSON) == 0:
        return []
    try:
        with open(KARDEX_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("movimientos", [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_movimientos(movimientos):

    os.makedirs(os.path.dirname(KARDEX_JSON), exist_ok=True)
    with open(KARDEX_JSON, "w", encoding="utf-8") as f:
        json.dump({"movimientos": movimientos}, f, indent=4, ensure_ascii=False)

def registrar_movimiento(id_producto, tipo, cantidad):

    tipo = tipo.upper()
    productos = Cru_producto.cargar_datos()
    movimientos = cargar_movimientos()

    producto = next((p for p in productos if p.id == id_producto), None)
    if not producto:
        print(f"Producto con ID {id_producto} no encontrado")
        return

    stock_anterior = producto.stock

    if tipo == "COMPRA":
        producto.stock += cantidad
    elif tipo == "VENTA":
        if cantidad > producto.stock:
            print(f"Stock insuficiente para {producto.nombre}")
            return
        producto.stock -= cantidad
    else:
        print("Tipo inválido. Use 'COMPRA' o 'VENTA'")
        return

    movimiento = {
        "id_mov": len(movimientos) + 1,
        "tipo": tipo,
        "fecha": datetime.now().isoformat(),
        "productos": [{
            "id_producto": producto.id,
            "nombre": producto.nombre,
            "cantidad": cantidad,
            "stock_anterior": stock_anterior,
            "stock_nuevo": producto.stock
        }],
        "cantidad_total": cantidad
    }


    Cru_producto.guardar_datos(productos)
    movimientos.append(movimiento)
    guardar_movimientos(movimientos)

    print(f" Movimiento registrado correctamente (ID {movimiento['id_mov']})")

def listar_movimientos():

    return cargar_movimientos()

def actualizar_movimiento(id_mov, tipo=None, productos_ids_cant=None):

    movimientos = cargar_movimientos()
    for m in movimientos:
        if m["id_mov"] == id_mov:
            if tipo: m["tipo"] = tipo
            if productos_ids_cant:
                m["productos"] = []
                total = 0
                productos = Cru_producto.cargar_datos()
                for id_producto, cantidad in productos_ids_cant:
                    producto = next((p for p in productos if p.id == id_producto), None)
                    if producto:
                        m["productos"].append({
                            "id_producto": producto.id,
                            "nombre": producto.nombre,
                            "cantidad": cantidad,
                            "stock_anterior": producto.stock,
                            "stock_nuevo": producto.stock + cantidad if tipo=="COMPRA" else producto.stock - cantidad
                        })
                        total += cantidad
                m["cantidad_total"] = total
    guardar_movimientos(movimientos)

def eliminar_movimiento(id_mov):

    movimientos = cargar_movimientos()
    movimientos = [m for m in movimientos if m["id_mov"] != id_mov]
    guardar_movimientos(movimientos)
    print(f"Movimiento {id_mov} eliminado ")
