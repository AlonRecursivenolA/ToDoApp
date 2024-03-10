from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic, View
from django.views.decorators.csrf import csrf_protect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from ToDo_App.forms import ToDoTask, RegisterForm
from ToDo_App.models import Todo, Profile

from django.contrib.auth import authenticate, login

# Create your views here.
# def HomeView(request):
#     model = Todo
#     display_user = Todo.objects.filter(author=0)
#     if display_user != int:
#         display_user = Todo.objects.filter(author=0)
#         return render(request, 'Home_View.html', {'display':display_user})
#     else:
#         dis = Todo.objects.filter(author=request.user)
#         return render(request, 'Home_View.html', {'display': dis})


from django.contrib.auth import authenticate, login

from django.contrib.auth import authenticate, login
# @csrf_protect
# def my_view(request):
#    if request.method == "POST":
#        username = request.POST.get('username')
#        password = request.POST.get('password')
#        user = authenticate(request, username=username, password=password)
#        if user:
#            login(request, user)
#            return reverse_lazy('HomeView')
#        return render(request,'registration/login.html',{"invalid":True})
#    else:
#         return render(request,'registration/login.html')

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class EditUserProfileView(generic.UpdateView):
    template_name = 'registration/edit_profile.html'
    form_class = UserChangeForm
    success_url = reverse_lazy('HomeView')

    def get_object(self):
        return self.request.user


class SignUpView(generic.CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    form_class = UserCreationForm
    success_message = "Your profile was created successfully"


class CompletedTaskView(View):

    def post(self, request, *args, **kwargs):  # this method is for classbasedviews
        obj = get_object_or_404(Todo, pk=self.kwargs['pk'])
        obj.is_completed = True
        obj.save()

        return redirect(reverse_lazy('HomeView'))


class RetreatTaskView(View):

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Todo, pk=self.kwargs['pk'])
        obj.is_completed = False
        obj.save()

        return redirect(reverse_lazy('finished_tasks'), )


class FinishedTasksView(generic.ListView):
    model = Todo
    fields = '__all__'
    template_name = 'finished_tasks.html'


class HomeView(generic.ListView):
    model = Todo
    fields = '__all__'
    template_name = 'Home_View.html'


def Search_by_task(request):
    title_of_task = request.GET.get('search_task').lower()  # O(n)
    if title_of_task == 'high' or 'medium' or 'low':
        ts = Todo.objects.filter(priority__iexact=title_of_task)
    if title_of_task == 'work' or title_of_task == 'personal' or title_of_task == 'fitness':
        ts = Todo.objects.filter(category__iexact=title_of_task)
    else:
        ts = Todo.objects.filter(title__contains=title_of_task)
    context = {
        'ts': ts,
    }
    return render(request, 'search_task.html', context)


def Sort_lowToHigh(request):
    high_priority = Todo.objects.filter(priority__iexact='high')
    medium_priority = Todo.objects.filter(priority__iexact='medium')
    low_priority = Todo.objects.filter(priority__iexact='low')

    context = {
        'high_list': high_priority,
        'medium_list': medium_priority,
        'low_list': low_priority,
    }
    return render(request, 'priority_low_to_high.html', context)

    # return HttpResponse(high_priority)


def Sort_hightoLow(request):
    high_priority = Todo.objects.filter(priority__iexact='high')
    medium_priority = Todo.objects.filter(priority__iexact='medium')
    low_priority = Todo.objects.filter(priority__iexact='low')

    context = {
        'high_list': high_priority,
        'medium_list': medium_priority,
        'low_list': low_priority,
    }
    return render(request, 'priority_high_to_low.html', context)

    # def get(self, request, *args, **kwargs):
    #     global search_task
    #     search_task = request.GET.get('search_task')

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(self, **kwargs)
    #     data_search = Todo.objects.filter(id=self.request.user.id)
    #     if any(word in data_search.title for word in search_task.split()):
    #         data['Task'] = data_search

    #
    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data2 = Todo.objects.filter(id=self.request.user.id)
    #     data['Todos'] = data2
    #     return data


class ShowToDoView(DetailView):
    model = Todo
    fields = '__all__'
    template_name = 'Show_To_Do_List.html'


class CreateTaskView(CreateView):
    model = Todo
    form_class = ToDoTask
    template_name = 'Create_Task.html'

    # def form_valid(self, form):
    #     #form.instance.Todo_id = self.kwargs['pk']
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)


class ChangeTaskView(UpdateView):
    model = Todo
    form_class = ToDoTask
    template_name = 'Change_Task.html'


class DeleteTaskView(DeleteView):
    model = Todo
    template_name = 'Delete_Task.html'
    success_url = reverse_lazy('HomeView')


class ProfileView(UpdateView):
    model = Profile
    template_name = 'profile_view.html'
    fields = '__all__'
    success_url = reverse_lazy('HomeView')
