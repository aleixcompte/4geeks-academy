# TicTacToe CLI con Python

Juego de tres en raya para dos jugadores, desarrollado en Python y ejecutado desde la terminal.

## Funcionamiento

- El jugador X comienza la partida.
- Los jugadores X y O se alternan automáticamente.
- El tablero tiene nueve posiciones, numeradas del 0 al 8.
- El juego detecta victorias y empates.
- Permite reiniciar la partida y salir en cualquier momento.

## Ejecución

```bash
python3 app.py
```

## Comandos

- `play 0` a `play 8`: colocar una ficha.
- `board`: mostrar el tablero.
- `new`: comenzar una nueva partida.
- `stop`: salir del juego.

## Comprobaciones

Se han probado las victorias de X y O, una victoria diagonal, el empate, el reinicio, las jugadas inválidas y la salida del programa.
