import json
import os
from datetime import datetime

TASK_FILE = "tasks.json"

# Load tasks from file
if os.path.exists(TASK_FILE):
    with open(TASK_FILE, "r") as f:
        tasks = json.load(f)
else:
    tasks = []

def save_tasks():
    """Save tasks to the JSON file."""
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    """Add a new task with name, priority, and optional due date."""
    name = input("Enter task name: ").strip()
    if not name:
        print("❌ Task cannot be empty.")
        return

    # Validate priority
    while True:
        priority = input("Enter priority (High/Medium/Low): ").strip().capitalize()
        if priority in ["High", "Medium", "Low"]:
            break
        print("❌ Invalid priority. Choose High, Medium, or Low.")

    # Validate due date
    due = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
    if due:
        try:
            datetime.strptime(due, "%Y-%m-%d")
        except ValueError:
            print("❌ Invalid date format. Skipping due date.")
            due = ""

    tasks.append({"name": name, "done": False, "priority": priority, "due": due})
    save_tasks()
    print(f"✅ Task '{name}' added with priority {priority}.")

def view_tasks():
    """Display all tasks with status, priority, and due date."""
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour Tasks:")
    for i, t in enumerate(tasks, 1):
        status = "✔️" if t.get("done") else "❌"
        due = t.get("due", "No due date")
        priority = t.get("priority", "Medium")
        print(f"{i}. {t.get('name', 'Unnamed Task')} [{status}] Priority: {priority} Due: {due}")
    print("")

def mark_as_done():
    """Mark a specific task as completed."""
    if not tasks:
        print("No tasks yet!")
        return
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks()
            print(f"✅ Task '{tasks[index]['name']}' marked as done!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def remove_task():
    """Remove a task by its number."""
    if not tasks:
        print("No tasks to remove!")
        return
    view_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            save_tasks()
            print(f"🗑️ Task '{removed_task['name']}' removed successfully!")
        else:
            print("❌ Invalid task number.")
    except ValueError:
        print("❌ Please enter a valid number.")

def close():
    """Exit the program."""
    print("👋 Goodbye!")
    exit()

menu = """
📝 Task Manager
1 - Add Task
2 - View Tasks
3 - Mark Task as Done
4 - Remove Task
5 - Close
"""

# Main loop
while True:
    print(menu)
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_as_done()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        close()
    else:
        print("❌ Invalid choice. Enter a number between 1 and 5.\n")
