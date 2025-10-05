from dataclasses import dataclass, asdict, field

@dataclass
class Proveedor:
    nombre: str
    cedula: int
    telefono: int
    direccion: str
    empresa: str
    id: int = field(init=False)
    id_contador = 0

    def __post_init__(self):
        type(self).id_contador += 1
        self.id = type(self).id_contador

    def validacion(self):
        if not self.nombre or not self.empresa:
            return False
        return True

    def validacion_telefono(self):
        if len(str(self.telefono)) < 10 or len(str(self.cedula)) < 10:
            return False
        return True

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):

        obj = cls(**{k: v for k, v in data.items() if k != "id"})

        obj.id = data.get("id", obj.id)

        cls.id_contador = max(cls.id_contador, obj.id)
        return obj
