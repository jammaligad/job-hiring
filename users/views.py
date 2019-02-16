from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import UserRegisterForm

def index(request):
    if request.method == 'POST':
        if 'signupbtn' in request.POST:
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You may now login.')
                return redirect('index') 
        elif 'loginbtn' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            if form.is_valid():
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)

    else:
        form = UserRegisterForm()
        return render(request, 'users/index.html', {'form': form})
