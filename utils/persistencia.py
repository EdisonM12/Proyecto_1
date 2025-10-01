from dataclasses import dataclass, is_dataclass, asdict
import json
import os

Archivos_Datos = "data/almacenamiento.json"


_DEFAULT_DATA = {
    "autoinc": {"libro": 0, "socio": 0, "prestamo": 0},
    "productos": [],
    "administrador": [],
    "proveedores": []
}

def _deepcopy_default():
    return json.loads(json.dumps(_DEFAULT_DATA))

class RepoJson:
    def _init_(self, archivo= Archivos_Datos):
        self.archivo = archivo
        self.data= _deepcopy_default()
        self.cargar()

    def guardar_estado(self, data):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    def _flush(self):
        self.guardar_estado(self.data)

    def cargar(self):
        if not os.path.exists(self.archivo):
            self.guardar_estado(self.data)
            return
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                self.data = json.load(f)
            for k in _DEFAULT_DATA.keys():
                if k not in self.data:
                    self.data[k] = _deepcopy_default()
        except Exception as e:
            print(f"error, no se pudo cargar")
            self.data = _deepcopy_default()
            self.guardar_estado(self.data)

    def next_id(self, entidad):
        actual = self.data["autoinc"].get(entidad,0)
        self.data["autoinc"][entidad] = int(actual) + 1
        self._flush()
        return self.data["autoinc"][entidad]

    def leer_todo(self):
        ad = self.data.get("autoinc", {})
        return (
            {"producto": ad.get("libro", 0),"proveedores": ad.get("proveedores", 0), "administrador": ad.get("administrador", 0) },
            list(self.data.get("productos", [])),
            list(self.data.get("proveedores", [])),
            list(self.data.get("administrador", [])),
        )

    def guardar_listas(self, autonic, productos, proveedores, administrador):
        def to_dicts(items):
            out = []
            for it in items:
                if is_dataclass(it):
                    out.append(asdict(it))
                elif isinstance(it, dict):
                    out.append(it)

                else:
                    raise TypeError("solo se aceptan diccionario")
            return out

        self.data["autonic"] = {**self.data.get("autoinc",{}), **autonic}
        self.data["productos"] = to_dicts(productos)
        self.data["proveedores"] = to_dicts(proveedores)
        self.data["administrador"] = to_dicts(administrador)
        self._flush()