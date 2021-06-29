from django.shortcuts import render, reverse, HttpResponseRedirect, \
    HttpResponse

from blogs.models import Blog
from blogs.forms import BlogForm
from recipe_users.models import RecipeUser

def bloginsert(request):
    html = "blog.html"
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Blog.objects.create(
                blog_title=data['blog_title'],
                blog_body=data['blog_body'],
                blog_author=data['blog_author']
                # blog_image=data['blog_image']
            )
            return HttpResponseRedirect(reverse('homepage'))
    else:
        form = BlogForm()
    context = {'form': form}
    return render(request, html, context)

def blogdetail(request, username):
    html = "blog_view.html"
    author = RecipeUser.objects.get(username=username)
    author = request.user
    blogs = Blog.objects.filter(blog_author=author)
    context = {'author': author, 'blogs': blogs}
    return render(request, html, context)
