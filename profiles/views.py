from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import Users

def profiles_detail(request, username):
    profile_user = get_object_or_404(Users, username=username)
    channels = profile_user.channels.all()
    return render(request, 'profile.html', {
        'profile_user': profile_user,
        'channels': channels
    })


@login_required
def profiles_create(request):
    user = request.user
    if request.method == 'POST':
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.bio = request.POST.get('bio')
        if request.FILES.get('avatar'):
            user.avatar = request.FILES.get('avatar')
        user.save()
        return redirect('profiles_detail', username=user.username)

    return render(request, 'profile_create.html', {'user': user})