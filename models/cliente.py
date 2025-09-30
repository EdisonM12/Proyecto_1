from dataclasses import dataclass
from models.compra import Compra
@dataclass
class Cliente:
    id = int
    nombre = str
    apellido = str
    telefono = int
    cedula = int
    direccion = str

    def presentar(self):
        return f"{self.nombre} {self.apellido}"

    def actualizar_contacto(self, nuevo_email=None, nuevo_telefono=None):
        if nuevo_email:
            self.email = nuevo_email
        if nuevo_telefono:
            self.telefono = nuevo_telefono
