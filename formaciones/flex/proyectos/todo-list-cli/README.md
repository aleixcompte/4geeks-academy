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

**Verificación funcional manual completada (22 de octubre de 2026)** sobre una copia nueva clonada desde GitHub en Codespaces.

| Prueba | Resultado |
| --- | --- |
| Clonar repositorio y verificar sintaxis | PASS |
| Iniciar aplicación sin `todos.csv` | PASS |
| Mostrar lista vacía | PASS |
| Rechazar eliminación con índice inexistente | PASS |
| Rechazar opción de menú no válida | PASS |
| Añadir y listar una tarea | PASS |
| Guardar la tarea en `todos.csv` | PASS |
| Reiniciar y recuperar la tarea | PASS |
| Eliminar la tarea por posición | PASS |
| Comprobar lista vacía y guardar | PASS |
| `git status --short` sin cambios pendientes | PASS |

**Pruebas automáticas oficiales:** no ejecutadas; no se encontraron archivos de test en la plantilla utilizada.

**Entrega al profesorado:** pendiente. **Validación académica:** pendiente.

Se trata de pruebas manuales de funcionamiento, no de una calificación o certificación oficial.

## Archivos

- `app.py`: programa principal incluido.
- `todos.csv`: archivo local generado al guardar; no es necesario publicarlo con datos de uso.

[Volver a FLEX](../../README.md) · [Catálogo de proyectos](../../../../proyectos/README.md)
