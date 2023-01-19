from django.contrib import admin


# Register your models here.
from about import models

admin.site.register(models.About)
admin.site.register(models.skils)
admin.site.register(models.sumary)
admin.site.register(models.Professional)
admin.site.register(models.Education)
admin.site.register(models.service)
admin.site.register(models.Testimonials)

