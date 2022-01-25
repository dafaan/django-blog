from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.user.username
    
    
    
class blogPost(models.Model):
    title = models.CharField(max_length = 200)
    tagline = models.CharField(max_length=50)
    author = models.ForeignKey(profile, null=True, blank=True, on_delete=models.CASCADE)
    post = models.TextField()
    image = models.ImageField(upload_to='media')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
    
