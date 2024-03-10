from time import sleep

from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.forms import ModelForm

from ToDo_App.models import Todo


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class ToDoTask(forms.ModelForm):
    class Meta:
        model = Todo
        category_choice = {'Work': 'Work', 'Personal':'Personal','Fitness':'Fitness'}
        fields = ['author', 'title', 'description', 'priority', 'reminded_time','category']  # ,'due_date_day','due_date_time']

        widgets = {
            'author': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'priority': forms.Select(choices={'High': 'high', 'Medium': 'Medium', 'Low': 'Low'},
                                     attrs={'class': 'form-control', 'background-color': 'red'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'reminded_time': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices={'Work': 'Work', 'Personal':'Personal','Fitness':'Fitness'},attrs={'class': 'form-control'}),
            # 'due_date_day' : forms.DateTimeInput(attrs={'class':'form-control'}),
            # 'due_date_time':forms.DateTimeInput(attrs={'class':'form-control'}),
        }


