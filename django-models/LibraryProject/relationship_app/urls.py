from django.urls import path
from .views import list_books, LibraryDetailView # Changed here

urlpatterns = [
    path('books/', list_books, name='book_list'), # Changed here
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]