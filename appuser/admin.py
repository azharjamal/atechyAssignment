from django.contrib import admin
from .models import AppUser, Role

admin.site.register(AppUser)
admin.site.register(Role)