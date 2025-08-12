import os
import sys
import django

# Add the project's root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Setup Sample Data (to make queries work) ---
# Clean up existing data to avoid duplicates
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

# Create an Author
author1 = Author.objects.create(name="Stephen King")

# Create a Book with a ForeignKey to the Author
book1 = Book.objects.create(title="The Stand", author=author1)
book2 = Book.objects.create(title="It", author=author1)

# Create a Library
library1 = Library.objects.create(name="Central City Library")

# Add the books to the Library's ManyToManyField
library1.books.add(book1, book2)

# Create a Librarian with a OneToOneField to the Library
librarian1 = Librarian.objects.create(name="Alice Smith", library=library1)

print("--- Sample Data Setup Complete ---")

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