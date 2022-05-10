from django.shortcuts import render
from .models import Book, Category


def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {'books': books})


def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    context = {"book": book}
    return render(request, "books/book_details.html", context)


def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)
    return render(request, "books/category.html", {'books': books, 'category': category})
