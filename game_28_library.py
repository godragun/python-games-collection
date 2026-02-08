import sys
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

class Library:
    def __init__(self, filename="library.txt"):
        self.filename = filename
        self.books = self.load_books()
    
    def load_books(self):
        try:
            books = []
            with open(self.filename, 'r') as f:
                for line in f:
                    if line.strip():
                        title, author, isbn, available = line.strip().split('|')
                        books.append({
                            'title': title,
                            'author': author,
                            'isbn': isbn,
                            'available': available == 'True'
                        })
            return books
        except FileNotFoundError:
            # Sample books
            return [
                {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'isbn': '123', 'available': True},
                {'title': '1984', 'author': 'George Orwell', 'isbn': '456', 'available': True},
                {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'isbn': '789', 'available': False}
            ]
    
    def save_books(self):
        with open(self.filename, 'w') as f:
            for book in self.books:
                f.write(f"{book['title']}|{book['author']}|{book['isbn']}|{book['available']}\n")
    
    def add_book(self):
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        
        self.books.append({
            'title': title,
            'author': author,
            'isbn': isbn,
            'available': True
        })
        print(f"Added: {title}")
        self.save_books()
    
    def search_books(self):
        print("\nSearch by:")
        print("1. Title")
        print("2. Author")
        print("3. ISBN")
        
        choice = input("\n> ")
        search_term = input("Search term: ").lower()
        
        results = []
        for book in self.books:
            if choice == '1' and search_term in book['title'].lower():
                results.append(book)
            elif choice == '2' and search_term in book['author'].lower():
                results.append(book)
            elif choice == '3' and search_term in book['isbn'].lower():
                results.append(book)
        
        if results:
            print(f"\nFound {len(results)} book(s):")
            for book in results:
                status = "Available" if book['available'] else "Checked Out"
                print(f"{book['title']} by {book['author']} - {status}")
        else:
            print("No books found")
    
    def checkout_book(self):
        isbn = input("Enter ISBN of book to checkout: ")
        
        for book in self.books:
            if book['isbn'] == isbn:
                if book['available']:
                    book['available'] = False
                    self.save_books()
                    print(f"Checked out: {book['title']}")
                    return
                else:
                    print("Book is already checked out")
                    return
        print("Book not found")
    
    def return_book(self):
        isbn = input("Enter ISBN of book to return: ")
        
        for book in self.books:
            if book['isbn'] == isbn:
                if not book['available']:
                    book['available'] = True
                    self.save_books()
                    print(f"Returned: {book['title']}")
                    return
                else:
                    print("Book was not checked out")
                    return
        print("Book not found")
    
    def list_books(self):
        if not self.books:
            print("No books in library")
            return
        
        print(f"\n📚 Library ({len(self.books)} books):")
        for i, book in enumerate(self.books, 1):
            status = "✓" if book['available'] else "✗"
            print(f"{i}. [{status}] {book['title']} by {book['author']} ({book['isbn']})")

def library_app():
    library = Library()
    
    print("📚 Library Management System 📚")
    print("=" * 50)
    
    while True:
        print("\n1. Add Book")
        print("2. Search Books")
        print("3. Checkout Book")
        print("4. Return Book")
        print("5. List All Books")
        print("6. Statistics")
        print("0. Exit")
        
        choice = input("\n> ")
        
        if choice == '0':
            break
        elif choice == '1':
            library.add_book()
        elif choice == '2':
            library.search_books()
        elif choice == '3':
            library.checkout_book()
        elif choice == '4':
            library.return_book()
        elif choice == '5':
            library.list_books()
        elif choice == '6':
            total = len(library.books)
            available = sum(1 for book in library.books if book['available'])
            print(f"\n📊 Library Statistics:")
            print(f"Total books: {total}")
            print(f"Available: {available}")
            print(f"Checked out: {total - available}")
        else:
            print("Invalid choice")

# 29. ☎️ Contact Book

if __name__ == "__main__":
    library_app()
