from django.contrib import admin
from .models import Author, Book, Borrowed_books
# Register your models here.
admin.site.register([Author, Book, Borrowed_books])