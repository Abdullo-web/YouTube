from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth.decorators import login_required


@login_required
def create_channel(request):
    
    if not request.user.is_verified:
        return redirect('verified')
    
    if request.user.is_verified:
    
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            avatar = request.FILES.get('avatar')
        
            if title:
                Channel.objects.create(title=title,description=description,avatar=avatar,owner=request.user)
        
            
                return redirect('profile')
            else:
                return render(request, 'create_channel.html', {'error':'title is required'})


    return render(request, 'create_channel.html')


@login_required
def verified(request):
    user = request.user
    


    if user.is_verified:

        return redirect('create_channel')
   
    
    if request.method == 'POST':
        code = request.POST.get('code')
        
        
            
        if user.code == code:
            user.is_verified = True
            user.code = None
            user.save()
            
            return redirect('create_channel')
        else:
            return render(request, 'verified.html', {'error': 'Wrong code'})
            

    if not user.code:
    
        code = str(random.randint(1000, 9999))

        user.code = code
        
        user.save()
        
        
        send_mail(
            "Email Verification Code",
            f"Your verification code is: {code}",
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        
        

    return render(request, 'verified.html')
        
        
        
        
        