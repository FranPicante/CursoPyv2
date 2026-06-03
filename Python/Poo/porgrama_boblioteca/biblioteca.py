from poo.porgrama_boblioteca.libros import Libro

class Biblioteca:

    def __init__(self, nombre):
        self._nombre = nombre
        self._lista_libros = []

    def agregar_libro(self, libro):
        self._lista_libros.append(libro)
    
    def buscar_libro_autor(self, autor):
        for libro in self._lista_libros:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libro(libro)#le pasa el libro que encontro al metodo encontrar
    
    def buscar_libro_categoria(self, categoria):
        for libro in self._lista_libros:
            if libro.categoria.lower() == categoria.lower():
                self.mostrar_libro(libro)#le pasa el libro que encontro al metodo encontrar

    def mostrar_todo(self):
        print(f'todos los libro de la biblioteca {self._nombre}')
        for libro in  self._lista_libros:
            self.mostrar_libro(libro)
    
    def mostrar_libro(self, libro):
        print(f'titulo: {libro.nombre} - autor: {libro.autor} - categoria: {libro.categoria}')

    @property
    def nombre(self):
        return self._nombre
    

if __name__ == '__main__':
    biblioteca1 = Biblioteca ('ñaña')
    libro1 = Libro('el gran infiel', 'cristian', 'suspenso')

    biblioteca1.agregar_libro(libro1)
    
    biblioteca1.mostrar_todo()