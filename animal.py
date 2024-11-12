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
    def alimentar(self):
        self.hambre=0
    def aguar(self):
        self.sed = 0
    def estado(self):
        print(f'Estado de {self.nombre}:\nHambre: {self.hambre}\nSed:{self.sed}')
    def es_adecuado(self, animal):
        for animals in Arca.animales:
            if animals.nombre == animal and animals.tipo=="Carnivoro":
                Carnivoro.alimentar_carne()
            elif animals.nombre == animal and animals.tipo == "Herbivoro":
                Herbivoro.alimentar_vegetal()
            elif animals.nombre == animal and animals.tipo =="Omnivoro":
                i=1
                for aliments in Arca.alimentos:
                    print(f"{i}- {aliments.nombre} / {aliments.cantidad} unidades")
                    i+=1

"""
LOCO TE HAS QEUDADO DONDE TE DICE QUE CARNIVORO NO TIENE EL ES_ADECUADO PORQUE SE LO PUSISTE EN LA CLASE 
ALIMENTO Y ESTABAS USANDO LA CLASE ANIMALS PARA COMPRAR.
"""
class Carnivoro(Animal):
    pass

class Herbivoro(Animal):
    pass
class Omnivoro(Animal):
    pass