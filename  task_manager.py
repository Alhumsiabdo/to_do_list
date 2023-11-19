def main():
    message = """
1- add task to a list
2- mark task as complete
3- view tasks
4- Quit
    """

    tasks = []

    while True:
        print(message)
        choice = input("Enter your choice: ")

        if choice == "1":
            # add task to tasks list
            add_task(tasks)
        elif choice == "2":
            mark_task_complete(tasks)

        elif choice == "3":
            view_tasks(tasks)

        elif choice == "4":
            break

        # message when user
        else:
            print("Invalid choice, please enter a number between 1 and 4")


def add_task(tasks):
    # get task from user
    task = input("Enter task: ")
    # define task status
    task_info = {"task": task, "completed": False}
    # add task to the list of tasks
    tasks.append(task_info)
    # message show to user added successfully!
    print("Task added to list successfully!")


def mark_task_complete(tasks):
    # Get list of incomplete tasks
    incomplete_tasks = [task for task in tasks if not task["completed"]]

    # Show them to the user
    if not incomplete_tasks:
        print("No incomplete tasks to mark as complete.")
        return

    print("Incomplete tasks:")
    for i, task in enumerate(incomplete_tasks, start=1):
        print(f"{i}- {task['task']}")
        print("-" * 30)

    # Get the task from the user
    while True:
        try:
            task_number = int(input("Choose the task to complete (enter the number): "))
            if 1 <= task_number <= len(incomplete_tasks):
                break
            else:
                print("Invalid input. Please enter a valid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Mark the task as completed
    incomplete_tasks[task_number - 1]["completed"] = True

    # Message shown to the user after marking completed successfully
    print(f"Task {task_number} is marked as completed successfully!")


def view_tasks(tasks):
    # Check if there are no tasks
    if not tasks:
        print("There are no tasks.")
    else:
        print("Tasks:")
        # Enumerate through tasks and display details
        for i, task in enumerate(tasks, start=1):
            status = "✅" if task["completed"] else "❌"
            print(f"{i}. {task['task']} : {status}")
            print("-" * 30)

main()