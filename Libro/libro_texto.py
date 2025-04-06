from Libro.libro import Libro

class LibroTexto(Libro):
    def __init__(self, titulo: str, autor: str, precio: float, curso: str):
        super().__init__(titulo, autor, precio)
        self.curso = curso

    def calcular_descuento(self) -> float:
        return self.precio * 0.40