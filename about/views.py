from django.shortcuts import render

# Create your views here.
from .models import About,skils,service,Testimonials,sumary,Education,Professional




def create(reqeust):
    about=About.objects.last()
    skill1=skils.objects.filter(type='skill1')
    skill2=skils.objects.filter(type='skill2')
    Service=service.objects.all()
    testimonials=Testimonials.objects.all()
    Sumary=sumary.objects.last()
    education=Education.objects.all()
    professional=Professional.objects.all()
    

    return render (reqeust,'create.html',{'about':about,'skill1':skill1 , 'skill2':skill2, 'Service':Service, 'testimonials':testimonials,'Sumary':Sumary,'education':education,'professional':professional,
        
        
    
     })

         