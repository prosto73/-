from utilits import check_confirm

def delete_tasks(task_collection):
    delete_task = input("Введите номер задачи: ")
    if check_confirm(delete_task, task_collection):
        task_collection.pop(int(delete_task) - 1)
        print(f"Задача {delete_task} удалена!")
    else:
        print("Неверный номер задачи!")


def edit_task(task_collection):
    edit_task = input("Введите номер задачи: ")
    if check_confirm(edit_task, task_collection):
        task_collection[int(edit_task) - 1] = input("Новое имя задачи: ")
    else:
        print("Неверный номер задачи!")


def add_task(task_collection):
    task_name = input("Введите имя задачи для добавления: ").strip()

    if not task_name:
        print("Название задачи не может быть пустым!")
        return

    task_details = input("Введите подробности задачи: ").strip()

    if task_details:
        task = f"Задача {len(task_collection) + 1}. {task_name} - {task_details}"
    else:
        task = f"Задача {len(task_collection) + 1}. {task_name}"

    task_collection.append(task)
    print(f"Задача успешно добавлена: {task}")