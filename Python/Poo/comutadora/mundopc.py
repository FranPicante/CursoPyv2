from monitor import Monitor
from teclado import Teclado
from raton import Raton
from compu import Compu
from orden import Orden

print('*** App Mundo Pc***')

teclado1 = Teclado('Hp', 'usd')
raton1 = Raton('Logi', 'bt')
monitor1 = Monitor('Samsung', 20)
pc1 = Compu('Pc Prueba', monitor1, teclado1, raton1)

teclado2 = Teclado('Razer', 'usd')
raton2 = Raton('Zowi', 'usb')
monitor2 = Monitor('Gb', 30)
pc2 = Compu('Pc Gamer', monitor1, teclado1, raton1)

lista_pc = [pc1, pc2]
orden1 = Orden(lista_pc)
print(orden1)