from dataclasses import is_dataclass, asdict
import json, os

class ProductoRepo:
    def __init__(self, archivo="data/Productos.json"):
        self.archivo = archivo
        self.data = []
        self.cargar()

    def cargar(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                self.data = json.load(f)

    def guardar(self):
        os.makedirs(os.path.dirname(self.archivo), exist_ok=True)
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def agregar(self, producto):
        if is_dataclass(producto):
            self.data.append(asdict(producto))
        else:
            self.data.append(producto)
        self.guardar()

    def listar(self):
        return self.data

    def buscar(self, id_producto):
        for p in self.data:
            if p["id"] == id_producto:
                return p
        return None
