tasks = ["task 1", "task 2", "task 3"]
choice = 0
task_choice = ""
run_ = True

print("Welcome to Python Task Manager")
while run_:
    print ("Select managing option: \n" \
    "1. View tasks \n" \
    "2. Add task \n" \
    "3. Rename task \n" \
    "4. Remove task \n" \
    "5. Exit")
    choice = int(input())
    match choice:
        case 1:
            print(tasks)
        case 2:
            tasks.append(input("enter task's name: "))
        case 3:
            if (len(tasks) > 0):
                print(tasks, f"\n select task number (1-{len(tasks)}):")
                task_choice = int(input())
                tasks[task_choice - 1] = input("select new name: ")
                task_choice = 0
            else:
                print("no tasks found!")
        case 4:
            if (len(tasks) > 0):
                print(tasks, f"\n select task number (1-{len(tasks)}):")
                task_choice = int(input())
                tasks.pop(task_choice - 1)
                task_choice = 0
            else:
                print("no tasks found!")
        case 5:
            run_ = False
print("Goodbye")
