class Orden:
    contador_orden = 0

    def __init__(self, lista_computadora):
        Orden.contador_orden += 1
        self.id_orden = Orden.contador_orden
        self.computadoras = lista_computadora

    def agregar_pc(self, computadora):
        self.computadoras.append(computadora)
    
    def __str__(self):
        lista_pc = ''
        for computadora in self.computadoras:
            lista_pc += '\n' +  computadora.__str__()
        return (f'''orden: {self.id_orden}\ncomputadoras: {lista_pc}''')
    