# Inicializamos el arca con capacidad máxima de 10 elementos
from ArcaNoe import Arca
from derivados import Croquetas, Gato, Heno, Perro

def __main__():
    Arca.__init__(10)

    # Creamos animales
    perro = Perro("Rex")
    gato = Gato("Miau")

    # Creamos alimentos
    heno = Heno(5)
    croquetas = Croquetas(10)

    # Añadimos animales y alimentos al arca
    Arca.agregar_animal(perro)
    Arca.agregar_animal(gato)
    Arca.agregar_alimento(heno)
    Arca.agregar_alimento(croquetas)

    # Añadimos agua al arca
    Arca.agregar_agua(20)

    # Alimentamos a los animales y les damos agua
    Arca.alimentar_animal(perro)
    Arca.dar_agua(perro)

    Arca.alimentar_animal(gato)
    Arca.dar_agua(gato)

    # Verificamos el estado del arca
    print("Estado del arca:", Arca.estado_arca())

    # Mostramos el estado de los animales
    print(perro.estado())
    print(gato.estado())
