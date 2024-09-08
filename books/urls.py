from django.urls import path

from books.views import BooksView, BookDetailView

urlpatterns = [
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('', BooksView.as_view(), name='home'),
]