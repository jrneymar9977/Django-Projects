from django.shortcuts import render
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
