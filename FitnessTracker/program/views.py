from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from FitnessTracker.program.forms import AddWeekDayForm, WeekDayDetailsForm
from FitnessTracker.program.models import WeekDay


class WeekDayHomepage(ListView):
    model = WeekDay
    template_name = 'program/program-home.html'
    context_object_name = 'weekdays'

    def get_queryset(self):
        return WeekDay.objects.filter(user=self.request.user)


class AddWeekDayView(LoginRequiredMixin, CreateView):
    model = WeekDay
    form_class = AddWeekDayForm
    template_name = 'program/program-add.html'
    success_url = reverse_lazy('program-home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class WeekDayDetailsView(UpdateView):
    model = WeekDay
    form_class = WeekDayDetailsForm
    template_name = 'program/program-details.html'
    success_url = reverse_lazy('program-home')

    def get_object(self, queryset=None):
        weekday_name = self.kwargs['weekday'].capitalize()
        user = self.request.user
        return WeekDay.objects.get(user=user, name=weekday_name)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
