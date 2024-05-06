from django.contrib import admin
from .models import ProductMaster, ProductUpdateHistory, Job

admin.site.register(ProductMaster)
admin.site.register(ProductUpdateHistory)
admin.site.register(Job)
