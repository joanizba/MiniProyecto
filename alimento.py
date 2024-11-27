from ArcaNoe import Arca
from animal import Animal
class Alimento:
    def __init__(self, nombre, cantidad, tipo):
        self.nombre = nombre
        self.cantidad = cantidad
        self.tipo = tipo
    def usar(self, cantidad_u):
        if self.cantidad >= cantidad_u :
            self.cantidad -= cantidad_u
            return 1
        else:
            print("No hay alimento suficiente")

    def es_adecuado( animal):
        if animal.tipo=="Carnivoro":
            cantidad = Carn.alimentar_carne(animal)
        elif animal.tipo == "Herbivoro":
            cantidad= Herb.alimentar_vegetal()
        elif animal.tipo =="Omnivoro":
            i=1
            for aliments in Arca.alimentos:
                print(f"{i}- {aliments.nombre} | {aliments.cantidad} unidades")
                i+=1
            while True:
                try:
                    choose= int(input("Introduce el alimento de la lista con el que quieres alimentar, si quieres salir escribe 666"))
                    if 1<= choose <= len(Arca.alimentos):
                        alimento_seleccionado = alimentos_carnics[choose-1]
                        cantidad = int(input("Cuanto le quieres dar(una unidad elimina 25 de hambre, las sobras se pierden)? "))
                        alimento_seleccionado.usar(cantidad)
                    elif choose == 666:
                        break
                    else :
                        print("Fuera de rango")
                except ValueError:
                    print("Error")
        animal.alimentar(cantidad)
        
class Carn(Alimento):
    def alimentar_carne(self):
        alimentos_carnics= [aliments for aliments in Arca.alimentos if aliments.tipo == "Carnico"]
        print("Puedes alimentar con:\n")
        i=1
        for aliments in alimentos_carnics:
            print(f"{i}- {aliments.nombre} | {aliments.cantidad} unidades")
            i+=1
        while True:
            try:
                choose= int(input("Introduce el alimento de la lista con el que quieres alimentar, si quieres salir escribe 666: "))
                if 1<= choose <= len(alimentos_carnics):
                    alimento_seleccionado = alimentos_carnics[choose-1]
                    cantidad = int(input("Cuanto le quieres dar(una unidad elimina 25 de hambre, las sobras se pierden)? "))
                    alimento_seleccionado.usar(cantidad)
                    return cantidad
                elif choose == 666:
                    break
                else :
                    print("Fuera de rango")
            except ValueError:
                print("Error")

class Herb(Alimento):
    def alimentar_herb(self):
        alimentos_herb= [aliments for aliments in Arca.alimentos if aliments.tipo == "Herb"]
        print("Puedes alimentar con:\n")
        i=1
        for aliments in alimentos_herb:
            print(f"{i}- {aliments.nombre} | {aliments.cantidad} unidades")
            i+=1
        while True:
            try:
                choose= int(input("Introduce el alimento de la lista con el que quieres alimentar, si quieres salir escribe 666"))
                if 1<= choose <= len(alimentos_herb):
                    alimento_seleccionado = alimentos_herb[choose-1]
                    cantidad = int(input("Cuanto le quieres dar(una unidad elimina 25 de hambre, las sobras se pierden)? "))
                    alimento_seleccionado.usar(cantidad)
                    return cantidad
                elif choose == 666:
                    break
                else :
                    print("Fuera de rango")
            except ValueError:
                print("Error")
