from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional.')
    last_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional.')
    email = forms.EmailField(max_length = 254, help_text = 'Required. Inform a valid email address.')
    # password = forms.CharField(widget = forms.PasswordInput)
    degree = forms.CharField(help_text = 'Enter your degree/office. Whatever you input here will be set to your profile.')

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'degree' ,'email', 'password1', 'password2']
