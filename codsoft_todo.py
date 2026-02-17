import os

FILE_NAME = "tasks.txt"

# ---------------- FILE FUNCTIONS ---------------- #

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")

# ---------------- MAIN PROGRAM ---------------- #

def show_menu():
    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    print("================================")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter new task: ").strip()
            if task:
                tasks.append(task)
                save_tasks(tasks)
                print("✅ Task added successfully!")
            else:
                print("⚠ Task cannot be empty!")

        elif choice == "2":
            if not tasks:
                print("📌 No tasks available.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "3":
            if not tasks:
                print("⚠ No tasks to delete.")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_tasks(tasks)
                        print(f"❌ Task '{removed}' deleted successfully!")
                    else:
                        print("⚠ Invalid task number.")
                except ValueError:
                    print("⚠ Please enter a valid number.")

        elif choice == "4":
            print("👋 Exiting To-Do List. Thank you!")
            break

        else:
            print("⚠ Invalid choice. Please select between 1-4.")

if __name__ == "__main__":
    main()