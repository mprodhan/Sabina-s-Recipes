from django.urls import path
from blogs import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('blog_insert/', views.bloginsert, name='bloginsert'),
    path('blog_detail/<str:username>/', views.blogdetail, name='blog'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)