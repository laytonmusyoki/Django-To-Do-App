from django import forms
from .models import Create
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Createform(forms.ModelForm):
    class Meta:
        model=Create
        fields="__all__"

        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Enter name'}),
            'semester':forms.TextInput(attrs={'placeholder':'Enter semester/year'}),
            'week':forms.TextInput(attrs={'placeholder':'Enter the week'}),
            'ToDo':forms.TextInput(attrs={'placeholder':'Enter the project'})
        }


class Createusers(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter your username'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your email'}),
            'password1':forms.TextInput(attrs={'placeholder':'Enter your password'})
        }