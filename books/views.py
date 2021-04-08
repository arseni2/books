from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin  # new
from django.views.generic import ListView, DetailView
from .models import Book
from django.db.models import Q

class BookListView(LoginRequiredMixin, ListView): # new
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login' # new

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin,DetailView): # new
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login' # new
    permission_required = 'books.special_status'

class SearchResultsView(ListView): # new
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):  # new
        return Book.objects.filter(
            Q(title__icontains=self.request.GET.get('q')) | Q(author__icontains=self.request.GET.get('q'))
        )

