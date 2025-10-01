# from dataclasses import dataclass, field
# @dataclass
# class Proveedor:
#     id: int
#     nombre: str
#     cedula : int
#     telefono: int
#     direccion: str
#     empresa: str
#     def validadcion(self):
#         if not self.nombre or not self.empresa:
#             return False
#         return True
#
#     def validacion_telefono(self):
#         if len(str(self.telefono)) < 10 or len(str(self.cedula)) < 10:
#             return False
#         return True

from dataclasses import dataclass, asdict

@dataclass
class Proveedor:
    id: int
    nombre: str
    cedula: int
    telefono: int
    direccion: str
    empresa: str

    # ------------------- Validaciones -------------------
    def validadcion(self):
        if not self.nombre or not self.empresa:
            return False
        return True

    def validacion_telefono(self):
        if len(str(self.telefono)) < 10 or len(str(self.cedula)) < 10:
            return False
        return True

    # ------------------- Métodos para JSON -------------------
    def to_dict(self) -> dict:
        """Convierte el objeto Proveedor a un diccionario listo para JSON."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        """Crea un objeto Proveedor a partir de un diccionario."""
        return cls(**data)



