# Snake Game

Este proyecto es una versión propia del clásico juego de la serpiente, desarrollado en Python utilizando la biblioteca `turtle`.

## Estructura del Proyecto

El proyecto tiene la siguiente estructura de archivos:

### Archivos

- **food.py**: Contiene la clase `Food` que maneja la creación y posicionamiento aleatorio de la comida para la serpiente.
- **main.py**: Archivo principal que inicializa el juego, maneja la lógica principal y la interacción del usuario.
- **score_board.py**: Contiene la clase `Score` que maneja la puntuación y muestra el mensaje de "Game Over".
- **snake.py**: Contiene la clase `Snake` que maneja la creación, movimiento y crecimiento de la serpiente.

## Requisitos

- Python 3.x
- Biblioteca `turtle` (incluida en la instalación estándar de Python)

## Cómo Ejecutar el Juego

1. Clona este repositorio en tu máquina local.
2. Navega al directorio del proyecto.
3. Ejecuta el archivo `main.py`:
    - Desde la terminal escribe lo siguiente en el directorio del codigo

```sh
python main.py
```

## Controles del Juego

- **Flecha Izquierda:** Mover la serpiente a la izquierda.
- **Flecha Derecha:** Mover la serpiente a la derecha.
- **Flecha Arriba:** Mover la serpiente hacia arriba.
- **Flecha Abajo:** Mover la serpiente hacia abajo.
- **Espacio:** Activar el "cheat" para crecer la serpiente y aumentar la puntuación. *[ Uso exclusivo para debugging ]*

## Logica del Juego

- La serpiente se mueve continuamente en la una direcion que puede ser modificada por el jugador.
- La comida aparece en posiciones aleatorias dentro de los límites de la pantalla.
- Cuando la serpiente come la comida, crece y la puntuación aumenta.
- El juego termina si la serpiente choca con los bordes de la pantalla o consigo misma.
- Al finalizar el juego, se muestra el mensaje "GAME OVER".

## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza tus cambios y haz commit (git commit -am 'Añadir nueva funcionalidad').
4. Haz push a la rama (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT.
.
  
______________  
# ¡Gracias por jugar Snake Game! Si tienes alguna pregunta o sugerencia, no dudes en abrir un issue o contactarme.
______________