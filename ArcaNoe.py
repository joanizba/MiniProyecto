class Arca:
    animales = []
    alimentos = []
    agua = 0
    capacidad_maxima = 0

    @classmethod
    def __init__(cls, capacidad_maxima):
        cls.capacidad_maxima = capacidad_maxima

    @classmethod
    def agregar_animal(cls, animal):
        if len(cls.animales) + len(cls.alimentos) < cls.capacidad_maxima:
            cls.animales.append(animal)
            print(f"Animal agregado: {animal.nombre} ({animal.tipo})")
        else:
            print("⚠️ El arca está llena, no se puede agregar más animales.")

    @classmethod
    def agregar_alimento(cls, alimento):
        if len(cls.animales) + len(cls.alimentos) < cls.capacidad_maxima:
            cls.alimentos.append(alimento)
            print(f"Alimento agregado: {alimento.tipo}")
        else:
            print("⚠️ El arca está llena, no se puede agregar más alimentos.")

    @classmethod
    def agregar_agua(cls, cantidad):
        cls.agua += cantidad
        print(f"Agua agregada: {cantidad} litros")

    @classmethod
    def alimentar_animal(cls, nombre_animal):
        for animal in cls.animales:
            if animal.nombre == nombre_animal:
                for alimento in cls.alimentos:
                    if alimento.es_alimento_adecuado(animal.tipo) and alimento.cantidad > 0:
                        animal.alimentar()
                        alimento.usar(1)
                        return
                print(f"No hay alimento adecuado para {animal.nombre}.")
                return
        print(f"Animal no encontrado: {nombre_animal}")

    @classmethod
    def dar_agua(cls, nombre_animal):
        if cls.agua > 0:
            for animal in cls.animales:
                if animal.nombre == nombre_animal:
                    animal.dar_agua()
                    cls.agua -= 1
                    return
            print(f"Animal no encontrado: {nombre_animal}")
        else:
            print("No hay suficiente agua en el arca.")

    @classmethod
    def estado_arca(cls):
        estado = {
            "animales": len(cls.animales),
            "alimentos": len(cls.alimentos),
            "agua": cls.agua
        }
        return estado

    @classmethod
    def mostrar_estado_animales(cls):
        if not cls.animales:
            print("No hay animales en el arca.")
        else:
            for animal in cls.animales:
                print(animal.estado())
