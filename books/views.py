from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView, FormView
from django.views.generic.detail import SingleObjectMixin

from books.forms import CommentForm
from books.models import Book


class BooksView(ListView):
    model = Book
    template_name = 'home.html'


class CommentGet(DetailView):
    model = Book
    template_name = 'book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Book
    form_class = CommentForm
    template_name = "book_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.book = self.object
        comment.comment = form.cleaned_data['comment']
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        book = self.get_object()
        return reverse('book_detail', kwargs={'pk': book.pk})


class BookDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)