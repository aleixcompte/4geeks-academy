# Todo List CLI · Python

**Proyecto práctico de 4Geeks Academy**

> Ubicación académica provisional dentro de FLEX; se ajustará si el campus asigna el proyecto a otro programa o módulo.

## Objetivo

Aplicación de consola para registrar, listar y eliminar tareas numeradas, con persistencia local mediante `todos.csv`.

## Funciones

- `add_one_task(title)`: añadir una tarea.
- `print_list()`: consultar tareas numeradas.
- `delete_task(number_to_delete)`: eliminar una tarea por número.
- `save_todos()`: guardar las tareas en CSV.
- `load_todos()`: cargar las tareas desde CSV.
- Menú interactivo con múltiples operaciones.

## Ejecución

Desde esta carpeta:

```bash
python3 app.py
```

No se requieren dependencias externas.

## Estado de comprobación

- Sintaxis Python: PASS (verificado en Codespaces).
- Alta, listado, eliminación y persistencia CSV: verificados manualmente.
- Pruebas automáticas: no se identificaron archivos de pruebas en la plantilla utilizada.
- Código fuente publicado en este directorio: **sí**, a partir de la versión compartida y probada en Codespaces.
- Validación académica: **pendiente**.

## Archivos

- `app.py`: programa principal incluido.
- `todos.csv`: archivo local generado al guardar; no es necesario publicarlo con datos de uso.

[Volver a FLEX](../../README.md) · [Catálogo de proyectos](../../../../proyectos/README.md)
