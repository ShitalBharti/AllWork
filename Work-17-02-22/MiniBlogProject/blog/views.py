from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.contrib import messages

# Create your views here.
# Home
def home(request):
    return render(request, 'blog/home.html')

# About
def about(request):
    return render(request, 'blog/about.html')

# Contact
def contact(request):
    return render(request, 'blog/contact.html')

# Dashboard
def dashboard(request):
    return render(request, 'blog/dashboard.html')

# Logout
def user_logout(request):
    return HttpResponseRedirect('/')

# Signup
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! You have become an Author.')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'blog/signup.html', {'form':form})

# Login
def user_login(request):
    form = LoginForm()
    return render(request, 'blog/login.html', {'form':form})