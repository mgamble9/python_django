from django.shortcuts import render, redirect
from .models import Book

# Create your views here.
def index(request):
    print "*"*42
    try:
        context = {
            "books" : Book.objects.all(),
        }
    except:
        context = {}
    return render(request,'full_stack_books_app/index.html', context)

def add_book(request):
    if request.method == 'POST':
        print "*"*42
        print request.POST
        Book.objects.create(title=request.POST['title'],
            author=request.POST['author'],
            category=request.POST['category'],
            )
    return redirect('/')
