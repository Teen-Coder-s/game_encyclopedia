from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Collection)
admin.site.register(models.Events)
admin.site.register(models.Articles)
admin.site.register(models.Facts)