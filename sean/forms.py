from django import forms
from django.db import models

from .models import blogPost
  
# create a ModelForm
class prodForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = blogPost
        fields = "__all__"