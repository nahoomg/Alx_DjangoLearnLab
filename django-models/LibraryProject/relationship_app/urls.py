from django.urls import path
from . import views
from .views import LibraryDetailView, CustomLoginView # IMPORT CustomLoginView

urlpatterns = [
    # Path for the homepage, pointing to the book list view
    path('', views.book_list, name='home'),
    
    # Paths for Task 2: Views and URL Configuration
    path('books/', views.book_list, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Paths for Task 3: User Authentication
    path('register/', views.register, name='register'),
    
    # THIS LINE IS NOW CORRECT
    path('login/', CustomLoginView.as_view(), name='login'),
    
    path('logout/', views.logout_view, name='logout'),
    
    # Paths for Task 4: Role-Based Access Control
    path('admin_dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian_dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member_dashboard/', views.member_view, name='member_dashboard'),
]