from django.shortcuts import render,redirect
from .models import *
from accounts.models import Users
from django.contrib.auth.decorators import login_required




def profiles_create(request):
    proverka_profile = Profiles.objects.filter(owner_profile = request.user).exists()
    
    if proverka_profile:
        profile = Profiles.objects.get(owner_profile=request.user)
        return render(request, 'profile.html', {'profile': profile})
    

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        avatar = request.FILES.get('avatar')
        bio = request.POST.get('bio')
        
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.save()
        
        
        Profiles.objects.create(owner_profile=request.user,avatar = avatar , bio = bio)

            
        return redirect('profile')
        
    return render(request, 'profile_create.html')



def profile(request):
    user = request.user
    profile = Profiles.objects.get(owner_profile=request.user)
    
    return render(request, 'profile.html', {'user':user , 'profile':profile})

