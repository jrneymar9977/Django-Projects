from django.shortcuts import render
from sellers.models import sell
from django.contrib.auth.decorators import login_required

@login_required(login_url='myapps:login') 
def myauction(request):
    user_sells = sell.objects.filter(user=request.user)
    return render(request, 'myauction.html', {'user_sells': user_sells})

