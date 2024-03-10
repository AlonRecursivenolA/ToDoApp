from datetime import timezone

from django.contrib.auth.models import User
from django.db import models
from django.db.models import options
from django.shortcuts import get_object_or_404
from django.urls import reverse


# Create your models here.
class Todo(models.Model):  # default is id in every table!

    priority_choices = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('low', 'low'),
    ]
    category_choices = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Fitness','Fitness')
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30, null=True)
    description = models.TextField(max_length=255, null=True)
    priority = models.CharField(choices=priority_choices, null=True, max_length=10)
    due_date_day = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    reminded_time = models.TimeField(null=True, blank=True)
    category = models.CharField(null=True,choices=category_choices, max_length=255)
    # due_date_time = models.TimeField(null=True, blank=T
    # rue)
    #creation_date = models.DateTimeField(auto_now_add=True, default=timezone)
    # category =
    # completion_ status =
    def get_absolute_url(self):
        return reverse('HomeView')


    def get_context_data(self,**kwargs):
        context = super(Todo,self).get_context_data()
        stuff = Todo.objects.all
        context["stuff"] = stuff

        return context


    def __str__(self):
        return f"{self.title} due to {self.due_date_day}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True, upload_to='images/')
    bio = models.CharField(max_length=255)
