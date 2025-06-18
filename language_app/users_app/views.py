from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home_page')  # Redirect to a home page or dashboard after login
        else:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('login')
         
    else:
        return render(request, 'authentication/login.html', {})