from django.urls import path
from . import views

app_name = 'lib'
urlpatterns = [
    path('', views.index, name='index'),
    path('books', views.books_list, name='books_list'),
    path('books/<int:book_id>', views.single_book, name='single_book')
]