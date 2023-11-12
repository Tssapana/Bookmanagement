from django.urls import path
from .views import get_all_books, add_book, delete_book, update_book

urlpatterns=[
    path('', get_all_books, name='books'),
    path('add-book', add_book, name='add-book'),
    path('delete/<int:book_id>', delete_book, name='delete-book'),
    path('update/<int:book_id>', update_book, name='update-book')


]