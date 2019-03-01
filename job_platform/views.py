from django.shortcuts import render, redirect
from .models import JobPost
from .forms import JobPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def home(request):
    title = 'Home'
    posts = JobPost.objects.all()
    return render(request, 'job_platform/home.html', {'title': title, 'jobs': posts})

@login_required
def jobs(request):
    title = 'Jobs'
    posts = JobPost.objects.all()
    return render(request, 'job_platform/jobs.html', {'title': title, 'jobs': posts})

@login_required
def createjob(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('jobs')
        else:
            return render(request, 'job_platform/createjob.html', {'form': form})
    else:
        form = JobPostForm()
        return render(request, 'job_platform/createjob.html', {'form': form})

@login_required
def detailjob(request, job_id):
    job = JobPost.objects.get(id=job_id)
    posts = JobPost.objects.exclude(id=job_id)
    return render(request, 'job_platform/detailjob.html', {'job': job, 'jobs': posts})

@login_required
def updatejob(request, job_id):
    job = JobPost.objects.get(id=job_id)

    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs')
        else:
            render(request, 'job_platform/updatejob.html', {'form': form})
    else:
        form = JobPostForm(instance=job)
        return render(request, 'job_platform/updatejob.html', {'form': form})