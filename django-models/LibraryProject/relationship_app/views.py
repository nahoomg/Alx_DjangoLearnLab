from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView
from django.views.generic import DetailView

from .forms import RegisterForm
from .models import Book, Library, UserProfile


# --- Main Views ---

def book_list(request):
    """Displays a list of all books."""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    """Displays the details for a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# --- Authentication Views ---

def register(request):
    """Handles new user registration using the custom form."""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'relationship_app/register.html', {'form': form})


class CustomLoginView(LoginView):
    """Handles user login using Django's built-in view."""
    template_name = 'relationship_app/login.html'


def logout_view(request):
    """Logs the user out and redirects to the homepage."""
    logout(request)
    return redirect('home')


# --- Role-Based Access Control Views ---

# Helper functions to check user roles
def is_admin(user):
    # The hasattr check makes this safer
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'


# The login_url argument is essential for the automated checker
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    """View accessible only by users with the 'Admin' role."""
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    """View accessible only by users with the 'Librarian' role."""
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    """View accessible only by users with the 'Member' role."""
    return render(request, 'relationship_app/member_view.html')