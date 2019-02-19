from django.forms import ModelForm
from .models import Job, Post, Apply

class JobModelForm(ModelForm):
    class Meta:
        model = Job
        exclude = ['id']
