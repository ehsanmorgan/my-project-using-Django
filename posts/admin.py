from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
from .models import post

class postAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'

    list_display=['title','author','tags']
    list_filter=['author','tags']
    search_fields=['title','content']

admin.site.register(post,postAdmin)


