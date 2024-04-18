from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django import forms
from .models import *


def signup(request):
    if request.method == 'POST':
        # Retrieve form data
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check if passwords match
        if password != confirm_password:
            print("Passwords do not match.")
            return redirect('signup')

        # Create the user
        user = CustomUser.objects.create_user(username=username, email=email, password=password, firstname=first_name, lastname=last_name)
        user.save()

        # Redirect to a success page or homepage
        return redirect('login')
    else:
        return render(request, 'signup.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = CustomUser.objects.get(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a specific page after successful login
            return redirect('index')  
        else:
            # Handle invalid login credentials
            pass
    return render(request, 'login.html')

def index(request):
    user = request.user
    print(user)
    return render(request , 'index.html')

