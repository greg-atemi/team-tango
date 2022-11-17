from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import Book, BookInstance, Language, Genre
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available
    }

    return render(request, 'catalog/index.html', context=context)


class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = '__all__'

    # success_url =


class BookDetail(DetailView):
    # mapping = model_detail.html
    model = Book


class BookList(ListView):
    model = Book


@login_required
def my_view(request):
    return render(request, 'catalog/my_view.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'catalog/signup.html'


class CheckedOutBooksByUserVIew(LoginRequiredMixin, ListView):
    # List all instances but filter based on the currently logged in user session
    model = BookInstance
    template_name = 'catalog/profile.html'
    paginate_by = 5  # 5 book instances per page

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).all()
