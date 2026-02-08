import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def favorites_manager():
    import json
    
    filename = "favorites.json"
    
    def load_favorites():
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                'movies': [],
                'books': [],
                'songs': [],
                'foods': [],
                'places': []
            }
    
    def save_favorites(data):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    categories = ['movies', 'books', 'songs', 'foods', 'places']
    
    print("💖 Favorites Manager 💖")
    print("=" * 40)
    
    favorites = load_favorites()
    
    while True:
        print("\n1. Add Favorite")
        print("2. View Favorites")
        print("3. Remove Favorite")
        print("4. Search Favorites")
        print("5. Statistics")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            print("\nCategories:", ', '.join(categories))
            category = input("Choose category: ").lower()
            if category in categories:
                item = input(f"Enter {category[:-1]} name: ")
                favorites[category].append(item)
                save_favorites(favorites)
                print(f"Added to {category}!")
            else:
                print("Invalid category")
        elif choice == '2':
            print("\n⭐ Your Favorites:")
            for category in categories:
                if favorites[category]:
                    print(f"\n{category.capitalize()}:")
                    for i, item in enumerate(favorites[category], 1):
                        print(f"  {i}. {item}")
        elif choice == '3':
            category = input("Enter category: ").lower()
            if category in categories:
                if favorites[category]:
                    print(f"\n{category.capitalize()}:")
                    for i, item in enumerate(favorites[category], 1):
                        print(f"{i}. {item}")
                    try:
                        num = int(input("Enter number to remove: "))
                        if 1 <= num <= len(favorites[category]):
                            removed = favorites[category].pop(num-1)
                            save_favorites(favorites)
                            print(f"Removed: {removed}")
                        else:
                            print("Invalid number")
                    except ValueError:
                        print("Please enter a number")
                else:
                    print("This category is empty")
            else:
                print("Invalid category")
        elif choice == '4':
            search = input("Search for: ").lower()
            found = False
            for category in categories:
                matches = [item for item in favorites[category] if search in item.lower()]
                if matches:
                    print(f"\nFound in {category}:")
                    for item in matches:
                        print(f"  - {item}")
                    found = True
            if not found:
                print("No matches found")
        elif choice == '5':
            total = sum(len(favorites[cat]) for cat in categories)
            print(f"\n📊 Statistics:")
            print(f"Total favorites: {total}")
            for category in categories:
                count = len(favorites[category])
                print(f"{category.capitalize():10}: {count:3} items")
        else:
            print("Invalid choice")

# 26. 📝 Class Schedule

if __name__ == "__main__":
    favorites_manager()
