from django.contrib import admin

from .models import User, School, Education

admin.site.register(User)
admin.site.register(School)
admin.site.register(Education)