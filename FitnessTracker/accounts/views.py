from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from FitnessTracker.accounts.forms import UserForm, ProfileForm
from FitnessTracker.accounts.models import Profile


class UserRegistrationView(CreateView):
    form_class = UserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')


class ProfileDetailsView(LoginRequiredMixin, TemplateView):
    model = Profile
    template_name = 'profile/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_object_or_404(Profile, user=self.request.user)

        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'profile/profile-edit.html'
    form_class = ProfileForm

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.request.user.pk})

