import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

class GroceryList:
    def __init__(self, filename="grocery.txt"):
        self.filename = filename
        self.items = self.load_items()
    
    def load_items(self):
        try:
            with open(self.filename, 'r') as f:
                items = []
                for line in f:
                    if line.strip():
                        name, quantity, category = line.strip().split('|')
                        items.append({
                            'name': name,
                            'quantity': quantity,
                            'category': category
                        })
                return items
        except FileNotFoundError:
            return []
    
    def save_items(self):
        with open(self.filename, 'w') as f:
            for item in self.items:
                f.write(f"{item['name']}|{item['quantity']}|{item['category']}\n")
    
    def add_item(self):
        name = input("Item name: ")
        quantity = input("Quantity (e.g., 1 lb, 2 bags): ")
        category = input("Category (produce, dairy, meat, etc.): ")
        
        self.items.append({
            'name': name,
            'quantity': quantity,
            'category': category
        })
        print(f"Added {quantity} of {name}")
        self.save_items()
    
    def view_list(self, category=None):
        if not self.items:
            print("Grocery list is empty!")
            return
        
        categories = {}
        for item in self.items:
            cat = item['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(item)
        
        print("\n🛒 Grocery List:")
        for cat in sorted(categories.keys()):
            print(f"\n{cat.upper()}:")
            for item in categories[cat]:
                print(f"  - {item['quantity']} {item['name']}")
    
    def remove_item(self):
        self.view_list()
        item_name = input("Enter item name to remove: ")
        
        for i, item in enumerate(self.items):
            if item['name'].lower() == item_name.lower():
                del self.items[i]
                print(f"Removed {item_name}")
                self.save_items()
                return
        print("Item not found")
    
    def search_item(self):
        search_term = input("Search for item: ").lower()
        found = []
        
        for item in self.items:
            if search_term in item['name'].lower() or search_term in item['category'].lower():
                found.append(item)
        
        if found:
            print(f"\nFound {len(found)} items:")
            for item in found:
                print(f"- {item['quantity']} {item['name']} ({item['category']})")
        else:
            print("No items found")

def grocery_app():
    grocery = GroceryList()
    
    print("🛒 Grocery List Manager 🛒")
    print("=" * 40)
    
    while True:
        print("\n1. Add Item")
        print("2. View List")
        print("3. Remove Item")
        print("4. Search Items")
        print("5. Clear List")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            grocery.add_item()
        elif choice == '2':
            grocery.view_list()
        elif choice == '3':
            grocery.remove_item()
        elif choice == '4':
            grocery.search_item()
        elif choice == '5':
            grocery.items = []
            grocery.save_items()
            print("List cleared!")
        else:
            print("Invalid choice")

# 25. 💖 Faves List

if __name__ == "__main__":
    grocery_app()
