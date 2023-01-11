from django.shortcuts import render

# Create your views here.
from .models import About,skils




def create(reqeust):
    about=About.objects.last()
    codaing_skills=skils.objects.filter(type='coding')
    design_skills=skils.objects.filter(type='design')
    

    return render (reqeust,'create.html',{'about':about,
        'codaing_skills':codaing_skills,
        'design_skills':design_skills
    
     })

         