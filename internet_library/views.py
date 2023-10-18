from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . import models
 
def index(request):
    books = models.Book.objects.all()
    return render(request, 'internet_library/internet_lib.html', {'books': books})

def books_list(request):
    books = models.Book.objects.all()
    return render(request, 'internet_library/books_list.html', {'books': books})

def single_book(request, book_id):
    book = get_object_or_404(models.Book, pk=book_id)
    return render(request, 'internet_library/single_book.html', {'book': book})
