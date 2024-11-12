from ArcaNoe import Arca

class Alimento:
    def __init__(self, nombre, cantidad, tipo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.tipo = tipo
    def usar(self, cantidad_u):
        self.cantidad -= cantidad_u
    def es_adecuado(self, animal):
        for animals in Arca.animales:
            if animals.nombre == animal and animals.tipo=="Carnivoro":
                Carn.alimentar_carne()
            elif animals.nombre == animal and animals.tipo == "Herbivoro":
                Herb.alimentar_vegetal()
            elif animals.nombre == animal and animals.tipo =="Omnivoro":
                i=1
                for aliments in Arca.alimentos:
                    print(f"{i}- {aliments.nombre} / {aliments.cantidad} unidades")
                    i+=1
        
class Carn(Alimento):
    def alimentar_carne(self):
        i=1
        for aliments in Arca.alimentos:
            if aliments.tipo == "Carnico":
                print(f"{i}- {aliments.nombre} / {aliments.cantidad} unidades")
    pass

class Herb(Alimento):
    def alimentar_vegetal(self):
        i=1
        for aliments in Arca.alimentos:
            if aliments.tipo == "Vegetal":
                print(f"{i}- {aliments.nombre} / {aliments.cantidad} unidades")
    pass
