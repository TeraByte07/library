from django.db import models
from user_app.models import customUser
from django.utils import timezone
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    num_of_pages = models.PositiveIntegerField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    is_borrowed = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)


    def __str__(self):
        return self.title
    
class Borrowed_books(models.Model):
    book = models.ForeignKey(Book, related_name= "borrowed_books", on_delete=models.CASCADE)
    user = models.ForeignKey(customUser, related_name= "borrowed_books", on_delete=models.CASCADE)
    borrowed_date=models.DateField(auto_now_add=True)
    return_date = models.DateField()
    is_returned = models.BooleanField(default=False)
    actual_return_date = models.DateField(null=True, blank=True)
    class Meta:
        verbose_name_plural = 'Borrowed Books'
    
    def save(self, *args, **kwargs):
        if self.is_returned and not self.actual_return_date:
            self.actual_return_date = timezone.now().date()  # Set the actual return date
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.user.username} borrowed {self.book.title}'