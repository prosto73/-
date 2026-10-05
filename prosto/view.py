


def show_collection(task_collection):
    print("=" * 45)

    if not task_collection:
        print("Список задач пуст!")
    else:
        for i, task in enumerate(task_collection):
            print(i + 1, task)

    print("=" * 45)

def show_menu():
    print("1 - Показать задачи \n"
          "2 - Добавить задачу \n"
          "3 - Редактировать задачи \n"
          "4 - Удаление задачи \n"
          "5 - Выход")