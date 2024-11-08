class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hambre = 0
        self.sed = 50
    

    def alimentar(self):
        if self.hambre > 0:
            self.hambre -= 1
    
    def aguar(self):
        if self.sed > 0:
            self.sed -= 1

    def estado(self):
        return f'Estado de {self.nombre}: Hambre: {self.hambre} Sed:{self.sed}'