from perifericos import Perifericos

class Raton(Perifericos):
    contador_ratones = 0 

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        self.marca = marca
        self.tipo_entrada = tipo_entrada
        #super().__init__(marca, tipo_entrada)
    
    def __str__(self):
        return (f'''Id raton: {self.id_raton} - Marca: {self.marca} - Tipo de entrada: {self.tipo_entrada}''')
    
if __name__ == '__main__':
        ratoin1 = Raton('hp', 'usb')
        ratoin2 = Raton('logi', 'usb')

        print(ratoin1)
        print(ratoin2)
