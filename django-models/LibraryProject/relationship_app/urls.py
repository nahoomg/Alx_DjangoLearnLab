from django.urls import path
from .views import list_books, LibraryDetailView, register_user, login_user, logout_user # Updated import

urlpatterns = [
    # Existing URL patterns
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # New: Authentication URL patterns
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]