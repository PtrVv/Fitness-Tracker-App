from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DeleteView, FormView

from FitnessTracker.meals.forms import MealForm, EditMealForm, DeleteMealForm
from FitnessTracker.meals.models import Meal
from FitnessTracker.mixins import UserOwnershipMixin


class AddMealView(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealForm
    template_name = 'meals/add-meal.html'
    success_url = reverse_lazy('meals-homepage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditMealView(UserOwnershipMixin, UpdateView):
    model = Meal
    form_class = EditMealForm
    template_name = 'meals/edit-meal.html'
    success_url = reverse_lazy('meals-homepage')


class MealsHomepage(ListView):
    model = Meal
    template_name = 'meals/meals-homepage.html'
    context_object_name = 'meals'
    paginate_by = 3

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)


class DeleteMealView(UserOwnershipMixin, DeleteView, FormView):
    model = Meal
    form_class = DeleteMealForm
    template_name = 'meals/delete-meal.html'
    success_url = reverse_lazy('meals-homepage')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        meal = Meal.objects.get(pk=pk)
        return meal.__dict__
