from django.urls import path
from blogs import views

urlpatterns = [

    path('blog_insert/', views.bloginsert, name='bloginsert'),
    path('blog_detail/<str:username>/', views.blogdetail, name='blog'),

]