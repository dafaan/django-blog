from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts', views.posts, name='posts'),
    path('post/<str:id>', views.post, name='post'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]