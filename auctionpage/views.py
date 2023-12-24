from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import updates


# Create your views here.

def home(request):

    produpd = updates.objects.all() 
    return render(request, 'homepage.html', {'produpd':produpd});

def about(request):
    return render(request, 'about.html');

def sell(request):
    return render(request, 'sellerpage.html');

def productdetails(request, id):
    product = get_object_or_404(updates, id=id)
    return render(request, 'productdetails.html', {'product': product})

def search_results(request):
    if 'search' in request.GET:
        query = request.GET['search']
        results = sell.objects.filter(productname__icontains=query)
        return render(request, 'search_results.html', {'results': results, 'query': query})
    else:
        return render(request, 'search_results.html')  