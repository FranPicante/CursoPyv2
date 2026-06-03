class Persona:

    contador_persona = 0

    def __init__(self, nombre, apellido):
        Persona.contador_persona += 1

        self._id = Persona.contador_persona
        self._nombre = nombre
        self.apellido = apellido
    
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido   

    def mostrar(self):
        print(f'id: {self._id} - nombre: {self._nombre} - apellido: {self._apellido}')

if __name__ == '__main__':
    persona1 = Persona('yo', '123')
    persona1.mostrar()

    persona2 = Persona('yo1', '456')
    persona2.mostrar()
    