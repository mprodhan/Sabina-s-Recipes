from django import forms
from django.contrib.auth.forms import UserCreationForm

from recipe_users.models import RecipeUser

class SignUpForm(UserCreationForm):
    display_name = forms.CharField(max_length=30)

    class Meta:
        model = RecipeUser
        fields = ('email', 'username', 'display_name', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.Charfield(max_length=forms.PasswordInput)