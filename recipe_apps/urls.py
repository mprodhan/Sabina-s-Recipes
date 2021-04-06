from django.urls import path
from recipe_apps import views

urlpatterns = [
    path('', views.index, name='homepage')
]