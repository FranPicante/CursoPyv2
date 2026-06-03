from CursoPy.curso.poo.sistema_de_empleados.empresa import Empresa
from CursoPy.curso.poo.sistema_de_empleados.empleados import Empleados

print('*** Sistema prueba empleados ***')

empresa1 = Empresa('ñaña llc')
empresa1.contratar('cristian ñaña', 'desarrollo')
empresa1.contratar('yo', 'desarrollo')
empresa1.contratar('bet', 'soporte')

<<<<<<< HEAD
print(f'contador de empleados:')
=======
print(f'contador de empleados: {Empleados.contador_empledos}')
>>>>>>> 4c85662d42d4fb23afa348d825c6ae569595b4e6
print(f'empleados en desarrollo: {empresa1.empleados_x_depto('desarrollo')}')
empresa1.total_empleados()