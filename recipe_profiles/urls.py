from django.urls import path
from recipe_profiles import views

urlpatterns = [
    path('profile/<str:username>/', views.profileview, name='profile')
]