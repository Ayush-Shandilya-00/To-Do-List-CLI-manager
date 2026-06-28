# ╔══════════════════════════════════════╗
# ║     PROJECT: TO-DO LIST MANAGER      ║
# ╚══════════════════════════════════════╝

import json
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "main.json")


def load_tasks():
    if not os.path.exists(FILE_PATH):
        return []

    with open(FILE_PATH, "r", encoding="utf-8") as file:
        data = json.load(file)

    if isinstance(data, dict) and "tasks" in data and isinstance(data["tasks"], list):
        return data["tasks"]

    return []


def save_tasks(tasks):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump({"tasks": tasks}, file, indent=2)
        file.write("\n")


def add_task(serial_no=None, task_text=None):
    if serial_no is None:
        serial_no = input("Enter the Serial no. of the Task: ").strip()
    if task_text is None:
        task_text = input("Enter the Task: ").strip()

    if not serial_no or not task_text:
        print("Both serial number and task are required.")
        return

    tasks = load_tasks()
    tasks.append({"serial": serial_no, "task": task_text})
    save_tasks(tasks)
    print("Task added to main.json successfully.")


def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("Stored Tasks:")
    for item in tasks:
        print(f"{item['serial']}: {item['task']}")


def menu():
    print("─────────|Welcome to the Task Manager|─────────")
    print("")
    print("                  ❀ MENU ❀")
    print("───────────────────────────────────────────────")
    print("1> Add Task")
    print("2> View All Tasks")
    print("3❯ Update Task")
    print("4❯ Delete Task")
    print("5❯ Exit")


def main():
    while True:
        menu()
        choice = input("Enter Choice from menu: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Update feature is not available yet.")
        elif choice == "4":
            print("Delete feature is not available yet.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == "__main__":
    main()


