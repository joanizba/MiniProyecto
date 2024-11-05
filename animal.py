class Animal:
    
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hambre = 0
        self.sed = 0

    def alimentar(self):
        return self.hambre - 1
    

    def dar_agua(self):
        return self.sed - 1
    
    def estado(self):
        return 0