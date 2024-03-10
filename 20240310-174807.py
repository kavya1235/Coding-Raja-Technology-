def print_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")

def add_task(tasks, task):
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def mark_task_done(tasks, task_number):
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
    else:
        tasks[task_number - 1] += " (DONE)"
        print("Task marked as done.")

def remove_task(tasks, task_number):
    if task_number < 1 or task_number > len(tasks):
        print("Invalid task number.")
    else:
        del tasks[task_number - 1]
        print("Task removed.")

def main():
    tasks = []
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            task_number = int(input("Enter task number to mark as done: "))
            mark_task_done(tasks, task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to remove: "))
            remove_task(tasks, task_number)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()