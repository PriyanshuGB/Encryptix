# todo.py

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def update_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description

def display_menu():
    print("\nTo-Do List Application")
    print("1. Add task")
    print("2. Remove task")
    print("3. Mark task complete")
    print("4. List tasks")
    print("5. Update task")
    print("6. Exit")

def main():
    todo_list = ToDoList()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter the task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter the task number to remove: ")) - 1
            todo_list.remove_task(index)
        elif choice == '3':
            index = int(input("Enter the task number to mark complete: ")) - 1
            todo_list.mark_task_complete(index)
        elif choice == '4':
            print("\nCurrent To-Do List:")
            todo_list.list_tasks()
        elif choice == '5':
            index = int(input("Enter the task number to update: ")) - 1
            new_description = input("Enter the new description: ")
            todo_list.update_task(index, new_description)
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
