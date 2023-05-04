from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput
from django import forms
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'jclass': 'form-control'}),
        label='유저이름'
    )


class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            'username'
        ]
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'style': 'background-color : skyblue',
                'placeholder': 'ID'
            })
        }
        labels = {
            'username': 'ID',
        }
