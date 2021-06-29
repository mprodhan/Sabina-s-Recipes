from django.urls import path
from recipe_profiles import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('profile/<str:username>/', views.profileview, name='profile')
]