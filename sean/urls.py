from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:id>', views.post, name='post'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('search_db', views.search_db, name='search_db'),
]