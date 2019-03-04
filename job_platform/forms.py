from django import forms
from django.forms import ModelForm
from .models import JobPost, Application, Profile

class ProfileForm(ModelForm):
    displaypic = forms.ImageField(label='Profile Picture',required=False, \
                                    error_messages ={'invalid': "Image files only"},\
                                    widget=forms.FileInput)
    resume = forms.FileField(label='Resume',required=False, \
                                    error_messages ={'invalid': "PDF files only"},\
                                    widget=forms.FileInput)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['displaypic'].label = ''

    class Meta:
        model = Profile
        exclude = ['id', 'user']

class JobPostForm(ModelForm):
    class Meta:
        model = JobPost
        exclude = ['id', 'archived']

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ['id']