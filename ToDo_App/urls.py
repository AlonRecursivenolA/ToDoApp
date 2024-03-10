from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ToDo_App.views import (HomeView, ShowToDoView, CreateTaskView, ChangeTaskView, DeleteTaskView, SignUpView,
                            CompletedTaskView, FinishedTasksView, RetreatTaskView, ProfileView, EditUserProfileView,
                            Search_by_task, Sort_lowToHigh, Sort_hightoLow)

urlpatterns = [
    path('', HomeView.as_view(), name='HomeView'),
    path('show_todo_list/<int:pk>', ShowToDoView.as_view(), name='Show_To_Do_list'),
    path('create_task/', CreateTaskView.as_view(), name='Create_Task'),
    path('change_task/<int:pk>', ChangeTaskView.as_view(), name='Change_Task'),
    path('delete_task/<int:pk>', DeleteTaskView.as_view(), name='Delete_Task'),
    # path('login/', my_view, name='login')
    path('register/', SignUpView.as_view(), name='Register_View'),
    path('mark_completed/<int:pk>', CompletedTaskView.as_view(), name='mark_completed'),
    path('finished_tasks/', FinishedTasksView.as_view(), name= 'finished_tasks'),
    path('unmark_completed/<int:pk>', RetreatTaskView.as_view(), name = 'retreat_task'),
    path('profile_view/<int:pk>/', ProfileView.as_view(), name='profile_view'),
    path('update_profile/', EditUserProfileView.as_view(), name = 'edit_profile'),
    path('search_task/', Search_by_task, name='search_task'),
    path('sort_priority_to_high/', Sort_lowToHigh, name='sort_toHigh'),
    path('sort_priority_to_low/', Sort_hightoLow, name='sort_toLow'),



]
