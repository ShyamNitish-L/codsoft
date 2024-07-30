Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("\nTasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "✔️ Completed" if task["completed"] else "❌ Incomplete"
                print(f"{index}. {task['task']} - {status}")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            if self.tasks[index]["completed"]:
                print("This task is already marked as completed.")
            else:
                self.tasks[index]["completed"] = True
                print(f'Task "{self.tasks[index]["task"]}" marked as completed.')
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f'Task "{removed_task["task"]}" deleted successfully.')
        else:
            print("Invalid task number.")


def main():
...     todo_list = ToDoList()
... 
...     while True:
...         print("\nTo-Do List Menu:")
...         print("1. Add a task")
...         print("2. View tasks")
...         print("3. Mark a task as complete")
...         print("4. Delete a task")
...         print("5. Exit")
... 
...         choice = input("Enter your choice (1-5): ")
... 
...         if choice == "1":
...             task = input("Enter a new task: ")
...             todo_list.add_task(task)
...         elif choice == "2":
...             todo_list.view_tasks()
...         elif choice == "3":
...             todo_list.view_tasks()
...             try:
...                 index = int(input("Enter the task number to mark as complete: ")) - 1
...                 todo_list.mark_task_complete(index)
...             except ValueError:
...                 print("Please enter a valid number.")
...         elif choice == "4":
...             todo_list.view_tasks()
...             try:
...                 index = int(input("Enter the task number to delete: ")) - 1
...                 todo_list.delete_task(index)
...             except ValueError:
...                 print("Please enter a valid number.")
...         elif choice == "5":
...             print("Exiting the program...")
...             break
...         else:
...             print("Invalid choice. Please try again.")
... 
... if __name__ == "__main__":
