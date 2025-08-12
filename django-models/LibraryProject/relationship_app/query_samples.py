# ... (rest of the code)

# --- Query Examples ---
print("\n1. Query all books by a specific author:")
author_books = Book.objects.filter(author__name="Stephen King")
for book in author_books:
    print(f"  - {book.title}")

print("\n2. List all books in a library:")
library_name = "Central City Library"
library_books = Library.objects.get(name=library_name).books.all()
for book in library_books:
    print(f"  - {book.title}")

print("\n3. Retrieve the librarian for a library:")
library = Library.objects.get(name="Central City Library")
librarian = Librarian.objects.get(library=library)
print(f"  - The librarian for '{library.name}' is {librarian.name}")# ... (rest of the code)

# --- Query Examples ---
print("\n1. Query all books by a specific author:")
author_name = "Stephen King"
author = Author.objects.get(name=author_name)
author_books = Book.objects.filter(author=author)
for book in author_books:
    print(f"  - {book.title}")

print("\n2. List all books in a library:")
library_name = "Central City Library"
library_books = Library.objects.get(name=library_name).books.all()
for book in library_books:
    print(f"  - {book.title}")

print("\n3. Retrieve the librarian for a library:")
library = Library.objects.get(name="Central City Library")
librarian = Librarian.objects.get(library=library)
print(f"  - The librarian for '{library.name}' is {librarian.name}")
