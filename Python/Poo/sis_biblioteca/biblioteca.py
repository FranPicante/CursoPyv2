from CursoPy.curso.poo.sis_biblioteca.libro import Libro

class biblioteca:

    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_libros = []

    def agregar_libro(self, nombre, autor, categoria):
        libro = Libro(nombre, autor, categoria)
        self.lista_libros.append(libro)
    
    def buscar_libro_nombre(self, nombre):
        libro_entontrado = []
        for libro in self.lista_libros:
            if libro.nombre == nombre:
                libro_entontrado.append(libro)
        return libro_entontrado
    
    def buscar_libro_autor(self, autor):
        libro_entontrado = []  
        for libro in self.lista_libros:
            if libro.autor == autor:
                libro_entontrado.append(libro)
        return libro_entontrado 