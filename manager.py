def add_task(tasks, task_name):
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' has been added successfully!")

def view_tasks(tasks):
    print("\nTask List:")
    if not tasks:
        print("The list is empty.")
    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        task_name = task["name"]
        print(f"{index}. [{status}] {task_name}")

def update_task_name(tasks, task_index, new_task_name):
    try:
        adjusted_index = int(task_index) - 1
        if 0 <= adjusted_index < len(tasks):
            tasks[adjusted_index]["name"] = new_task_name
            print(f"Task {task_index} updated to: {new_task_name}")
        else:
            print("Error: Invalid task index. Task not found.")
    except ValueError:
        print("Error: Please enter a valid number for the task index.")

def complete_task(tasks, task_index):
    try:
        adjusted_index = int(task_index) - 1
        if 0 <= adjusted_index < len(tasks):
            tasks[adjusted_index]["completed"] = True
            print(f"Task {task_index} marked as completed.")
        else:
            print("Error: Invalid task index. Task not found.")
    except ValueError:
        print("Error: Please enter a valid number for the task index.")

def delete_completed_tasks(tasks):
    # Overwrites the list with only the incomplete tasks
    tasks[:] = [task for task in tasks if not task["completed"]]
    print("Completed tasks have been deleted.")

tasks = []

while True:
    print("\nTask List Manager Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Update task")
    print("4. Complete task")
    print("5. Delete completed tasks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter the task name you want to add: ")
        add_task(tasks, task_name)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        view_tasks(tasks)
        task_index = input("Enter the task number you want to update: ")
        new_name = input("Enter the new task name: ")
        update_task_name(tasks, task_index, new_name)

    elif choice == "4":
        view_tasks(tasks)
        task_index = input("Enter the task number you want to complete: ")
        complete_task(tasks, task_index)

    elif choice == "5":
        delete_completed_tasks(tasks)
        view_tasks(tasks)

    elif choice == "6":
        print("Closing the program...")
        break
    
    else:
        print("Invalid option. Please choose a number between 1 and 6.")

print("Program finished.")