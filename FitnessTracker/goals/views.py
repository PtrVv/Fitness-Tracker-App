from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, FormView

from FitnessTracker.goals.forms import SetGoalForm, EditGoalForm, DeleteGoalForm
from FitnessTracker.goals.models import Goal


class SetGoalView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = SetGoalForm
    template_name = 'goals/set-goal.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GoalEditView(UpdateView):
    model = Goal
    form_class = EditGoalForm
    template_name = 'goals/edit-goal.html'
    success_url = reverse_lazy('index')


class GoalDeleteView(DeleteView, FormView):
    model = Goal
    form_class = DeleteGoalForm
    template_name = 'goals/delete-goal.html'
    success_url = reverse_lazy('index')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        goal = Goal.objects.get(pk=pk)
        return goal.__dict__

