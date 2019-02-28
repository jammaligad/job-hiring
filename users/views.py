from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as jh_login, logout
from .forms import UserRegisterForm

def index(request):
    if request.method == 'POST':
        if 'signupbtn' in request.POST:
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You may now login.')
<<<<<<< HEAD
                return redirect('index')
=======
                messagesheader = 'Welcome to the Hub!'
                regform = UserRegisterForm()
                return render(request, 'users/index.html', {'regform': regform, 'messagesheader': messagesheader})
            else:
                messages.warning(request, f'Warning! Please try again.')
                messagesheader = 'Warning'
                return render(request, 'users/signup.html', {'messagesheader': messagesheader})
>>>>>>> d057f28c8115c1d76ca936d9ab70d4b9837a7541
        elif 'loginbtn' in request.POST:
            username = request.POST['username']
            password = request.POST['password1']
            form = UserRegisterForm(request.POST)
            user = authenticate(username=username, password=password)
            if user is not None:
<<<<<<< HEAD
                login(request, user)
                return redirect('/home')
            else:
                return redirect('/index')

=======
                jh_login(request, user)
                return redirect('home')
            else:
                messages.error(request, f'Invalid Account Details. Please try again.')
                messagesheader = 'Error'
                regform = UserRegisterForm()
                return render(request, 'users/login.html', {'regform': regform, 'messagesheader': messagesheader})
>>>>>>> d057f28c8115c1d76ca936d9ab70d4b9837a7541
    else:
        logout(request)
        regform = UserRegisterForm()
        return render(request, 'users/index.html', {'regform': regform})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        form = UserRegisterForm(request.POST)
        user = authenticate(username=username, password=password)
        if user is not None:
            jh_login(request, user)
            return redirect('home')
        else:
            messages.error(request, f'Invalid Account Details. Please try again.')
            messagesheader = 'Error'
            regform = UserRegisterForm()
            return render(request, 'users/login.html', {'regform': regform, 'messagesheader': messagesheader})
    else:
        form = UserRegisterForm()
        return render(request, 'users/login.html', {'regform': form})

def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You may now login.')
            messagesheader = 'Welcome to the Hub!'
            return redirect('login')
        else:
            messages.warning(request, f'Warning! Please try again.')
            messagesheader = 'Warning'
            form = UserRegisterForm()
            return render(request, 'users/signup.html', {'regform': form})
    else:
        form = UserRegisterForm()
        return render(request, 'users/signup.html', {'regform': form})
