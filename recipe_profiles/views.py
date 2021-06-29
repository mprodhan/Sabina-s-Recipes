from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse

from recipe_apps.models import Food
from recipe_users.models import RecipeUser
from blogs.models import Blog
from recipe_users.models import RecipeUser
# from authe.forms import SignUpForm

# def profile_image(request):
#     html = "signup.html"
#     if request.method == "POST":
#         form = SignUpForm(request.POST, request.FILES)
#         if form.is_valid():
#             data  = form.cleaned_data
#             RecipeUser.objects.create(
#                 profile_image=data['profile_image']
#             )
#             return HttpResponseRedirect(reverse('profile'))
#     else:
#         form = SignUpForm()
#     context = {"form":form}
#     return render(request, html, context)


def profileview(request, username):
    html = "profile.html"
    profilers = RecipeUser.objects.get(username=username)
    profilers = request.user
    profiles = Food.objects.filter(food_author=profilers)
    blogs = Blog.objects.filter(blog_author=profilers)
    context = {'profilers': profilers, 'profiles': profiles,
            'blogs': blogs}
    return render(request, html, context)