class Aritmetica:
    def __init__(self, uno, dos):
        self._uno = uno
        self._dos = dos

    def sumar(self):
        resultado = self._uno + self._dos
        print(f'{self.uno} + {self.dos} = {resultado}')
    
    def resta(self):
        resultado = self._uno - self._dos
        print(f'{self.uno} - {self.dos} = {resultado}')
    
    def multiplicacion(self):
       resultado = self._uno * self._dos
       print(f'{self.uno} * {self.dos} = {resultado}')

    def divicion(self):
        resultado = self._uno / self._dos
        print(f'{self.uno} / {self.dos} = {resultado}')

    @property
    def uno(self):
        return self._uno
    @uno.setter
    def uno(self, uno):
        self._uno = uno
    
    @property
    def dos(self):
        return self._dos
    @dos.setter
    def dos(self, dos):
        self._dos = dos

if __name__ == '__main__':
    operecion1 = Aritmetica(5 , 7)

class aritmetica:
    def __init__(self, uno, dos):
        self.uno = uno
        self.dos = dos

    def sumar(self):
        resultado = self.uno + self.dos
        print(f'{self.uno} + {self.dos} = {resultado}')
    
    def resta(self):
        resultado = self.uno - self.dos
        print(f'{self.uno} - {self.dos} = {resultado}')
    
    def multiplicacion(self):
        operando1 = self.uno
        operando2 = self.dos
        resultado = operando1 * operando2
        print(f'{self.uno} * {self.dos} = {resultado}')

    def divicion(self):
        operando1 = self.uno
        operando2 = self.dos
        resultado = operando1 / operando2
        print(f'{self.uno} / {self.dos} = {resultado}')

if __name__ == '__main__':
    operecion1 = aritmetica(5 , 7)
    operecion1.sumar()
    operecion1.resta()
    operecion1.multiplicacion()
    operecion1.divicion()

    print('')

    operecion2 = Aritmetica(12 , 1)
    operecion2 = aritmetica(12 , 1)
    operecion2.sumar()
    operecion2.resta()
    operecion2.multiplicacion()
    operecion2.divicion()