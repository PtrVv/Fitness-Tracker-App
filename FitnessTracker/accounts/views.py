from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from FitnessTracker.accounts.forms import UserForm


class UserRegistrationView(CreateView):
    form_class = UserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')

