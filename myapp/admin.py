from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(bed)
admin.site.register(ipd)
admin.site.register(scalp)
admin.site.register(complaint)
admin.site.register(past_history)
admin.site.register(personal_H_O)

