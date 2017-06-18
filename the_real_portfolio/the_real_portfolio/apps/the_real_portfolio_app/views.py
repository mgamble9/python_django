from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'the_real_portfolio_app/index.html')

def projects(request):
    return render(request, 'the_real_portfolio_app/projects.html')

def aboutme(request):
    return render(request, 'the_real_portfolio_app/aboutme.html')

def testimonials(request):
    return render(request, 'the_real_portfolio_app/testimonials.html')
