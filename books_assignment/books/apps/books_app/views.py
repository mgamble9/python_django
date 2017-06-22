from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print "*"*42
    return render(request, 'books_app/index.html')
