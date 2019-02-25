from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, label='')
    last_name = forms.CharField(max_length=200, label='')
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
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['first_name'].label = ''
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['last_name'].label = ''
        self.fields['email'].widget.attrs['placeholder'] = 'E-mail'
        self.fields['email'].label = ''

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']