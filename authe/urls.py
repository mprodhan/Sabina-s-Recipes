from django.urls import path
from authe import views

urlpatterns = [

    path('signup/', views.signupview, name='sign_up'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout')

]