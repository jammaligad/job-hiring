from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=200, label='')
    lastname = forms.CharField(max_length=200, label='')
    email = forms.EmailField(label='')

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        self.fields.pop('password2')
        for fieldname in ['username', 'password1']:
            self.fields[fieldname].help_text = None

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].label = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['firstname'].widget.attrs['placeholder'] = 'First Name'
        self.fields['firstname'].label = ''
        self.fields['lastname'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['lastname'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['email'].label = ''

    class Meta:
        model = User
        fields = ['username', 'firstname', 'lastname', 'email', 'password1']

class UserLoginForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields.pop('password2')
        for fieldname in ['username', 'password1']:
            self.fields[fieldname].help_text = None

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = User
        fields = ['username', 'password1']