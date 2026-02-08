import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

class ContactBook:
    def __init__(self, filename="contacts.json"):
        import json
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        import json
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    
    def save_contacts(self):
        import json
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=2)
    
    def add_contact(self):
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        address = input("Address: ")
        
        self.contacts[name] = {
            'phone': phone,
            'email': email,
            'address': address
        }
        print(f"Added contact: {name}")
        self.save_contacts()
    
    def search_contact(self):
        search = input("Search by name: ").lower()
        found = False
        
        for name, info in self.contacts.items():
            if search in name.lower():
                print(f"\n{name}:")
                print(f"  Phone: {info['phone']}")
                print(f"  Email: {info['email']}")
                print(f"  Address: {info['address']}")
                found = True
        
        if not found:
            print("No contacts found")
    
    def list_contacts(self):
        if not self.contacts:
            print("No contacts")
            return
        
        print(f"\n📇 Contacts ({len(self.contacts)}):")
        for name in sorted(self.contacts.keys()):
            print(f"- {name} ({self.contacts[name]['phone']})")
    
    def delete_contact(self):
        name = input("Enter name to delete: ")
        
        if name in self.contacts:
            del self.contacts[name]
            self.save_contacts()
            print(f"Deleted: {name}")
        else:
            print("Contact not found")

def contact_app():
    contacts = ContactBook()
    
    print("📇 Contact Book 📇")
    print("=" * 40)
    
    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. List All Contacts")
        print("4. Delete Contact")
        print("5. Export Contacts")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            contacts.add_contact()
        elif choice == '2':
            contacts.search_contact()
        elif choice == '3':
            contacts.list_contacts()
        elif choice == '4':
            contacts.delete_contact()
        elif choice == '5':
            import json
            print("\nExporting contacts...")
            with open('contacts_export.json', 'w') as f:
                json.dump(contacts.contacts, f, indent=2)
            print("Contacts exported to contacts_export.json")
        else:
            print("Invalid choice")

# 30. 🍲 Recipe Book

if __name__ == "__main__":
    contact_app()
