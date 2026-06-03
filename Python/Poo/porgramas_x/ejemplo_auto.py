class Auto:
    def __init__(self, marca , modelo, color):
        self._marca = marca
        self._modelo = modelo
        self._color = color

    def mostrar(self):
        print(f'''info del auto
            modelo : {self._modelo}
            marca: {self._marca}
            color: {self._color}''')
        
    #forma de usar el get
    @property
    def marca(self):
        return self._marca
    
    #forma de usar el set
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color


if __name__  == '__main__':
    auto1 = Auto ('yo', 'yo2', 'verde')
    auto1.mostrar()

    #se hace un set con los nuevos parametros
    auto1.modelo = 'yo1'
    auto1.color = 'azul'
    auto1.marca = 'yo00'
    auto1.mostrar()

    #