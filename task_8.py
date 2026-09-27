task_manager = []

def add():
    new_task = input("Task name: ")
    task_manager.append(new_task)
    print("Task added successfully")

def show():
    print("current tasks")

    if len(task_manager) == 0:
        print("No tasks available")
    else:
        index = 0
        while index < len(task_manager):
            print(index + 1, ".", task_manager[index])
            index += 1

def modify():
    show()

    if len(task_manager) > 0:
        number = int(input("Enter task number to update: "))

        if number >= 1 and number <= len(task_manager):
            updated_task = input("Enter new task: ")
            task_manager[number - 1] = updated_task
            print("Task updated successfully")
        else:
            print("Invalid task number")

def remove():
    show()

    if len(task_manager) > 0:
        number = int(input("Enter task number to delete: "))

        if number >= 1 and number <= len(task_manager):
            task_manager.pop(number - 1)
            print("Task deleted successfully")
        else:
            print("Invalid task number")

def start():
    while True:
        print("Tasks")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add()

        elif choice == "2":
            show()

        elif choice == "3":
            modify()

        elif choice == "4":
            remove()

        elif choice == "5":
            print("Program closed")
            break

        else:
            print("Invalid option")

start()
