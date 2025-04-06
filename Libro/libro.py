class Libro:
    def __init__(self, titulo: str, autor: str, precio: float):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def calcular_descuento(self) -> float:
        raise NotImplementedError("Método abstracto: implementar en subclases")