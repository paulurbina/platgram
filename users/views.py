
# Create your views here.
# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#Execeptions
from django.db.utils import IntegrityError

#Models
from django.contrib.auth.models import User
from users.models import Profile

def update_profile(request):
    return render(request, 'users/update_profile.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'login', { 'error': 'Invalid username or password' })

    return render(request, 'users/login.html')

def signup_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']


        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match.'})

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})
            
        user.last_name = request.POST['last_name']
        user.first_name = request.POST['first_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')

@login_required
def logout_view (request):
    logout(request)
    return redirect('login')