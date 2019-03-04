from django.shortcuts import render, redirect
from .models import JobPost, Application, Profile
from .forms import JobPostForm, ProfileForm, ApplicationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def profile(request):
    title = 'Profile'
    profile = Profile.objects.get(user=request.user)
    jobs = JobPost.objects.filter(author=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            render(request, 'job_platform/profile.html', {'form': form, 'title': title})
    else:
        form = ProfileForm(instance=profile)
        return render(request, 'job_platform/profile.html', {'profile': profile, 'form': form, 'jobs': jobs})

@login_required
def home(request):
    title = 'Home'
    profile = Profile.objects.get(user=request.user)
    posts = JobPost.objects.select_related('author')
    return render(request, 'job_platform/home.html', {'title': title, 'jobs': posts, 'profile': profile})

@login_required
def jobs(request):
    title = 'Jobs'
    profile = Profile.objects.get(user=request.user)
    posts = JobPost.objects.select_related('author')
    return render(request, 'job_platform/jobs.html', {'title': title, 'jobs': posts, 'profile': profile})

@login_required
def createjob(request):
    title = 'Jobs'
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = JobPostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('jobs')
        else:
            return render(request, 'job_platform/createjob.html', {'form': form, 'title': title, 'profile': profile})
    else:
        form = JobPostForm()
        return render(request, 'job_platform/createjob.html', {'form': form, 'title': title, 'profile': profile})

@login_required
def detailjob(request, job_id):
    title = 'Jobs'
    profile = Profile.objects.get(user=request.user)
    job = JobPost.objects.get(id=job_id)
    posts = JobPost.objects.exclude(id=job_id)
    if request.method=='POST':
        if 'applyjob' in request.POST:
            form = ApplicationForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.jobpost = job
                instance.applicant = request.user
                instance.save()
                return redirect('jobs')
            else:
                return render(request, 'job_platform/detailjob.html', {'job': job, 'jobs': posts, 'title': title, 'form': form, 'profile': profile})
        elif 'editjob' in request.POST:
            form = JobPostForm(request.POST, instance=job)
            if form.is_valid():
                form.save()
                return redirect('jobs')
            else:
                render(request, 'job_platform/detailjob.html', {'form': form, 'title': title, 'profile': profile})
    else:
        form = ApplicationForm()
        jobform = JobPostForm(instance=job)
        return render(request, 'job_platform/detailjob.html', {'job': job, 'jobs': posts, 'title': title, 'form': form, 'jobform': jobform, 'profile': profile})

@login_required
def updatejob(request, job_id):
    title = 'Jobs'
    profile = Profile.objects.get(user=request.user)
    job = JobPost.objects.get(id=job_id)

    if request.method == 'POST':
        form = JobPostForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('jobs')
        else:
            render(request, 'job_platform/updatejob.html', {'form': form, 'title': title, 'profile': profile})
    else:
        form = JobPostForm(instance=job)
        return render(request, 'job_platform/updatejob.html', {'form': form, 'title': title, 'profile': profile})

@login_required
def archive(request,job_id):
    if JobPost.objects.get(id=job_id).archived:
        JobPost.objects.filter(id=job_id).update(archived=False)
    else:
        JobPost.objects.filter(id=job_id).update(archived=True)   
    return redirect('jobs')
