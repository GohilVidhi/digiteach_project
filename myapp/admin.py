from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Designation)
admin.site.register(School)
admin.site.register(Job)
admin.site.register(Teacher)
admin.site.register(Job_Apply)