class Libro:
    contador_libros = 0 

    def __init__(self, nombre, autor, categoria):
        self._nombre = nombre
        self._autor = autor
        self._categoria = categoria
        Libro.contador_libros += 1
        self.id = Libro.contador_libros

    @classmethod
    def meth_contador_libro(cls):
        return cls.contador_libros
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria
