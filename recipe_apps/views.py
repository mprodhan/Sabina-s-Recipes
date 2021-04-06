from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse

from recipe_apps.models import Food
from recipe_users.models import RecipeUser

def index(request):
    html="index.html"
    return render(request, html)
