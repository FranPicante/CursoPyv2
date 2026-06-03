class Persona:

    def __init__(self, nombre, apellido):
         self.nombre = nombre
         self.apellido = apellido

    def mostrar_persona(self):
        print(f'''persona
            nombre: {self.nombre}
            apellido: {self.apellido}
            id: {id(self)}
            id hex: {hex(id(self))}''')

if __name__ == '__main__':
    persona1 = Persona('yo', 'yo apellido')
    persona1.mostrar_persona()