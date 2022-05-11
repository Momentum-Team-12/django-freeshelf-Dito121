from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category, Favorite
from .forms import FavoriteForm


def list_books(request):
    books = Book.objects.all()
    return render(request, "books/list_books.html", {'books': books})


def book_details(request, pk):
    form = FavoriteForm()
    book = Book.objects.get(pk=pk)
    return render(request, "books/book_details.html", {"book": book, 'form': form})


def books_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    books = Book.objects.filter(category=category)
    return render(request, "books/category.html", {'books': books, 'category': category})


def add_favorite(request, pk):
    if request.method == 'POST':
        book = Book.objects.get_object_or_404(Book, pk=pk)
        user = request.user
        form = FavoriteForm(data=request.POST)
        if form.is_valid():
            favorite = form.save(commit=False)
            favorite.book = book
            favorite.user = user
            favorite.save()
            return redirect(to='book_details', pk=pk)


def books_by_favorites(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'books/books_by_favorites.html', {'favorites': favorites})
