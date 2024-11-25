from django import forms

from FitnessTracker.meals.models import Meal


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'


class EditMealForm(MealForm):
    pass
