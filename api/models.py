from tastypie.resources import ModelResource
from internet_library.models import Genre, Author, Book
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication

class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genres'
        allowed_methods = ['get']

class AuthorResource(ModelResource):
    class Meta:
        queryset = Author.objects.all()
        resource_name = 'authors'
        allowed_methods = ['get']

class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'books'
        allowed_method = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization() 

    def hydrate(self, bundle):
        bundle.obj.author_id = bundle.data['author_id']
        bundle.obj.genre_id = bundle.data['genre_id']
        return bundle

    def dehydrate(self, bundle):
        bundle.data['author'] = bundle.obj.author
        bundle.data['genre'] = bundle.obj.genre
        return bundle