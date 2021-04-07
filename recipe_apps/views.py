from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse

from recipe_apps.models import Food
from recipe_apps.forms import RecipeForm
from recipe_users.models import RecipeUser
from blogs.models import Blog

def index(request):
    html="index.html"
    data = Food.objects.all()
    blogs = Blog.objects.all()
    context = {'data': data, 'blogs': blogs}
    return render(request, html, context)

def recipe(request):
    html = "recipe.html"
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Food.objects.create(
                food_title=data['food_title'],
                ingredients=data['ingredients'],
                directions=data['directions'],
                food_author=data['food_author']
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = RecipeForm()
    context = {'form': form}
    return render(request, html, context)

def recipedetail(request, username):
    html = "recipe_view.html"
    author = RecipeUser.objects.get(username=username)
    author = request.user
    recipes = Food.objects.filter(food_author=author)
    context = {'author': author, 'recipes': recipes}
    return render(request, html, context)