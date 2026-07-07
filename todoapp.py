def display_menu():
    print("\nTo-Do List Application")
    print("1. View task")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def view_task(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\n Your To-Do List: ")
        for i,task in enumerate(tasks,start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task=input("Enter the task you want to add : ")
    tasks.append(task)
    print("Task added successfully.")

def remove_task(tasks):
    if not tasks:
        print("Your to-do list is empty.")
        return
    view_task(tasks)
    try:
        task_number=int(input("Enter the task number to delete : "))
        if 1<= task_number <= len(tasks):
            removed_task= tasks.pop(task_number -1)
            print(f"Task '{removed_task}' deleted successfully.")
        else:
            print("invalid task number , tyr again later.")
    except ValueError:
        print("Invalid input , please enter a valid task number.")

def to_do_list_app():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4) : " )
        if choice == '1':
            view_task(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the application , Goodbye...")
            break
        else:
            print("Invalid choice , please try again later.")

to_do_list_app()
           