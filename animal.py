class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hambre = 0
        self.sed = 50
    def alimentar(self):
        Arca.alimentar_animal(self)
        self.hambre=0
    def aguar(self):
        tomar = 100-self.sed
        Arca.dar_agua(self,tomar)
        self.sed = 0
    def estado(self):
        return f'Estado de {self.nombre}: Hambre: {self.hambre} Sed:{self.sed}'