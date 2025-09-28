from dataclasses import dataclass, field
@dataclass
class Proveedor:
    id: int
    nombre: str
    cedula : int
    telefono: int
    direccion: str
    empresa: str
    def validadcion(self):
        if not self.nombre or not self.empresa:
            return False
        return True

    def validacion_telefono(self):
        if len(str(self.telefono)) < 10 or len(str(self.cedula)) < 10:
            return False
        return True




