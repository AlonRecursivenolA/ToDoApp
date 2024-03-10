from django.contrib import admin
from django.contrib.auth.models import User

from ToDo_App.models import Todo, Profile

# Register your models here.

admin.site.register(Todo)
admin.site.register(Profile)
