# Функция для добавления новой задачи в список
def add_task(tasks, task):
    tasks.append(task)
    print("Новая задача добавлена!")


# Функция для отметки задачи как выполненной
def complete_task(tasks, index):
    if index >= 0 and index < len(tasks):
        tasks[index] = tasks[index] + " (выполнено)"
        print("Задача отмечена как выполненная!")
    else:
        print("Неверный номер задачи!")


# Функция для отображения списка задач
def show_tasks(tasks):
    if len(tasks) == 0:
        print("Список задач пуст")
    else:
        print("Текущий список задач:")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}")


# Основная функция приложения
def main():
    tasks = []

    while True:
        print("\nДоступные команды:")
        print("1. Добавить задачу")
        print("2. Отметить задачу выполненной")
        print("3. Показать список задач")
        print("4. Выйти из приложения")

        choice = input("Введите номер команды: ")

        if choice == "1":
            task = input("Введите новую задачу: ")
            add_task(tasks, task)
        elif choice == "2":
            show_tasks(tasks)
            index = int(input("Введите номер задачи, которую хотите отметить выполненной: ")) - 1
            complete_task(tasks, index)
        elif choice == "3":
            show_tasks(tasks)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверная команда, повторите ввод.")


if __name__ == "__main__":
    main()