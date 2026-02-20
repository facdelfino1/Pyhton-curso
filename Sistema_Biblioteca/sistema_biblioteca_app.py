from biblioteca import Biblioteca
from libro import Libro

biblioteca_nacional = Biblioteca("Biblioteca Nacional")
print(f"Bienvenido a la {biblioteca_nacional.nombre}")

#definir algunos libros
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico")
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela")
libro3 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", "Realismo mágico")
libro4 = Libro("La sombra del viento", "Carlos Ruiz Zafón", "Misterio")

#agregar libros a la biblioteca
biblioteca_nacional.agregar_libro(libro1)
biblioteca_nacional.agregar_libro(libro2)
biblioteca_nacional.agregar_libro(libro3)
biblioteca_nacional.agregar_libro(libro4)

#buscar libros por autor
autor = "Gabriel García Márquez"
print(f"\nLibros del autor {autor}:")
biblioteca_nacional.buscar_libros_por_autor(autor)
autor1 = "Miguel de Cervantes"
print(f"\nLibros del autor {autor1}:")
biblioteca_nacional.buscar_libros_por_autor(autor1)

#buscar libros por género
genero = "Realismo mágico"
print(f"\nLibros del género {genero}:")
biblioteca_nacional.buscar_libros_por_genero(genero)

biblioteca_nacional.mostrar_todos_libros()