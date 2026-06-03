from CursoPy.curso.poo.sistema_de_empleados.empleados import Empleados

class Empresa:

    def __init__(self, nombre):
        self._nombre = nombre
        self._empledos = []
    
    def contratar(sefl, nombre, depto):
        empledo = Empleados(nombre, depto)
        sefl._empledos.append(empledo)

    def empleados_x_depto(self,  depto):
        contador_empleados_por_depto = 0
        for empleado in self._empledos:
            if empleado.depto == depto:
                contador_empleados_por_depto += 1
        return contador_empleados_por_depto
    
    def total_empleados(self):          
        print(f'total de empleados de la empresa {self._nombre}')
        for empleado in self._empledos:
            print(f'''id: {empleado.id}
                nombre: {empleado.nombre}
                depto. {empleado.depto}''')
    
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

if __name__ == '__main__':
<<<<<<< HEAD
    empleado1 = Empleados ('yo', 'ñaña')
=======
    empleado1 = Empleados ('yo' 'ñaña')
>>>>>>> 4c85662d42d4fb23afa348d825c6ae569595b4e6
    