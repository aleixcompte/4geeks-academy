# Lista de tareas en Python

He creado una aplicación de terminal para añadir tareas, verlas numeradas y eliminarlas por su posición. También puedo guardarlas en `todos.csv` y volver a cargarlas.

## Funciones

- `add_one_task(title)`: añade una tarea.
- `print_list()`: muestra la lista numerada.
- `delete_task(number_to_delete)`: elimina la tarea indicada.
- `save_todos()`: guarda la lista en CSV.
- `load_todos()`: recupera la lista del CSV.

El menú permite utilizar estas funciones sin modificar el código.

## Ejecución

Desde la carpeta del proyecto:

```bash
python3 app.py
```

He comprobado que puedo añadir, consultar, eliminar, guardar y recuperar tareas después de cerrar y volver a abrir el programa.
