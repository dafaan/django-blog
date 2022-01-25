from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    posts = blogPost.objects.all()
    context = {'posts':posts}
    return render(request, 'index.html', context)


def posts(request):
    
    return render(request, 'post.html')


def post(request, id):
    post = blogPost.objects.get(id=id)
    context = {'post':post}
    return render(request, 'post.html', context)