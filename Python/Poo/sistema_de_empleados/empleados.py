class Empleados:
    contador_empledos = 0

    def __init__(self, nombre, depto):
        self._nombre = nombre
        self._depto = depto
        Empleados.contador_empledos += 1
<<<<<<< HEAD
        self._id = Empleados.contador_empledos
=======
        self.id = Empleados.contador_empledos
>>>>>>> 4c85662d42d4fb23afa348d825c6ae569595b4e6

    @classmethod
    def meth_contador_empledos(cls):
        return cls.contador_empledos
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def depto(self):
        return self._depto
    @depto.setter
    def depto(self, depto):
        self._depto = depto

    def mostrar(self):
        print(f'{self.nombre}, {self.depto}')

if __name__ == '__main__':
    empleado1 = Empleados ('yo', 'ñaña')
<<<<<<< HEAD
    empleado1.mostrar()
=======
    empleado1.mostrar()
>>>>>>> 4c85662d42d4fb23afa348d825c6ae569595b4e6
