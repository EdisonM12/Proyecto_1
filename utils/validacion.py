def pedir_entero(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print(" Entrada inválida. Debe ser un número entero.")

def pedir_flotante(mensaje: str) -> float:
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print(" Entrada inválida. Debe ser un número.")
