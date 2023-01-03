from django.shortcuts import render
from .models import post

# Create your views here.
def post_list(request):
    all=post.objects.all()
    return render (request,'posts.html',{'data':all})

def post_detail(request,id):
    Post= post.objects.get(id=id)
    return render(request,'single.html',{'data':Post})