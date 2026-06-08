from monitor import Monitor
from teclado import Teclado
from raton import Raton

class Compu():
    contador_pc = 0

    def __init__(self, nombre, monitor, teclado, raton):
            Compu.contador_pc += 1
            self.id_pc = Compu.contador_pc
            self._nombre = nombre
            self._monitor = monitor
            self._teclado = teclado
            self._raton = raton
    
    def __str__(self):
          return (f'''\n{self._nombre}: {self.id_pc}\n{self._monitor}\n{self._teclado}\n{self._raton}\n''')

if __name__ == '__main__':
      teclado1 = Teclado('hp', 'usd')
      raton1 = Raton('logi', 'bt')
      monitor1 = Monitor('samsung', 20)
      pc1 = Compu('pc prueba', monitor1, teclado1, raton1)
      print(pc1)