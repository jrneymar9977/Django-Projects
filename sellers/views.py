from django.shortcuts import render,redirect
from .models import sell
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='myapps:login')
def sell_item(request):
    if request.method == 'POST':
        try:
            # Your existing code
            user = request.user  # Get the logged-in user
            sell_object = sell(
                user=user,
                category=request.POST.get('category'),
                productname=request.POST.get('productname'),
                productdescription=request.POST.get('productdescription'),
                productprice=request.POST.get('productprice'),
                date=request.POST.get('date'),
                start_time=request.POST.get('start_time'),
                end_time=request.POST.get('end_time'),
                productimg=request.FILES.get('productimg'),
                address=request.POST.get('address')
            )
            sell_object.save()
            messages.success(request, 'Item successfully listed for auction.')
            return redirect('myapp:myauction')
        except Exception as e:
            messages.error(request, f'Error: {e}')
            # You can log the exception or perform other actions as needed
            return redirect('myapp:sell')

    messages.error(request, 'Please log in to sell items.')
    return redirect('myapps:login')
