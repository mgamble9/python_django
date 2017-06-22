from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print "*"*42
    return render(request, 'the_wall_app/index.html')
    
