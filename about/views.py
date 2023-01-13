from django.shortcuts import render

# Create your views here.
from .models import About,skils




def create(reqeust):
    about=About.objects.last()
    skill1=skils.objects.filter(type='skill1')
    skill2=skils.objects.filter(type='skill2')
    

    return render (reqeust,'create.html',{'about':about,'skill1':skill1 , 'skill2':skill2
        
        
    
     })

         