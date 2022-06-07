from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('post/<str:id>', views.post, name='post'),
    path('add_post', views.add_post, name='add_post'),
    path('contact', views.contact, name='contact'),
    #path('news', views.news, name='news'),
    path('search_db', views.search_db, name='search_db'),
]