from django.contrib import admin


# Register your models here.
from posts import models

admin.site.register(models.post)

