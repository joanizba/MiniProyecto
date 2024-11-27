from MiniProyecto.ArcaNoe import Arca

class Animal:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.hambre = 0
        self.sed = 0
    def dar_hambre(self, hambruna):
        self.hambre += hambruna 
    def dar_sed(self, niv_sed):
        self.sed += niv_sed
    def alimentar(self, cantidad):
        quita_hambre = cantidad*25
        self.hambre -= quita_hambre
        if self.hambre < 0:
            self.hambre= 0
    def aguar(self):
        self.sed = 0
    def estado(self):
        print(f'Estado de {self.nombre}:\nHambre: {self.hambre}\nSed:{self.sed}')

class Carnivoro(Animal):
    pass

class Herbivoro(Animal):
    pass
class Omnivoro(Animal):
    pass