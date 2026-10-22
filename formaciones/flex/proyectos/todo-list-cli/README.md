# Lista de tareas en Python

Este proyecto es una lista de tareas que funciona desde la terminal. Puedo añadir tareas, consultar las que tengo pendientes y eliminar cualquiera indicando su número.

Las tareas se guardan en `todos.csv` para poder recuperarlas cuando vuelva a abrir el programa.

## Funciones

- `add_one_task(title)`: añade una tarea.
- `print_list()`: muestra todas las tareas numeradas.
- `delete_task(number_to_delete)`: elimina la tarea seleccionada por su posición.
- `save_todos()`: guarda la lista en `todos.csv`.
- `load_todos()`: carga las tareas guardadas.

El programa tiene un menú para utilizar estas opciones sin tener que modificar el código. No incluye edición de tareas, tal como indica la práctica.

## Cómo ejecutarlo

Con Python instalado, abro la terminal en esta carpeta y ejecuto:

```bash
python3 app.py
```

Después elijo una opción del menú, del 1 al 6. Al salir, la lista se guarda automáticamente.

## Comprobación

He probado añadir tareas, mostrarlas, eliminarlas y guardarlas. También he cerrado el programa, lo he vuelto a abrir y he comprobado que recupera los datos del CSV. He hecho las pruebas desde una copia descargada de GitHub.

No he ejecutado pruebas automáticas de la academia.
