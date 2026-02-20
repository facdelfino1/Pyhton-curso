from libro import Libro

class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = [] # Atributo de instancia
    
    def agregar_libro(self, libro:Libro):
        self._libros.append(libro)
    
    def buscar_libros_por_autor(self,autor):
     
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libro(libro)
    
    def buscar_libros_por_genero(self,genero):
        for libro in self._libros:
            if libro.genero.lower() == genero.lower():
                self.mostrar_libro(libro)
    
    def mostrar_todos_libros(self):
        for libro in self._libros:
            self.mostrar_libro(libro)

    def mostrar_libro(self, libro:Libro):
        print(f"El libro {libro.titulo} es del autor {libro.autor} y pertenece al genero {libro.genero}")

    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def libros(self):
        return self._libros