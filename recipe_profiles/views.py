from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse

from recipe_apps.models import Food
from recipe_users.models import RecipeUser
from blogs.models import Blog
from recipe_users.models import RecipeUser

def profileview(request, username):
    html = "profile.html"
    profilers = RecipeUser.objects.get(username=username)
    profilers = request.user
    profiles = Food.objects.filter(food_author=profilers)
    blogs = Blog.objects.filter(blog_author=profilers)
    context = {'profilers': profilers, 'profiles': profiles, 
            'blogs': blogs}
    return render(request, html, context)