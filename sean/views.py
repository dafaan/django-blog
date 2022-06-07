from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.postgres.search import SearchRank, SearchQuery, SearchVector
from django.db.models import Q

# Create your views here.


def home(request):
    posts = blogPost.objects.all()
    context = {'posts':posts}
    return render(request, 'index.html', context)

def news(request):
    posts = blogPost.objects.all()
    context = {'posts':posts}
    return render(request, 'index.html', context)


def post(request, id):
    post = blogPost.objects.get(id=id)
    context = {'post':post}
    return render(request, 'post.html', context)





def contact(request):
    
    return render(request, 'contact.html')


def search_db(request):
    #if request.method == 'POST':
    #query = request.GET.get('query', 1)
    check = SearchVector('title', 'tagline')   
    sq = SearchQuery(request.GET.get('query', 1))
    print(sq) 
    post = blogPost.objects.annotate(rank=SearchRank(check, sq)).filter().order_by('-rank')
    context = {'post':post}
    
    return render(request, 'search.html', context)


def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        tagline = request.POST['tagline']
        print(title)
        print(tagline)
        #if form.is_valid():
            
    context = {}
    context['form'] = prodForm()
    return render(request, 'add_post.html', context)