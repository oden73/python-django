from django.urls import path, include
from api.models import GenreResource, AuthorResource, BookResource
from tastypie.api import Api

api = Api(api_name='v1')
api.register(GenreResource())
api.register(AuthorResource())
api.register(BookResource())

urlpatterns = [
    path('', include(api.urls), name='index')
]
