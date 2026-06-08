from perifericos import Perifericos

class Teclado(Perifericos):
    contador_teclado = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)
    
    def __str__(self):
        return (f'''Id teclado: {self.id_teclado} - Marca: {self._marca} - Tipo de entrada: {self._tipo_entrada}''')

if __name__ == '__main__':
    teclado1 = Teclado('hp', 'usb')
    print(teclado1)

    teclado2 = Teclado('logi', 'bt')
    print(teclado2)