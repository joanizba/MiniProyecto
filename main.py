# Inicializamos el arca con capacidad máxima de 10 elementos
from ArcaNoe import Arca
from derivados import Croquetas, Gato, Heno, Perro

def menu():
    print("\n--- Menú del Arca de Noé ---")
    print("1. Agregar Animal")
    print("2. Agregar Alimento")
    print("3. Agregar Agua")
    print("4. Alimentar Animal")
    print("5. Dar Agua a Animal")
    print("6. Mostrar Estado del Arca")
    print("7. Mostrar Estado de Animales")
    print("0. Salir")
    return input("Elige una opción: ")


def main():
    try:
        capacidad = int(input("Ingresa la capacidad máxima del arca: "))
        Arca.__init__(capacidad)

        while True:
            opcion = menu()
            if opcion == "1":
                tipo = input("Tipo de animal (perro/gato): ").strip().lower()
                nombre = input("Nombre del animal: ")
                if tipo == "perro":
                    Arca.agregar_animal(Perro(nombre))
                elif tipo == "gato":
                    Arca.agregar_animal(Gato(nombre))
                else:
                    print("Tipo de animal no válido.")
            elif opcion == "2":
                tipo = input("Tipo de alimento (heno/croquetas): ").strip().lower()
                cantidad = int(input("Cantidad de alimento: "))
                if tipo == "heno":
                    Arca.agregar_alimento(Heno(cantidad))
                elif tipo == "croquetas":
                    Arca.agregar_alimento(Croquetas(cantidad))
                else:
                    print("Tipo de alimento no válido.")
            elif opcion == "3":
                cantidad = int(input("Cantidad de agua a agregar: "))
                Arca.agregar_agua(cantidad)
            elif opcion == "4":
                nombre = input("Nombre del animal a alimentar: ")
                animal = next((a for a in Arca.animales if a.nombre == nombre), None)
                if animal:
                    Arca.alimentar_animal(animal)
                else:
                    print("Animal no encontrado.")
            elif opcion == "5":
                nombre = input("Nombre del animal a dar agua: ")
                animal = next((a for a in Arca.animales if a.nombre == nombre), None)
                if animal:
                    Arca.dar_agua(animal)
                else:
                    print("Animal no encontrado.")
            elif opcion == "6":
                print("Estado del arca:", Arca.estado_arca())
            elif opcion == "7":
                Arca.mostrar_estado_animales()
            elif opcion == "0":
                print("Saliendo del programa. ¡Hasta luego!")
                break
            else:
                print("Opción no válida.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()