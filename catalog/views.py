from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre
from  django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits' : num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)


class BookListView(LoginRequiredMixin,generic.ListView):
    model = Book
    context_object_name = 'book_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'catalog/book_list.html'  # Specify your own template name/location
    paginate_by = 2

class AuthorListView(LoginRequiredMixin,generic.ListView):

    model = Author
    context_object_name = 'author_list'   # your own name for the list as a template variable
    #queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'catalog/author_list.html'  # Specify your own template name/location
    paginate_by = 2

class BookDetailView(LoginRequiredMixin,generic.DetailView):
    model = Book
    
    
class AuthorDetailView(LoginRequiredMixin,generic.DetailView):
    model = Author



class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing books on loan to current user."""
    model = BookInstance
    template_name ='catalog/books_instances_by_user.html'
    paginate_by = 3

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).order_by('due_back')

    