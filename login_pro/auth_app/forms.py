from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'username')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={
            'placeholder': 'enter username here'
        }
    ))
    password = forms.CharField(max_length=20, widget=forms.PasswordInput(
        attrs={
            'placeholder': 'enter password here'
        }
    ))
