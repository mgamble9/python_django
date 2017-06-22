from django.shortcuts import render, redirect
from .models import Product
# Create your views here.
def index(request):
    print "*"*42
    Product.objects.create(name='sux3000',description='cheap bicycle')
    Product.objects.create(name='adx120',description='electric guitar')
    Product.objects.create(name='440RCE',description='acoustic guitar')
    products_all = Product.objects.all()
    for prod in products_all:
        print prod
    return render(request,'product_app/index.html')
