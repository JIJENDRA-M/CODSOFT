TASK_FILE = "tasks.txt"
def load_tasks():
    tasks = []
    try:
        f = open(TASK_FILE, "r")
        lines = f.readlines()
        for line in lines:
            task, status = line.strip().rsplit(" | ", 1)
            tasks.append({"task": task, "status": status})
        f.close()
    except:
        tasks = []
    return tasks
def save_tasks(tasks):
    f = open(TASK_FILE, "w")
    for t in tasks:
        f.write(t["task"] + " | " + t["status"] + "\n")
    f.close()
def show_tasks(tasks):
    if len(tasks) == 0:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i in range(len(tasks)):
            print(str(i + 1) + ". " + tasks[i]["task"] + " [" + tasks[i]["status"] + "]")
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({"task": task, "status": "Pending"})
    print("Task added!")
def update_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to update: ")) - 1
    if 0 <= index < len(tasks):
        new_text = input("Enter updated task: ")
        tasks[index]["task"] = new_text
        print("Task updated.")
    else:
        print("Invalid task number.")
def delete_task(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print("Deleted:", removed["task"])
    else:
        print("Invalid task number.")
def mark_complete(tasks):
    show_tasks(tasks)
    index = int(input("Enter task number to mark as complete: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["status"] = "Done"
        print("Task marked as complete.")
    else:
        print("Invalid task number.")
tasks = load_tasks()
while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark as Complete")
    print("6. Exit")
    choice = input("Choose an option (1-6): ")
    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        update_task(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        mark_complete(tasks)
    elif choice == "6":
        save_tasks(tasks)
        print("Tasks saved. Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
