def store():
    n = int(input('Enter number of tasks: '))
    tasks = []
    with open('database.txt', 'w') as f:
        for _ in range(n):
            task = input('Enter task: ')
            tasks.append(task)
            f.write(task + '\n')
            print('Task saved successfully.')
    return tasks

def readfile():
    try:
        with open('database.txt', 'r') as f:
            stored_info = f.read()
            if stored_info.strip() == '':
                print('Empty list')
            else:
                print('Tasks:')
                print(stored_info)
    except FileNotFoundError:
        print('No database')

def modify():
    try:
        with open('database.txt', 'r') as f:
            tasks = f.readlines()

        print('Tasks:')
        for i, task in enumerate(tasks, start=1):
            print(f"{i}: {task.strip()}")

        choice_to_modify = int(input('Enter the task number to modify (0 to cancel): '))
        if 0 < choice_to_modify <= len(tasks):
            new_task = input('Enter the new task: ')
            tasks[choice_to_modify - 1] = new_task + '\n'

            with open('database.txt', 'w') as f:
                f.writelines(tasks)
            print("Task modified successfully.")
        elif choice_to_modify == 0:
            print("Operation canceled.")
        else:
            print("Invalid task number. No task modified.")
    except FileNotFoundError:
        print("No database found.")

def delete():
    try:
        with open('database.txt', 'r') as f:
            tasks = f.readlines()

        if not tasks:
            print("Empty list")
            return

        print('Tasks:')
        for i, task in enumerate(tasks, start=1):
            print(f"{i}: {task.strip()}")

        choice_to_delete = int(input('Enter the task number to delete (0 to cancel): '))
        if 0 < choice_to_delete <= len(tasks):
            del tasks[choice_to_delete - 1]

            with open('database.txt', 'w') as f:
                f.writelines(tasks)
            print("Task deleted successfully.")
        elif choice_to_delete == 0:
            print("Operation canceled.")
        else:
            print("Invalid task number. No task deleted.")
    except FileNotFoundError:
        print("No database found.")

if __name__ == '__main__':
    while True:
        choice = int(input('Enter 1 to input in todo list \n2 to read the todo list \n3 Modify list \n4 to delete \n5 to exit: '))
        if choice == 1:
            store()
        elif choice == 2:
            readfile()
        elif choice == 3:
            modify()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
