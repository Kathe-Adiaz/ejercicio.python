from Libro.libro import Libro

class Novela(Libro):
    def __init__(self, titulo: str, autor: str, precio: float, genero: str):
        super().__init__(titulo, autor, precio)
        self.genero = genero

    def calcular_descuento(self) -> float:
        return self.precio * 0.15