from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm

# Create your views here.

def get_all_books(request):
    books= Book.objects.all()
    context= {'books': books}
    return render (request, 'list_book.html', context)

def add_book(request):
    instance=BookForm()
    if request.method == "POST":
        instance=BookForm(request.POST)
        if instance.is_valid():
            instance.save()
            return redirect('/')
    context= {'form': instance}
    return render (request, 'add_book.html', context)

def delete_book(request,book_id):
    Book.objects.get(id=book_id).delete()
    return redirect('/')

def update_book (request, book_id):
    book= Book.objects.get(id=book_id)
    instance=BookForm(instance=book)
    if request.method == 'POST':
        instance= BookForm(request.POST, instance=book)
        if instance.is_valid():
            instance.save()
            return redirect('/')
    context= {'form': instance}
    return render (request, 'edit_book.html', context)








