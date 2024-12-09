from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, FormView

from FitnessTracker.goals.forms import SetGoalForm, EditGoalForm, DeleteGoalForm
from FitnessTracker.goals.models import Goal
from FitnessTracker.mixins import UserOwnershipMixin


class SetGoalView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = SetGoalForm
    template_name = 'goals/set-goal.html'
    success_url = reverse_lazy('private-index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GoalEditView(UserOwnershipMixin, UpdateView):
    model = Goal
    form_class = EditGoalForm
    template_name = 'goals/edit-goal.html'
    success_url = reverse_lazy('private-index')


class GoalDeleteView(UserOwnershipMixin, DeleteView, FormView):
    model = Goal
    form_class = DeleteGoalForm
    template_name = 'goals/delete-goal.html'
    success_url = reverse_lazy('private-index')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        goal = Goal.objects.get(pk=pk)
        return goal.__dict__


def approve_goal(request, pk):
    goal = Goal.objects.get(pk=pk)
    goal.approved = True
    goal.save()

    return redirect(request.META.get('HTTP_REFERER'))
