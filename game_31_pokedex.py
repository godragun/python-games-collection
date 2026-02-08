import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def pokedex():
    import json
    
    # Sample Pokémon data
    pokemon_data = {
        'pikachu': {
            'number': 25,
            'type': ['Electric'],
            'description': 'When several of these Pokémon gather, their electricity could build and cause lightning storms.',
            'height': '0.4 m',
            'weight': '6.0 kg',
            'abilities': ['Static', 'Lightning Rod']
        },
        'charizard': {
            'number': 6,
            'type': ['Fire', 'Flying'],
            'description': 'Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally.',
            'height': '1.7 m',
            'weight': '90.5 kg',
            'abilities': ['Blaze', 'Solar Power']
        },
        'bulbasaur': {
            'number': 1,
            'type': ['Grass', 'Poison'],
            'description': 'A strange seed was planted on its back at birth. The plant sprouts and grows with this Pokémon.',
            'height': '0.7 m',
            'weight': '6.9 kg',
            'abilities': ['Overgrow', 'Chlorophyll']
        },
        'squirtle': {
            'number': 7,
            'type': ['Water'],
            'description': 'After birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.',
            'height': '0.5 m',
            'weight': '9.0 kg',
            'abilities': ['Torrent', 'Rain Dish']
        }
    }
    
    print("🔎 Pokédex 🔎")
    print("=" * 40)
    
    while True:
        print("\n1. Search Pokémon")
        print("2. List All Pokémon")
        print("3. Pokémon by Type")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            name = input("Enter Pokémon name: ").lower()
            if name in pokemon_data:
                data = pokemon_data[name]
                print(f"\n#{data['number']:03} {name.capitalize()}")
                print(f"Type: {'/'.join(data['type'])}")
                print(f"Description: {data['description']}")
                print(f"Height: {data['height']}")
                print(f"Weight: {data['weight']}")
                print(f"Abilities: {', '.join(data['abilities'])}")
            else:
                print("Pokémon not found in Pokédex")
        elif choice == '2':
            print("\n📖 Pokédex Entries:")
            for name in sorted(pokemon_data.keys()):
                data = pokemon_data[name]
                print(f"#{data['number']:03} {name.capitalize():12} {'/'.join(data['type']):15}")
        elif choice == '3':
            types = set()
            for data in pokemon_data.values():
                types.update(data['type'])
            
            print(f"\nAvailable types: {', '.join(sorted(types))}")
            type_name = input("Enter type: ").capitalize()
            
            print(f"\n{type_name} type Pokémon:")
            found = False
            for name, data in pokemon_data.items():
                if type_name in data['type']:
                    print(f"#{data['number']:03} {name.capitalize()}")
                    found = True
            
            if not found:
                print("No Pokémon of this type")
        else:
            print("Invalid choice")

# ==================== LEVEL 3 PROJECTS ====================

# Due to space constraints, I'll show a few complete Level 3 games and outline the others

# 32. 🪦 Hangman

if __name__ == "__main__":
    pokedex()
