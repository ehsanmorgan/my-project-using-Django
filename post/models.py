from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify


# Create your models here.
class Post(models.Model):
	name=models.CharField(max_length=20)
	content=models.TextField(max_length=200)
	slug=models.slugify(null=True,blank=True)



	def __str___(self):
		return self.name



	def save(self,*args, **kwargs):
    	 self.slug=slugify(self.name)
		 super(Post,self).save(*args, **kwargs)

	


	




	
	
	







class Reivew(models.Model):
	user=models.ForeignKey(User,related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
	comment=models.ForeignKey(Post,related_name='comment_author',on_delete=models.SET_NULL,null=True,blank=True)
	createt_at=models.DateTimeField(default=timezone.now)



	


	 
