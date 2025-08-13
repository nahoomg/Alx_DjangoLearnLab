from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book
from .models import Library # Add this line
# Function-based view to list all books
def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display a single library's details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'