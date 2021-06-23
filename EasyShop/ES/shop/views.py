from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil



# Create your views here.

def index(request):
    products = Product.objects.all()
    print("productssssssss\t",products)
    n = len(products)
    print("lennnnnn\t",n)
    nSlides = n//4 + ceil((n/4) -(n//4))
    print("slidessss\t",nSlides)
    allProds = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    params = {'allProds': allProds}
    #params= {'no_of_slides':nSlides,'range':range(1,nSlides+1),'no_of_product': products}

    return render(request,'shop/index.html',params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def productView(request):
    return HttpResponse("We are at product view")

def search(request):
    return HttpResponse("We are at search")

def tracker(request):
    return HttpResponse("We are at tracker")

def checkout(request):
    return HttpResponse("We are at checkout")
