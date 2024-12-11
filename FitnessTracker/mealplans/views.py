from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from FitnessTracker.mealplans.forms import AddMealPlanForm, EditMealPlanForm, DeleteMealPlanForm
from FitnessTracker.mealplans.models import MealPlan
from FitnessTracker.mixins import UserOwnershipMixin


class MealPlanHomePageView(ListView):
    model = MealPlan
    template_name = 'mealplans/meal-plans-homepage.html'
    context_object_name = 'mealplans'

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.request.user)

        return queryset


class CreateMealPlanView(LoginRequiredMixin, CreateView):
    model = MealPlan
    form_class = AddMealPlanForm
    template_name = 'mealplans/add-meal-plan.html'
    success_url = reverse_lazy('mealplans-home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user

        return super().form_valid(form)


class EditMealPlanView(UserOwnershipMixin, UpdateView):
    model = MealPlan
    form_class = EditMealPlanForm
    template_name = 'mealplans/edit-meal-plan.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        return kwargs

    def get_success_url(self):
        return reverse_lazy('mealplan-details', kwargs={'pk': self.object.pk})


class DeleteMealPlanView(UserOwnershipMixin, DeleteView):
    model = MealPlan
    form_class = DeleteMealPlanForm
    template_name = 'mealplans/delete-meal-plan.html'
    success_url = reverse_lazy('mealplans-home')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        mealplan = MealPlan.objects.get(pk=pk)

        return mealplan.__dict__


class DetailsMealPlanView(UserOwnershipMixin, DetailView):
    model = MealPlan
    template_name = 'mealplans/mealplan-details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        mealplan = self.get_object()

        context['breakfast'] = mealplan.breakfast.all()
        context['morning_snack'] = mealplan.morning_snack.all()
        context['lunch'] = mealplan.lunch.all()
        context['afternoon_snack'] = mealplan.afternoon_snack.all()
        context['dinner'] = mealplan.dinner.all()
        context['desserts'] = mealplan.desserts.all()

        return context

