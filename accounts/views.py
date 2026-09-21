import random
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .models import Users

def register_usero(request):
    if request.method == 'POST':
        username = request.POST.get('nom')
        password = request.POST.get('parol')
        password2 = request.POST.get('parol2')
        email = request.POST.get('email')

        if Users.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'imya zanyata'})

        if password != password2:
            return render(request, 'register.html', {'error': 'password ne sofpadaet'})

        if Users.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'email uje suahestvuet'})

        user = Users.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('verified')

    return render(request, 'register.html')


def login_usero(request):
    if request.method == 'POST':
        username = request.POST.get('nom')
        password = request.POST.get('parol')

        user = authenticate(username=username, password=password)
        if not user:
            return render(request, 'login.html', {'error': 'imya ili parol nesushetvuet'})

        login(request, user)
        return redirect('video_list')

    return render(request, 'login.html')


def logaut_user(request):
    logout(request)
    return redirect('login')


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

        try:
            send_mail(
                "Email Verification Code",
                f"Your verification code is: {code}",
                settings.EMAIL_HOST_USER,
                [user.email],
            )
        except:
            pass

    return render(request, 'verified.html', {'code_for_test': user.code})