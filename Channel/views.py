from django.shortcuts import render,redirect
from .models import *


def create_channel(request):
    
    if request.user.is_verified:
    
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            avatar = request.FILES.get('avatar')
        
        
        
            Channel.objects.create(title= title , description=description,avatar=avatar, owner = request.user)
            
            return redirect('profile')
        
        return render(request, 'create_channel.html')
    
    return redirect('verified')
        
        
        
        
        