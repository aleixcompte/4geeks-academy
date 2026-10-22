import csv

# Todo List CLI - 4Geeks Academy

todos = []


def add_one_task(title):
    title = title.strip()

    if not title:
        print("Error: la tarea no puede estar vacía")
        return

    todos.append(title)
    print("Tarea añadida correctamente")


def print_list():
    print("\nLISTA DE TAREAS")

    if not todos:
        print("No hay tareas pendientes")
        return

    for number, task in enumerate(todos, start=1):
        print(f"{number}. {task}")


def delete_task(number_to_delete):
    if 1 <= number_to_delete <= len(todos):
        removed = todos.pop(number_to_delete - 1)
        print(f"Tarea eliminada: {removed}")
    else:
        print("Error: número de tarea no válido")


def save_todos():
    with open("todos.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        for task in todos:
            writer.writerow([task])

    print("Tareas guardadas correctamente en todos.csv")


def load_todos():
    try:
        with open("todos.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            loaded = [row[0] for row in reader if row]

        todos.clear()
        todos.extend(loaded)
        print("Tareas cargadas correctamente")

    except FileNotFoundError:
        print("No existe todavía el archivo todos.csv")


def main():
    load_todos()

    while True:
        print("\n===== TODO LIST CLI =====")
        print("1. Añadir tarea")
        print("2. Mostrar tareas")
        print("3. Eliminar tarea")
        print("4. Guardar tareas")
        print("5. Cargar tareas")
        print("6. Salir")

        option = input("\nSelecciona una opción: ").strip()

        if option == "1":
            title = input("Escribe la nueva tarea: ")
            add_one_task(title)

        elif option == "2":
            print_list()

        elif option == "3":
            print_list()

            try:
                number = int(input("Número de tarea a eliminar: "))
                delete_task(number)
            except ValueError:
                print("Error: introduce un número entero")

        elif option == "4":
            save_todos()

        elif option == "5":
            load_todos()

        elif option == "6":
            save_todos()
            print("Hasta pronto")
            break

        else:
            print("Error: opción no válida")


if __name__ == "__main__":
    main()
