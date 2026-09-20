from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout



def register_usero(request):
    if request.method == 'POST':
        username = request.POST.get('nom')
        password = request.POST.get('parol')
        password2 = request.POST.get('parol2')
        email = request.POST.get('email')
        
        user = Users.objects.filter(username= username).exists()
        email_exists = Users.objects.filter(email = email).exists()
        if user:
            return render(request, 'register.html', {'error':'imya zanyata'})
        
        if password != password2:
            return render(request, 'register.html', {'error':'password ne sofpadaet'})
        
        if email_exists:
            return render(request, 'register.html', {'error':'email uje suahestvuet'})
        
        
        Users.objects.create_user(username=username,password=password,email=email)
        
        return redirect('login')
    
    return render(request, 'register.html')
        
        
def login_usero(request):
    if request.method == 'POST':
        username = request.POST.get('nom')
        password = request.POST.get('parol')

        user = authenticate(username=username,password=password)
        
        if not user:
            return render(request, 'login.html', {'error':'imya ili parol nesushetvuet'})
        
        login(request, user)
        
        return redirect('profiles_create')
    
    return render(request, 'login.html')
        
def logaut_user(request):

    logout(request)
    return redirect('login')



         
        
    
        