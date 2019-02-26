from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    title = 'Home'
    return render(request, 'job_platform/home.html', {'title': title})

@login_required
def jobs(request):
    title = 'Jobs'
    return render(request, 'job_platform/jobs.html', {'title': title})