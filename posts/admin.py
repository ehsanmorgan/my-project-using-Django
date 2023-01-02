from django.contrib import admin

# Register your models here.
from .models import post

admin.site.register(post)



def __str__(self):
    return self.title
