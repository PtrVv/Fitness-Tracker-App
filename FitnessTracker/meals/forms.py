from django import forms

from FitnessTracker.meals.models import Meal


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ['user']


class EditMealForm(MealForm):
    pass
