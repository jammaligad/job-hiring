from django.shortcuts import render, redirect
<<<<<<< HEAD
from .models import Job, Post, Apply
from .forms import JobModelForm
=======
from .models import JobPost
from .forms import JobPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
>>>>>>> d057f28c8115c1d76ca936d9ab70d4b9837a7541

@login_required
def home(request):
<<<<<<< HEAD
    context = {}
    context['Jobs'] = Job.objects.all()
    return render(request, 'job_platform/home.html',context)

def create_job(request):
    context = {}
    context['form'] = JobModelForm()
    if request.method == 'POST':
        form = JobModelForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('/home/')
        else:
            context['form'] = form
            render(request,'job_platform/create_job.html',context)
    else:
        return render(request,'job_platform/create_job.html',context)
=======
    title = 'Home'
    return render(request, 'job_platform/home.html', {'title': title})

@login_required
def jobs(request):
    title = 'Jobs'
    posts = JobPost.objects.all()
    return render(request, 'job_platform/jobs.html', {'title': title, 'jobs': posts})

@login_required
def createjob(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
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
>>>>>>> d057f28c8115c1d76ca936d9ab70d4b9837a7541
