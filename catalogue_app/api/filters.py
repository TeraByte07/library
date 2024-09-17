import django_filters
from catalogue_app.models import Book, Borrowed_books

class bookFilter(django_filters.FilterSet):
    # Filter on related 'Book' fields via the ForeignKey
    category = django_filters.CharFilter(field_name="category", lookup_expr='icontains')
    publisher = django_filters.CharFilter(field_name="publisher", lookup_expr='icontains')
    
    class Meta:
        model = Book
        fields = ['category', 'publisher']

class borrowedBookFilter(django_filters.FilterSet):
    # Filter on related 'Book' fields via the ForeignKey
    category = django_filters.CharFilter(field_name="book__category", lookup_expr='icontains')
    publisher = django_filters.CharFilter(field_name="book__publisher", lookup_expr='icontains')
    
    class Meta:
        model = Borrowed_books
        fields = ['category', 'publisher']
