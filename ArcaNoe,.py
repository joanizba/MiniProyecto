class Arca:
    animales = []
    alimentos = []
    agua = 100
    capacidad_maxima = 0
    def __init__(cls, capacidad):
        cls.capacidad_maxima = capacidad
    def agregar_animal(cls, animal):
        if len(cls.animales)< cls.capacidad_maxima:
            cls.animales.append(animal)
        else:
            return f'Está el tope'
    def agregar_alimento(cls, alimento):
        cls.alimentos.append(alimento)
        
    def agregar_agua(cls, cantidad):
        cls.agua += cantidad
        return cls.agua
    def alimentar_animal(cls, animal):
        if animal in cls.animales:
            cls.alimentos.pop()
        return cls.alimentos
    def dar_agua(cls, animal,tomar):
        if animal in cls.animales:
            cls.agua -= tomar
        return cls.agua