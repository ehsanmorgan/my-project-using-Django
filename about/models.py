from django.db import models

# Create your models here.


class About(models.Model):
    name=models.CharField(max_length=20)
    job=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=900)
    image=models.ImageField(upload_to='about/')
    city=models.CharField(max_length=10)
    age=models.IntegerField()
    brithday=models.CharField(max_length=30)
    freelance=models.CharField(max_length=10)
    Degree=models.CharField(max_length=10)
    phone =models.CharField(max_length=20)
    PhEmailone=models.CharField(max_length=30)
    Website=models.CharField(max_length=20)

    def __str__(self):
        return self.name


SKILL_TYPE={
    ('skill1','skill1'),
    ('skill2','skill2')
}


class skils(models.Model):
    skil=models.CharField(max_length=100)
    percentage=models.IntegerField()
    type=models.CharField(max_length=10,choices=SKILL_TYPE)

    
    def __str__(self):
        return self.skil




class sumary(models.Model):
    name=models.CharField(max_length=20)
    title=models.CharField(max_length=200)
    city=models.CharField(max_length=10)
    phone =models.CharField(max_length=20)
    PhEmailone=models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Education(models.Model):
    year=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    place=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    last=models.BooleanField(default=False)

    def __str__(self):
        return self.title


class service(models.Model):
    icone=models.CharField(max_length=20)
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=300)

    def __str__(self):
        return self.title



class Testimonials(models.Model):
    title=models.CharField(max_length=20)
    subtitle=models.CharField(max_length=100)
    content=models.TextField(max_length=400)
    name=models.CharField(max_length=20)
    job=models.CharField(max_length=20)


    def __str__(self):
        return self.name

    def __str__(self):
        return self.title