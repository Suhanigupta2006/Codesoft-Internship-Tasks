import os

# File to store tasks
TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as file:
        tasks = [line.strip() for line in file.readlines()]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Display the menu
def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed (Remove)")
    print("4. Delete Task")
    print("5. Exit")

# Main program
def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            print("\n--- Your Tasks ---")
            if not tasks:
                print("No tasks available.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")

        elif choice == '2':
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("Task added successfully!")
            else:
                print("Task cannot be empty.")

        elif choice == '3':
            if not tasks:
                print("No tasks to mark as completed.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
                try:
                    task_num = int(input("Enter task number to mark as completed: "))
                    if 1 <= task_num <= len(tasks):
                        completed_task = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"Completed and removed: {completed_task}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '4':
            if not tasks:
                print("No tasks to delete.")
            else:
                for idx, task in enumerate(tasks, 1):
                    print(f"{idx}. {task}")
                try:
                    task_num = int(input("Enter task number to delete: "))
                    if 1 <= task_num <= len(tasks):
                        deleted_task = tasks.pop(task_num - 1)
                        save_tasks(tasks)
                        print(f"Deleted: {deleted_task}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == '5':
            print("Exiting To-Do List. Have a productive day!")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()