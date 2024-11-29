from animal import Animal
class Arca:
    animales = []
    alimentos = []
    agua = 100
    agua_sobrante=0
    def __init__(cls, capacidad):
        cls.capacidad_maxima = capacidad
    def agregar_animal(cls, animal):
        if len(cls.animales)< cls.capacidad_maxima:
            cls.animales.append(animal)
        else:
            print(f'Está el tope')
    def agregar_alimento(cls, alimento):
        cls.alimentos.append(alimento)
        
    def agregar_agua(cls, cantidad):
        cls.agua += cantidad
        if cls.agua >= 500:
            cls.agua -= cantidad
        return cls.agua
    def alimentar_animal(cls, alimento):
        
        if alimento in cls.alimentos:
            cls.alimentos.pop(alimento)
        else:
            print("No esiste")
    def dar_agua(cls, animal):
        for animals in cls.animales:
            if animals.nombre == animal:
                if animals.sed > 0:
                    litros = cls.agua* 25
                    litros -= animals.sed
                    cls.agua = litros //25
                    if litros%25 != 0:
                        cls.agua_sobrante += litros%25
                        if cls.agua_sobrante == 25:
                            cls.agua += cls.agua_sobrante/25
                    Animal.aguar(animals)
                else:
                    print("El animal no tiene sed")
            else:
                print("Ese animal no existe")
    def estado_arca(cls):
        print(f"En el Arca hay {len(cls.animales)} animales")
        alimentos_totales = 0
        for aliments in cls.alimentos:
            alimentos_totales += aliments.cantidad
        print(f"En el Arca hay {len(cls.alimentos)} tipos de alimentos, {alimentos_totales} unidades de alimentos")
        print(f"En el Arca hay {cls.agua} porciones de agua")

