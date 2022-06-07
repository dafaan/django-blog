from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render(request, 'main.html')
    
def gallery(request):
    image = galleryImage.objects.all()
    context = {'image':image}
    return render(request, 'gallery.html', context)

def about(request):
    
    return render(request, 'about.html')

def fund_me(request):
    
    return render(request, 'fund_me.html')

def test(request):
    return render(request, 'tcp.html')

def contact(request):
    
    return render(request, 'contact.html')

