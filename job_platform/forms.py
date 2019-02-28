from django.forms import ModelForm
<<<<<<< HEAD
from .models import Job, Post, Apply

class JobModelForm(ModelForm):
    class Meta:
        model = Job
        exclude = ['id','user']
=======
from .models import JobPost

class JobPostForm(ModelForm):
    class Meta:
        model = JobPost
        exclude = ['id']
>>>>>>> d057f28c8115c1d76ca936d9ab70d4b9837a7541
