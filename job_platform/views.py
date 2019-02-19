from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'job_platform/home.html')

@login_required
def jobs(request):
    return render(request, 'job_platform/jobs.html')