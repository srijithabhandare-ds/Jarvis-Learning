print("welcome to the Todo App")

print("===== Todo List =====")
print("1. Add a task")
print("2. View tasks")  
print("3. Mark a task as completed")
print("4. Delete a task")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

elif choice == "2":
    print("Your tasks:")
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task.strip()}")

elif choice == "3":
    task_number = int(input("Enter the task number to mark as completed: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1] = tasks[task_number - 1].strip() + " (Completed)\n"
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

elif choice == "4":
    task_number = int(input("Enter the task number to delete: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 1 <= task_number <= len(tasks):
        del tasks[task_number - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

else:
    print("Invalid Choice")
    