# 🚢 Juego de Batalla Naval en Python

Este proyecto es un juego clásico de **Batalla Naval**, desarrollado completamente en **Python**. La versión principal y final es `batalla_naval_final.py`, la cual ofrece una experiencia mejorada con respecto a versiones anteriores.

## 🎮 Descripción del Juego

El jugador compite contra la computadora en un tablero de 5x5, donde cada uno coloca sus barcos estratégicamente. Luego, se turnan para disparar a posiciones específicas con el objetivo de hundir los barcos del oponente.

### Características:

- Modo de juego por turnos (jugador vs computadora).
- Colocación aleatoria de barcos para el jugador y la máquina.
- Feedback visual de impactos y fallos.
- Indicadores de quién gana y pierde.
- Control de flujo para repetir partidas si el jugador lo desea.

## 📁 Archivos del Proyecto

- `batalla_naval_final.py`: ✅ **Versión final y funcional del juego**.
- `batalla_naval_changes.py`: 🧪 Versión previa con cambios parciales o funciones en desarrollo.

## 🧠 Estructura del Código

El juego está dividido en varias funciones:

- `crear_tablero()`: Genera un tablero vacío.
- `colocar_barcos()`: Coloca los barcos en el tablero de forma aleatoria.
- `mostrar_tablero()`: Muestra el estado del tablero al jugador.
- `disparar()`: Permite al jugador ingresar coordenadas de ataque.
- `disparo_computadora()`: Lógica aleatoria para ataques enemigos.
- `jugar()`: Función principal que ejecuta la partida completa.

## ▶️ Cómo Ejecutarlo

### Requisitos:

- Python 3 instalado en tu sistema (Windows, macOS o Linux).

### Instrucciones:

```bash
python batalla_naval_final.py
```

El juego se ejecutará en la terminal. Sigue las instrucciones para comenzar a jugar.

## 📝 Ejemplo de Flujo del Juego

```
Bienvenido a la Batalla Naval 🚢
Tablero de juego (5x5)

Turno del jugador: Ingresa coordenadas (ej. 2 3)
¡Impacto!
Turno de la computadora...
¡La computadora falló!

...

¡Felicidades! Has ganado 🏆
```

## 👨‍💻 Autor

Leonardo, con ayuda de ChatGPT 😊  

🧡 Este proyecto fue hecho con dedicación, como parte de mi camino para dominar la programación en Python.
