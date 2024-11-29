from django import forms

from FitnessTracker.meals.models import Meal
from FitnessTracker.mixins import DisableFieldsMixin


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ['user']


class EditMealForm(MealForm):
    pass


class DeleteMealForm(MealForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)
