from alimento import Alimento
from animal import Animal


class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "perro")


class Gato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, "gato")


class Heno(Alimento):
    def __init__(self, cantidad):
        super().__init__("heno", cantidad)


class Croquetas(Alimento):
    def __init__(self, cantidad):
        super().__init__("croquetas", cantidad)

    @staticmethod
    def es_alimento_adecuado(tipo_animal):
        return tipo_animal in ["perro", "gato"]
