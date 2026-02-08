import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

class TodoList:
    def __init__(self, filename="todo.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                tasks = []
                for line in f:
                    if line.strip():
                        completed, description = line.strip().split('|', 1)
                        tasks.append({
                            'completed': completed == 'True',
                            'description': description
                        })
                return tasks
        except FileNotFoundError:
            return []
    
    def save_tasks(self):
        with open(self.filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task['completed']}|{task['description']}\n")
    
    def add_task(self):
        description = input("Enter task description: ")
        self.tasks.append({
            'completed': False,
            'description': description
        })
        print("Task added!")
        self.save_tasks()
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks!")
            return
        
        print("\n📋 To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            status = '✓' if task['completed'] else '○'
            print(f"{i}. [{status}] {task['description']}")
    
    def complete_task(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to mark complete: "))
            if 1 <= task_num <= len(self.tasks):
                self.tasks[task_num-1]['completed'] = True
                print("Task marked complete!")
                self.save_tasks()
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a number")
    
    def delete_task(self):
        self.view_tasks()
        try:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(self.tasks):
                del self.tasks[task_num-1]
                print("Task deleted!")
                self.save_tasks()
            else:
                print("Invalid task number")
        except ValueError:
            print("Please enter a number")

def todo_app():
    todo = TodoList()
    
    print("📋 To-Do List Manager 📋")
    print("=" * 40)
    
    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Show Statistics")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            todo.add_task()
        elif choice == '2':
            todo.view_tasks()
        elif choice == '3':
            todo.complete_task()
        elif choice == '4':
            todo.delete_task()
        elif choice == '5':
            if todo.tasks:
                completed = sum(1 for task in todo.tasks if task['completed'])
                total = len(todo.tasks)
                print(f"\n📊 Statistics:")
                print(f"Total tasks: {total}")
                print(f"Completed: {completed}")
                print(f"Remaining: {total - completed}")
                if total > 0:
                    print(f"Completion: {(completed/total)*100:.1f}%")
            else:
                print("No tasks!")
        else:
            print("Invalid choice")

# 24. 🛒 Grocery

if __name__ == "__main__":
    todo_app()
