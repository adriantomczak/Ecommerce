from django.contrib import admin
from .models import MyUser, MyUserAddress

# Register your models here.

admin.site.register(MyUser)
admin.site.register(MyUserAddress)
