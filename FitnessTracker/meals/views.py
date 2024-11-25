from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from FitnessTracker.meals.forms import MealForm, EditMealForm
from FitnessTracker.meals.models import Meal


class AddMealView(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealForm
    template_name = 'meals/add-meal.html'
    success_url = reverse_lazy('meals-homepage')


class EditMealView(UpdateView):
    model = Meal
    form_class = EditMealForm
    template_name = 'meals/edit-meal.html'
    success_url = reverse_lazy('meals-homepage')


class MealsHomepage(TemplateView):
    template_name = 'meals/meals-homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meals'] = Meal.objects.all()

        return context
