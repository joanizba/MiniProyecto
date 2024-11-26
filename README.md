# 🐾 MiniProyecto: Arca de Noé

**Autores**: Joan & Armen  
**Repositorio**: [joanizba/MiniProyecto](https://github.com/joanizba/MiniProyecto)

## 📖 Descripción

Este proyecto implementa una simulación de la famosa **Arca de Noé** utilizando programación orientada a objetos (OOP) en Python. La simulación incluye clases para modelar animales, alimentos y el propio arca, con métodos para gestionar los recursos y mantener a los animales alimentados e hidratados.

## 🚀 Características

- **Clases de Python**: Uso extensivo de OOP para definir `Animal`, `Alimento`, y `Arca`.
- **Gestión de Recursos**: Métodos para agregar animales, alimentos y agua, así como para alimentar y dar agua a los animales.
- **Extensibilidad**: Clases base como `Animal` y `Alimento` pueden ser extendidas para crear nuevos tipos específicos de animales y alimentos.

## 📂 Estructura del Proyecto

- MiniProyecto/ 
- ArcaNoe.py # Clase principal para gestionar el arca 
- alimento.py # Clase para manejar los alimentos 
- animal.py # Clase base para definir los animales 
- main.py # Script principal para ejecutar la simulación 
- README.md # Documentación del proyecto


## 🛠️ Instalación

Sigue estos pasos para clonar y ejecutar el proyecto en tu entorno local:

- Clona el repositorio:    
   ```bash
   git clone https://github.com/joanizba/MiniProyecto.git
- Navega al directorio del proyecto:
    ```bash
    cd MiniProyecto
- Ejecuta el script principal:
    ```bash
    python main.py

## 🐶 Ejemplo de Uso
   ### Flujo de Interacción
   Una vez que el proyecto está configurado, puedes interactuar con el programa utilizando el menú principal. A       
   continuación se describe cómo realizar las acciones disponibles.
   #### Menú Principal:
   Cuando ejecutes el programa, verás un menú con las siguientes opciones:
      1. **Agregar animal**  
      2. **Agregar alimento** 
      3. **Rellenar agua** 
      4. **Subir sed a un animal** 
      5. **Subir hambre a un animal** 
      6. **Dar agua a un animal** 
      7. **Alimentar a un animal** 
      20. **Ver estado de un animal** 
      21. **Ver estado general** 
      22. **Ver estado del arca** 
      9.  **Salir**

   
#### Ejemplos de Escenarios:

   1. **Agregar un Animal**
      - Selecciona la opción `1` en el menú.
      - Especifica el nombre del animal y selecciona el tipo de dieta:
        ```
        Qué animal es? 
        > León
        Escoge el tipo de dieta:
        1- Carnívoro
        2- Herbívoro
        3- Omnívoro
        > 1
        ```
   
   2. **Agregar Alimento**
      - Selecciona la opción `2`.
      - Ingresa los detalles del alimento, su cantidad, y su clasificación:
        ```
        Qué alimento es? 
        > Carne
        Introduce la cantidad:
        > 50
        Escoge el tipo de alimento:
        1- Cárnico
        2- Vegetal
        > 1
        ```
   
   3. **Rellenar Agua**
      - Selecciona la opción `3`.
      - Indica la cantidad de agua que deseas añadir:
        ```
        Cuántas porciones de agua quieres agregar? (1 porción = 25 unidades de sed)
        > 10
        ```
   
   4. **Dar Agua a un Animal**
      - Selecciona la opción `6`.
      - Especifica el nombre del animal al que quieres hidratar:
        ```
        A qué animal quieres darle agua?
        > León
        ```
   
   5. **Alimentar a un Animal**
      - Selecciona la opción `7`.
      - Introduce el nombre del animal al que quieres alimentar:
        ```
        A qué animal quieres alimentar?
        > León
        ```
   
   6. **Ver Estado del Arca**
      - Selecciona la opción `22`.
      - Obtendrás un informe general del estado del arca, incluyendo el número de animales, alimentos disponibles, y la 
        cantidad de agua restante:
        ```
        Animales en el arca: 1
        Alimentos disponibles: 1
        Agua restante: 200 unidades
        ```
   
   7. **Salir del Programa**
      - Selecciona la opción `9` para terminar la sesión:
        ```
        Adiós, Noé. ¡Buena suerte con el diluvio!
     ```

---

### Personalización del Código

Si necesitas personalizar el flujo o añadir nuevas funcionalidades, puedes modificar el archivo principal `main.py`. ¡Explora todas las posibilidades y adapta el sistema a tus necesidades específicas!

   
      
## 🌱 Contribuciones
Las contribuciones son bienvenidas. Si deseas colaborar, sigue estos pasos:

Haz un fork del repositorio.
- Crea una nueva rama: git checkout -b feature/nueva-funcionalidad.
- Realiza tus cambios y haz un commit: git commit -m 'Añadir nueva funcionalidad'.
- Envía tus cambios: git push origin feature/nueva-funcionalidad.
## 📝 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

