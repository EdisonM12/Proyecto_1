from Crud import Cru_producto
import json
import os
from datetime import datetime

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

#
def registrar_movimiento(id_producto, tipo, cant):
    #Registra un movimiento de inventario (si es COMPRA o VENTA)
    #Ajusta stock del producto y lo guarda en Kardex.json
    productos = Cru_producto.cargar_datos()
    producto = next((p for p in productos if p.id == id_producto), None)
    if not producto:
        print("Producto no encontrado")
        return

    tipo = tipo.upper()
    stock_anterior = producto.stock

    if tipo == "COMPRA":
        if cant <= 0:
            print("Cantidad debe ser positiva")
            return
        producto.stock += cant
    elif tipo == "VENTA":
        if cant <= 0:
            print("Cantidad debe ser positiva")
            return
        if cant > producto.stock:
            print("Stock insuficiente")
            return
        producto.stock -= cant
    else:
        print("Tipo de movimiento inválido. Use 'COMPRA' o 'VENTA'")
        return

    # Guardar producto actualizado
    Cru_producto.guardar_datos(productos)

    # Crear registro en kardex
    movimientos = cargar_movimientos()
    movimiento = {
        "id_mov": len(movimientos) + 1,
        "id_producto": producto.id,
        "Categoria":{
           "id": producto.categoria.id,
           "Nombre de categoria": producto.categoria.nombre
        } ,
        "cantidad": producto.cant,
        "fecha": datetime.now().isoformat(),
        "stock_anterior": stock_anterior,
        "stock_nuevo": producto.stock,
    }
    movimientos.append(movimiento)
    guardar_movimientos(movimientos)
    print("✅ Movimiento registrado correctamente")

def listar_movimientos():
    movimientos = cargar_movimientos()
    return movimientos

def actualizar_movimiento(id_mov, tipo=None, cantidad=None):
    movimientos = cargar_movimientos()
    for m in movimientos:
        if m["id_mov"] == id_mov:
            if tipo: m["tipo"] = tipo
            if cantidad: m["cantidad"] = cantidad
    guardar_movimientos(movimientos)

def eliminar_movimiento(id_mov):
    movimientos = cargar_movimientos()
    movimientos = [m for m in movimientos if m["id_mov"] != id_mov]
    guardar_movimientos(movimientos)
    print(f"Movimiento {id_mov} eliminado")


# Registrar movimientos

# Listar todos los movimientos
movs = listar_movimientos()
for m in movs:
    print(m)

# Actualizar un movimiento (opcional)
#actualizar_movimiento(1, cantidad=15)

# Eliminar un movimiento
#eliminar_movimiento(2)
