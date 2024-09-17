from .serializers import authorSerializer, BookSerializer, BorrowedBooksSerializer
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from catalogue_app.models import Book, Author, Borrowed_books
from .permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone
from .filters import bookFilter, borrowedBookFilter
from django_filters.rest_framework import DjangoFilterBackend

class authorCreateView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = authorSerializer
    permission_classes = [IsAdminUser]
    
class authorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = authorSerializer
    permission_classes = [IsAuthenticated]
    
class authorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = authorSerializer
    permission_classes = [IsAdminOrReadOnly]
    
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
    
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = bookFilter
    
class availableBookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = bookFilter
    
    def get_queryset(self):
        return Book.objects.filter(is_available=True)
    
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrReadOnly]

class borrowedBooksList(generics.ListAPIView):
    queryset = Borrowed_books.objects.all()
    serializer_class = BorrowedBooksSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_class = borrowedBookFilter
    
class BorrowBookView(APIView):
    def post(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

        if book.is_borrowed or not book.is_available:
            return Response({'error': 'Book is not available for borrowing'}, status=status.HTTP_400_BAD_REQUEST)

        # Extract return_date from request
        return_date = request.data.get('return_date')
        if not return_date:
            return Response({'error': 'Return date is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            return_date = timezone.datetime.strptime(return_date, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid return date format'}, status=status.HTTP_400_BAD_REQUEST)

        # Create Borrowed_books entry
        borrowed_book = Borrowed_books(
            book=book,
            user=request.user,
            return_date=return_date,
            is_returned = False
        )
        borrowed_book.save()

        # Update Book status
        book.is_borrowed = True
        book.is_available = False
        book.save()

        serializer = BorrowedBooksSerializer(borrowed_book)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]  # Restrict access to admin users

    def post(self, request, pk):
        try:
            borrowed_book = Borrowed_books.objects.get(pk=pk)
        except Borrowed_books.DoesNotExist:
            return Response({'error': 'Borrowed record not found'}, status=status.HTTP_404_NOT_FOUND)

        # Verify if the record is owned by the user
        if borrowed_book.user != request.user:
            return Response({'error': 'You do not own this borrowed record'}, status=status.HTTP_403_FORBIDDEN)

        # Update the borrowed book record
        borrowed_book.is_returned = True
        borrowed_book.save()  # This will trigger the save method to set actual_return_date

        # Update the associated book record
        book = borrowed_book.book
        book.is_borrowed = False
        book.is_available = True
        book.save()

        borrowed_book.delete()
        serializer = BorrowedBooksSerializer(borrowed_book)
        return Response(serializer.data, status=status.HTTP_200_OK)
