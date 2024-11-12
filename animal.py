class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hambre = 0
        self.sed = 50
    

    def alimentar(self):
        if self.hambre > 0:
            self.hambre -= 1
            print(f"{self.nombre} ha comido. Hambre actual: {self.hambre}")
    
    def aguar(self):
        if self.sed > 0:
            self.sed -= 1
            print(f"{self.nombre} ha bebido. Sed actual: {self.sed}")

    def estado(self):
        return f'Estado de {self.nombre}: Hambre: {self.hambre} Sed:{self.sed}'