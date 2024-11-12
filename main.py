from ArcaNoe import Arca, Alimento, Carn, Herb
from animal import Animal, Carnivoro, Herbivoro, Omnivoro


print("Hola Noe! Se acerca el diluvio universal, te necesitamos para salvar a las especies y organizar el Arca.")
while True:
    try:
        capacidad = int(input("Primero escoge la capacidad de animales del arca: \n"))
        break
    except ValueError:
        print("Eso no es un numero")
arca = Arca(capacidad)



while True:
    try:
        accion = int(input("1- Agregar animal\n2- Agregar alimento\n3- Rellenar agua\n4- Dar sed\n5- Dar hambre\n6- Dar agua\n7- Alimentar\n"))
        if accion == 1:
            nombre_an = input("Qué animal es? ")
            while True:
                tipo= int(input("Escoge el tipo de dieta:\n1- Carnívoro\n2- Herbivoro\n3- Omnivoro\n"))
                if tipo == 1:
                    animal_ag = Carnivoro(nombre_an, "Carnivoro")
                    break
                elif tipo == 2:
                    animal_ag = Herbivoro(nombre_an, "Herbivoro")
                    break
                elif tipo == 3:
                    animal_ag = Omnivoro(nombre_an, "Omnivoro")
                    break
                else:
                    print("Opcion no valida")
            arca.agregar_animal(animal_ag)
        elif accion ==2:
            nombre_al = input("Que alimento es? ")
            while True:
                try:
                    cantidad = int(input("Introduce la cantidad: "))
                    tipo= int(input("Escoge el tipo de alimento :\n1- Carnico\n2- Vegetal\n"))
                    if tipo == 1:
                        alimento_ag = Carn(nombre_al, cantidad, "Carnico")
                        break
                    elif tipo == 2:
                        alimento_ag = Herb(nombre_al, cantidad, "Vegetal")
                        break
                    else:
                        print("Opcion no valida")
                except ValueError:
                    print("Eso no es un numero")
            arca.agregar_alimento(alimento_ag)
        elif accion ==3:
            try:
                cantidad_agua = int(input("Cuantas porciones de agua quieres agregar?(1 porcion=25 unidades de sed)"))
                arca.agregar_agua(cantidad_agua)
            except ValueError:
                print("Eso no es un numero")
        elif accion == 4:
            animal_sed= input("A que animal le quieres subir la sed?")
            for animal in arca.animales:
                if animal.nombre == animal_sed:
                    niv_sed = int(input("Que porcentaje de sed tiene el animal? A mas alto, mas sed tiene"))
                    animal.dar_sed(niv_sed)
                    break
            else:
                print("Ese animal no existe")
        elif accion == 5:
            animal_hamb= input("A que animal le quieres subir el hambre?")
            for animal in arca.animales:
                if animal.nombre == animal_hamb:
                    hambruna = int(input("Que porcentaje de hambre tiene el animal? A mas alto, mas hambre tiene"))
                    animal.dar_hambre(hambruna)
                    break
            else:
                print("Ese animal no existe")
            
        elif accion == 6:
            animal_agua= input("A que animal quieres darle agua? ")
            arca.dar_agua(animal_agua)

        elif accion == 7:
            animal_alimentar = input("A que animal quieres alimentar? ")
            for animals in arca.animales:
                if animals.nombre == animal_alimentar:
                    animals.es_adecuado(animal_alimentar)

        elif accion==20:
            a_estado= input("De que animal quieres saber el estado? ")
            for animal in arca.animales:
                if animal.nombre.lower() == a_estado.lower():
                    animal.estado()
        elif accion == 21:
            for animal in arca.animales:
                print(f"Animal: {animal.nombre} Tipo: {animal.tipo}")
            for alimento in arca.alimentos:
                print(f"Alimento: {alimento.nombre} Cantidad:{alimento.cantidad} Tipo: {alimento.tipo}")
        elif accion == 9:
            break
        elif accion == 22:
            arca.estado_arca()
    except ValueError:
        print("Que haces?")

"""
1- Agregar animal\n2-Agregar alimento\n3- Alimentar animal\n4- Dar agua a animal

instancia_arca = Arca(2)
alimento1= Alimento("Manzana", 20)
alimento2= Alimento("Trigo", 15)
instancia_arca.agregar_alimento(alimento1)
instancia_arca.agregar_alimento(alimento2)
for alimento in instancia_arca.alimentos:
    print(f"{alimento.tipo} ({alimento.cantidad})")
"""