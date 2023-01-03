from django.shortcuts import render,redirect
from .models import post
from .forms import postForm

# Create your views here.
def post_list(request):
    all=post.objects.all()
    return render (request,'posts.html',{'data':all})

def post_detail(request,id):
    Post= post.objects.get(id=id)
    return render(request,'single.html',{'data':Post})



def create_post(request):
    if request.method=='POST':
        print('in post ----')
        form=postForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.author=request.user
            myform.save()

    else:
        print('in get ----')
        form=postForm()
    return render (request,'create.html',{'form':form})



def edit_post(request,id):
    Post= post.objects.get(id=id)
    if request.method=='POST':
        print('in post ----')
        form=postForm(request.POST,request.FILES,instance=Post)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.author=request.user
            myform.save()

    else:

        form=postForm(instance=Post)
        print('in get ----')
    return render (request,'edit.html',{'form':form})


def delete_post(request,id):
    Post=post.objects.get(id=id)
    Post.delete()
    return redirect('/blog')