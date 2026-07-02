from colorama import Fore, Style, init
init(autoreset=True)

tasks = []

try:
    with open("tasks.txt", "r") as file:
        tasks = [line.strip() for line in file]
except FileNotFoundError:
    tasks = []

def view_tasks():
    if len(tasks) == 0:
        print("\nNo tasks available!")

    else:

        print("\nYour tasks: ")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")    

def display_menu():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + "              📋 TO-DO LIST MANAGER")
    print(Fore.CYAN + "=" * 50)

    print(Fore.YELLOW + "\n[1] Add Task")
    print(Fore.YELLOW + "[2] View Tasks")
    print(Fore.YELLOW + "[3] Mark Task as Completed")
    print(Fore.YELLOW + "[4] Delete Task")
    print(Fore.YELLOW + "[5] Exit")

    print("=" * 50)

while True:
    display_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        task = input("\nEnter a new task: ")

        tasks.append(task)

        print("\n✅ Task aded successfully!")

    elif choice == "2":
        print("\n" + "-" * 40)
        print("               YOUR TASKS")
        print("-" * 40)
        view_tasks()

    elif choice == "3":
        
        if len(tasks) == 0:
            print("\nNo tasks available.")

        else:
            view_tasks()

            task_number = int(input("\nEnter the number to mark as completed: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1] = "✅ " + tasks[task_number - 1]

                print("\nTask marked as completed!")

            else:
                print("\nInvalid task number:")

    elif choice == "4":
        
        if len(tasks) == 0:
            print("\nNo tasks available!")

        else:
            view_tasks()

        task_number = int(input("\nEnter task number to delete: "))
        
        if 1 <= task_number <= len(tasks):

            deleted_task = tasks.pop(task_number - 1)

            print(f"\nDeleted task: {deleted_task}")

        else:
            print("\nInvalid task number.")

    elif choice == "5":
        
        with open("tasks.txt", "w") as file:

            for task in tasks:
                file.write(task + "\n")
                           
        
        print("\nTasks saved successfully!")
        print("Thankyou for using the To-DO App!")
        break

    else:
        print("\nInvalid choice. Please try again.")

    input("\nPress Enter to continue...")
    print()