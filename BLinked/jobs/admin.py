from django.contrib import admin

# Register your models here.
from blink.models import Job, Qualification

admin.site.register(Job)
admin.site.register(Qualification)
