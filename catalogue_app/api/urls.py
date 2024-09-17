from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (authorCreateView, authorDetailView, authorListView, 
                    BookCreateView, BookListView, BookDetailView, 
                    BorrowBookView, ReturnBookView, availableBookListView, borrowedBooksList)

urlpatterns = [
    path('author/create/', authorCreateView.as_view(), name="author-create"),
    path('author/details/<int:pk>/', authorDetailView.as_view(), name="author-detail"),
    path('author/lists/', authorListView.as_view(), name="author-list"),
    path('book/create/', BookCreateView.as_view(), name="book-create"),
    path('book/lists/', BookListView.as_view(), name="book-lists"),
    path('available-book/lists/', availableBookListView.as_view(), name="available-book-lists"),
    path('borrowed-book/lists/', borrowedBooksList.as_view(), name="borrowed-book-lists"),
    path('book/details/<int:pk>/', BookDetailView.as_view(), name="book-details"),
    path('books/borrow/<int:pk>/', BorrowBookView.as_view(), name='borrow-book'),
    path('books/return/<int:pk>/', ReturnBookView.as_view(), name='return-book'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)