from poo.porgrama_boblioteca.libros import Libro
from poo.porgrama_boblioteca.biblioteca import Biblioteca


print('*** sistema de bibliotecas ***')

biblioteca1 = Biblioteca('biblioñaña')

libro1 = Libro('el gran infiel', 'cristian', 'suspenso')
libro2 = Libro('lo que el ñaña se llevo', 'ñaña', 'drama')
libro3 = Libro('100 años de infidelidad', 'cristian', 'drama')
libro4 = Libro('la ñaña en tiempo de guerra', 'ñaña', 'terror')

biblioteca1.agregar_libro(Libro('el gran infiel', 'cristian', 'suspenso'))
biblioteca1.agregar_libro(libro2)
biblioteca1.agregar_libro(libro3)
biblioteca1.agregar_libro(libro4)


autor = 'ñaña'
print(f'libros de {autor}')
biblioteca1.buscar_libro_autor(autor)

categoria = 'drama'
print(f'libros de {categoria}')
biblioteca1.buscar_libro_categoria(categoria)

biblioteca1.mostrar_todo()
