"""
Develop a command-line application that allows users to
add, list, and remove tasks from a todo list.
The tasks should be saved to a file so that they persist between runs.
"""

import sys, os, json

def print_help():
    print("Usage:")
    print("  python exercise3_todo_list.py add 'Task description'")
    print("  python exercise3_todo_list.py list")
    print("  python exercise3_todo_list.py remove TASK_NUMBER")
    print("  python exercise3_todo_list.py help")

class TodoList:
    def __init__(self, filename="data/todo_list.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        else:
            return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task_description):
        self.tasks.append(task_description)
        self.save_tasks()

    def get_tasks(self):
        return self.tasks

    def remove_task(self, task_number):
        if 0 <= task_number < len(self.tasks):
            self.tasks.pop(task_number)
            self.save_tasks()

# Example usage
if __name__ == "__main__":
    print("Todo List Application")

    todo_list = TodoList()
    if len(sys.argv) < 2 or sys.argv[1] == 'help':
        print_help()
    elif sys.argv[1] == 'add':
        if len(sys.argv) < 3:
            print("Error: Task description required.")
        else:
            task = ' '.join(sys.argv[2:])
            todo_list.add_task(task)
            print(f"Added task: {task}")
    elif sys.argv[1] == 'list':
        tasks = todo_list.get_tasks()
        if tasks:
            print("Todo List:")
            for idx, task in enumerate(tasks):
                print(f"{idx}. {task}")
        else:
            print("Your todo list is empty.")
    elif sys.argv[1] == 'remove':
        if len(sys.argv) < 3:
            print("Error: Task number required.")
        else:
            try:
                task_number = int(sys.argv[2])
                todo_list.remove_task(task_number)
                print(f"Removed task number {task_number}.")
            except ValueError:
                print("Error: Task number must be an integer.")
    else:
        print("Unknown command.")
        print_help()

    print("Example usage:")
    todo_list.add_task("Buy groceries")
    todo_list.add_task("Clean house")
    print(todo_list.get_tasks())
