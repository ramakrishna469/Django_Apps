from django.contrib import admin
from models import Registration


# class RegAdmin(admin.ModelAdmin):
# 	fields=['username', 'email']

admin.site.register(Registration)
