from django.shortcuts import render

# Create your views here.
from .models import About,skils




def create(reqeust):
    about=About.objects.last()
    sk=skils.objects.all()
    

    return render (reqeust,'create.html',{'about':about,'sk':sk,
        
        
    
     })

         