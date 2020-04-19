from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Register(UserCreationForm):
    Name=forms.CharField(max_length=80,label="Name")
    Email=forms.EmailField(label="Email ID")

    class Meta:
        model=User
        fields=['Name','Email','username','password1','password2']

class Confess(forms.Form):
    confession=forms.CharField(max_length=500)