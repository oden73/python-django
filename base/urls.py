"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from api.models import GenreResource, AuthorResource, BookResource
from tastypie.api import Api

genre_resource = GenreResource()
author_resource = AuthorResource()
book_resource = BookResource()

api = Api(api_name='v1')
api.register(genre_resource)
api.register(author_resource)
api.register(book_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('internet_library.urls')),
    path('api/', include('api.urls')),
]
