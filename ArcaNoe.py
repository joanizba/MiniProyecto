class Arca:
    animales = []
    alimentos = []
    agua = 100
    capacidad_maxima = 0

    @classmethod
    def __init__(cls, capacidad):
        cls.capacidad_maxima = capacidad
    
    @classmethod
    def agregar_animal(cls, animal):
        if len(cls.animales)< cls.capacidad_maxima:
            cls.animales.append(animal)
        else:
            return f'Está el tope'
    
    @classmethod
    def agregar_alimento(cls, alimento):
        cls.alimentos.append(alimento)

    @classmethod    
    def agregar_agua(cls, cantidad):
        cls.agua += cantidad
        return cls.agua
    
    @classmethod
    def alimentar_animal(cls, animal):
        for alimento in cls.alimentos:
            if alimento.es_alimento_adecuado(animal.tipo) and alimento.cantidad > 0:
                animal.alimentar()
                alimento.usar(1)
                print(f"{animal.nombre} ha sido alimentado por {alimento.tipo}")
                return
        print(f"No hay alimento adecuado para {animal.nombre}")

    @classmethod
    def dar_agua(cls, animal,tomar):
        if cls.agua > 0:
            animal.dar_agua()
            cls.agua =-1 
            print(f"{animal.nombre} ha recibido agua")
        else:
            print("Insuficiente agua")

    @classmethod
    def estado_arca(cls):
        estado = {
            "animales": len(cls.animales),
            "alimentos": len(cls.alimentos),
            "agua": cls.agua
        }

        return estado