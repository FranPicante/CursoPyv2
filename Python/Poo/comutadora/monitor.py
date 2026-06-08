class Monitor:
    contador_monitor = 0

    def __init__(self,marca , tamano):
        Monitor.contador_monitor += 1
        self.id_monitor = Monitor.contador_monitor
        self._marca = marca
        self._tamano = tamano

    def __str__(self):
        return (f'''Id monitor: {self.id_monitor} - Marca: {self._marca} - Tamaño: {self._tamano}''')