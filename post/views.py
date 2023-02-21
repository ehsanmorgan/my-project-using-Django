from django.shortcuts import render


from .models import Post,Reivew



def add_review(request,slug):
    post=Post.objects.get(slug=slug)
    if request.method =='POST':
        form=productReviewsForm(request.POST)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.user=request.user
            myform.comment=post
            myform.save()


# Create your views here.
