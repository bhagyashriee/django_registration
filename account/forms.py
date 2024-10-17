from django import forms
from .models import CustomUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)