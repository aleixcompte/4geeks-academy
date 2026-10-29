# API de Lista de Tareas con Python y Flask

Proyecto realizado durante mi formación en 4Geeks Academy.

## Qué he construido

Una API REST para gestionar tareas utilizando Python y Flask.

## Funcionalidades

- GET /todos: consultar las tareas.
- POST /todos: añadir una tarea.
- DELETE /todos/<int:position>: eliminar una tarea por posición.

Las tareas se almacenan temporalmente en memoria.

## Cómo ejecutarlo

Instalar las dependencias:

    pipenv install

Iniciar la aplicación:

    pipenv run python src/app.py

La API estará disponible en:

http://127.0.0.1:3245/todos
