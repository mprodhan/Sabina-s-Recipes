from django import forms

from recipe_apps.models import Food
from recipe_users.models import RecipeUser

class RecipeForm(forms.Form):
    food_title = forms.CharField(max_length=50)
    ingredients = forms.CharField(widget=forms.Textarea)
    directions = forms.CharField(widget=forms.Textarea)
    food_author = forms.ModelChoiceField(queryset=RecipeUser.objects.all())
    food_image = forms.FileField()