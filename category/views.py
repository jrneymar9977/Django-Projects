from django.shortcuts import render
from sellers.models import sell
# Create your views here.
def product_list(request,category):
    products = sell.objects.filter(category=category)
    return render(request,'productspage.html',{'category':category,'products':products})