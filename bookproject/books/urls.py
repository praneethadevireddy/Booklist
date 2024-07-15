from django.urls import path
from .views import BookListCreate, BookDelete, home

urlpatterns = [
    path('', home, name='home'),
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDelete.as_view(), name='book-delete'),
]
