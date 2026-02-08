import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = filename
        self.expenses = self.load_expenses()
    
    def load_expenses(self):
        try:
            import csv
            expenses = []
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    row['amount'] = float(row['amount'])
                    expenses.append(row)
            return expenses
        except FileNotFoundError:
            return []
    
    def save_expenses(self):
        import csv
        with open(self.filename, 'w', newline='') as f:
            fieldnames = ['date', 'category', 'description', 'amount']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.expenses)
    
    def add_expense(self):
        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        category = input("Category (food, transport, entertainment, etc.): ")
        description = input("Description: ")
        try:
            amount = float(input("Amount: $"))
            self.expenses.append({
                'date': date,
                'category': category,
                'description': description,
                'amount': amount
            })
            self.save_expenses()
            print("Expense added!")
        except ValueError:
            print("Invalid amount")
    
    def view_expenses(self, period='all'):
        if not self.expenses:
            print("No expenses recorded!")
            return
        
        import datetime
        today = datetime.datetime.now()
        
        filtered = []
        for exp in self.expenses:
            exp_date = datetime.datetime.strptime(exp['date'], '%Y-%m-%d')
            if period == 'today' and exp_date.date() != today.date():
                continue
            elif period == 'week' and (today - exp_date).days > 7:
                continue
            elif period == 'month' and (today - exp_date).days > 30:
                continue
            filtered.append(exp)
        
        if not filtered:
            print(f"No expenses for {period}")
            return
        
        total = sum(exp['amount'] for exp in filtered)
        print(f"\n📊 Expenses ({period}):")
        print(f"Total: ${total:.2f}")
        print("\nDetails:")
        for exp in filtered:
            print(f"{exp['date']} - {exp['category']}: {exp['description']} - ${exp['amount']:.2f}")
    
    def category_summary(self):
        if not self.expenses:
            print("No expenses!")
            return
        
        categories = {}
        for exp in self.expenses:
            cat = exp['category']
            categories[cat] = categories.get(cat, 0) + exp['amount']
        
        total = sum(categories.values())
        print("\n📈 Category Summary:")
        for cat, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total) * 100
            print(f"{cat:15}: ${amount:8.2f} ({percentage:5.1f}%)")
        print(f"{'Total':15}: ${total:8.2f}")

def expense_tracker_app():
    tracker = ExpenseTracker()
    
    print("💸 Expense Tracker 💸")
    print("=" * 40)
    
    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. View Today's Expenses")
        print("4. View This Week's Expenses")
        print("5. View This Month's Expenses")
        print("6. Category Summary")
        print("7. Clear All Expenses")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses('all')
        elif choice == '3':
            tracker.view_expenses('today')
        elif choice == '4':
            tracker.view_expenses('week')
        elif choice == '5':
            tracker.view_expenses('month')
        elif choice == '6':
            tracker.category_summary()
        elif choice == '7':
            tracker.expenses = []
            tracker.save_expenses()
            print("All expenses cleared!")
        else:
            print("Invalid choice")

# 28. 📚 Library Management System

if __name__ == "__main__":
    expense_tracker_app()
