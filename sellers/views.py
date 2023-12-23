from django.shortcuts import render,redirect
from .models import sell


# Create your views here.
def sell_item(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        productname = request.POST.get('productname')
        productdescription = request.POST.get('productdescription')
        productprice = request.POST.get('productprice')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        productimg = request.FILES.get('productimg')
        address = request.POST.get('address')

        sell_object = sell(
            category=category,
            productname=productname,
            productdescription=productdescription,
            productprice=productprice,
            date=date,
            start_time=start_time,
            end_time=end_time,
            productimg=productimg,
            address=address
        )
        sell_object.save()
        return redirect('/')  

    return render(request, 'sellerpage.html')