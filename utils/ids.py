# import json
#
# def generar_id_producto(archivo="data/Productos.json") -> int:
#     try:
#         with open(archivo, "r", encoding="utf-8") as f:
#             data = json.load(f)
#     except FileNotFoundError:
#         return 1  # si no existe el archivo, empezamos desde 1
#
#     productos = data.get("Productos", [])
#     if not productos:
#         return 1  # si no hay productos, empezamos en 1
#
#     # Buscamos el ID más alto y sumamos 1
#     ultimo_id = max(p["id"] for p in productos)
#     return ultimo_id + 1
# import json
#
# def generar_id_producto(archivo="data/productos.json") -> int:
#     try:
#         with open(archivo, "r", encoding="utf-8") as f:
#             data = json.load(f)
#     except FileNotFoundError:
#         return 1  # si no existe el archivo, empezamos desde 1
#
#     productos = data.get("productos", [])
#     if not productos:
#         return 1  # si no hay productos, empezamos en 1
#
#     # Buscar el id mayor y sumarle 1
#     ultimo_id = max(p["id"] for p in productos)
#     return ultimo_id + 1
