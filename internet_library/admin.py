from django.contrib import admin
from .models import Book, Genre, Author

admin.site.site_header = "Books Admin"
admin.site.site_title = "My Books"
admin.site.index_title = "Welcome to the Books Admin area"

class BooksInline(admin.TabularInline):
    model = Book 
    extra = 1

class GenreAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'], 
            'classes': ['collapse']
        }),
    ]
    inlines = [BooksInline]


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'price')

admin.site.register(Genre, GenreAdmin)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)