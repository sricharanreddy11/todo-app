from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import RegistrationForm


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

    def form_invalid(self, form):
        messages.error(self.request,'Invalid Username or password')
        return self.render_to_response(self.get_context_data(form=form))


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self,form):
        user = form.save()
        if user:
            login(self.request,user)
        return super(RegisterView,self).form_valid(form)


