# Update a Book Instance

### Command
```python
from bookshelf.models import Book
book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()
updated_book = Book.objects.get(title="Nineteen Eighty-Four")
print(updated_book.title)