from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import RegisterForm


class SignupForm(UserCreationForm):
    class Meta:
        model = RegisterForm
        fields = (
            'username',
            'email',
            'phone_number',
            'role',
            'password1',
            'password2',
        )
