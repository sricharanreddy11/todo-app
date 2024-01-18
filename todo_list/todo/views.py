from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView,DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.contrib import messages
from django.urls import reverse_lazy


def index(request):
    return render(request, "index.html")


class TaskListView(LoginRequiredMixin, ListView):
    template_name = "task_list.html"
    model = Task
    context_object_name = "tasks"

    def get_queryset(self):
        base_qs = super(TaskListView, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class TaskDetailView(LoginRequiredMixin, DetailView):
    template_name = "task_detail.html"
    model = Task
    context_object_name = "task"

    def get_queryset(self):
        base_qs = super(TaskDetailView, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = "task_form.html"
    model = Task
    context_object_name = "form"
    fields = ['task_name', 'task_description', 'status']
    success_url = reverse_lazy('tasks')

    def get_queryset(self):
        base_qs = super(TaskCreateView, self).get_queryset()
        return base_qs.filter(user=self.request.user)

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Task Created Successfully")
        return super(TaskCreateView, self).form_valid(form)


class TaskUpdateView(UpdateView):
    template_name = "task_form.html"
    model = Task
    context_object_name = "form"
    fields = ['task_name', 'task_description', 'status']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "Task Updated Successfully")
        return super(TaskUpdateView, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(TaskUpdateView, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class TaskDeleteView(DeleteView):
    template_name = "task_confirm_delete.html"
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "Task Deleted Successfully")
        return super(TaskDeleteView, self).form_valid(form)

    def get_queryset(self):
        base_qs = super(TaskDeleteView, self).get_queryset()
        return base_qs.filter(user=self.request.user)