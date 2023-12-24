from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from sellers.models import sell

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.info(request,'user exist')
            return render(request,'login.html');
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email exist')
            return render(request,'login.html');
        else:
            user = User.objects.create_user(username = username,email=email,password=password)
            user.save();
            return render(request,'login.html'); 
    else:    
        return render(request, 'login.html');

def login(request):
    # print("method ",request.method )
    if request.method =='POST':
        # print('POST ',request.POST)
        email = request.POST['email']
        password = request.POST['password']
        
        user = User.objects.get(email=email)
        if user.check_password(password):
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'Invaild credential')
            # return redirect('login')
            return render(request,'login.html'); 
    else:
        return render(request,'login.html');
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required(login_url='myapps:login') 
def myauction(request):
    user_sells = sell.objects.filter(user=request.user)
    return render(request, 'myauction.html', {'user_sells': user_sells})