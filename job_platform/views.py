from django.shortcuts import render, redirect
from .models import Job, Post, Apply
from .forms import JobModelForm

def home(request):
    context = {}
    context['Jobs'] = Job.objects.all()
    return render(request, 'job_platform/home.html',context)

def create_job(request):
    context = {}
    context['form'] = JobModelForm()
    if request.method == 'POST':
        form = JobModelForm(request.POST)
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
