from Libro.libro_texto import LibroTexto
from Libro.libro_investigacion import LibroInvestigacion
from Libro.novela import Novela

class ControladorEditorial:
    def __init__(self):
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def mostrar_libros(self):
        for libro in self.libros:
            print(libro)
            print("-------------------")

if __name__ == "__main__":
    controlador = ControladorEditorial()
    
    controlador.agregar_libro(LibroTexto("Álgebra Lineal", "Pedro Martínez", 75000, "Matemáticas"))
    controlador.agregar_libro(LibroInvestigacion("Machine Learning", "Ana López", 120000, "Ingeniería"))
    controlador.agregar_libro(Novela("1984", "George Orwell", 45000, "Ciencia Ficción"))
    
    
    controlador.mostrar_libros()