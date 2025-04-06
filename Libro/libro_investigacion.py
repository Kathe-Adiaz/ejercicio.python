from Libro.libro import Libro


class LibroInvestigacion(Libro): 
    def __init__(self, titulo: str, autor: str, precio: float, facultad: str):
        super().__init__(titulo, autor, precio)
        self.facultad = facultad  

    def calcular_descuento(self) -> float:  
        return self.precio * 0.25  
    
    def __str__(self):
        return super().__str__() + f"\nFacultad: {self.facultad}\nTipo: Libro de Investigación UdeC (25% descuento)"
