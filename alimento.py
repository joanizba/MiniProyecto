class Alimento:

    def __init__(self, tipo, cantidad):
        self.tipo = tipo
        self.cantidad = cantidad

    def usar(self, cantidad):
        return cantidad
    
    @staticmethod
    def es_alimento_adecuado(cls, tipo_animal):
        return True