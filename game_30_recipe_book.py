import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

class RecipeBook:
    def __init__(self, filename="recipes.json"):
        import json
        self.filename = filename
        self.recipes = self.load_recipes()
    
    def load_recipes(self):
        import json
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_recipes(self):
        import json
        with open(self.filename, 'w') as f:
            json.dump(self.recipes, f, indent=2)
    
    def add_recipe(self):
        name = input("Recipe name: ")
        ingredients = []
        print("\nEnter ingredients (one per line, blank line to finish):")
        while True:
            ingredient = input()
            if not ingredient:
                break
            ingredients.append(ingredient)
        
        instructions = []
        print("\nEnter instructions (one step per line, blank line to finish):")
        while True:
            step = input()
            if not step:
                break
            instructions.append(step)
        
        prep_time = input("Prep time: ")
        cook_time = input("Cook time: ")
        
        self.recipes[name] = {
            'ingredients': ingredients,
            'instructions': instructions,
            'prep_time': prep_time,
            'cook_time': cook_time
        }
        print(f"Added recipe: {name}")
        self.save_recipes()
    
    def view_recipe(self):
        name = input("Recipe name: ")
        
        if name in self.recipes:
            recipe = self.recipes[name]
            print(f"\n🍲 {name}")
            print("=" * 40)
            print(f"Prep: {recipe['prep_time']} | Cook: {recipe['cook_time']}")
            
            print("\n📝 Ingredients:")
            for ingredient in recipe['ingredients']:
                print(f"- {ingredient}")
            
            print("\n👩‍🍳 Instructions:")
            for i, step in enumerate(recipe['instructions'], 1):
                print(f"{i}. {step}")
        else:
            print("Recipe not found")
    
    def search_recipes(self):
        search = input("Search for recipe or ingredient: ").lower()
        found = False
        
        for name, recipe in self.recipes.items():
            if search in name.lower():
                print(f"\n{name}")
                found = True
            else:
                for ingredient in recipe['ingredients']:
                    if search in ingredient.lower():
                        print(f"\n{name}")
                        found = True
                        break
        
        if not found:
            print("No recipes found")

def recipe_app():
    recipes = RecipeBook()
    
    print("🍲 Recipe Book 🍲")
    print("=" * 40)
    
    while True:
        print("\n1. Add Recipe")
        print("2. View Recipe")
        print("3. Search Recipes")
        print("4. List All Recipes")
        print("5. Random Recipe")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            recipes.add_recipe()
        elif choice == '2':
            recipes.view_recipe()
        elif choice == '3':
            recipes.search_recipes()
        elif choice == '4':
            if recipes.recipes:
                print("\n📖 All Recipes:")
                for name in sorted(recipes.recipes.keys()):
                    print(f"- {name}")
            else:
                print("No recipes")
        elif choice == '5':
            import random
            if recipes.recipes:
                name = random.choice(list(recipes.recipes.keys()))
                print(f"\nRandom recipe: {name}")
                view = input("View it? (y/n): ").lower()
                if view == 'y':
                    recipes.view_recipe(name)
            else:
                print("No recipes")
        else:
            print("Invalid choice")

# 31. 🔎 Pokédex

if __name__ == "__main__":
    recipe_app()
