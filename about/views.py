from django.shortcuts import render

# Create your views here.
from .models import About



def create(reqeust):
    about=About.objects.last()
    print(about)

    return render (reqeust,'create.html',{'about':about
     })

         