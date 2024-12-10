from django import forms

from FitnessTracker.mealplans.models import MealPlan
from FitnessTracker.meals.models import Meal


class BaseMealPlanForm(forms.ModelForm):
    class Meta:
        model = MealPlan
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        # Capture the user from kwargs
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if self.user:
            # Filter the queryset for each meal-related field
            meal_fields = ['breakfast', 'morning_snack', 'lunch', 'afternoon_snack', 'dinner', 'desserts']
            for field_name in meal_fields:
                if field_name in self.fields:
                    self.fields[field_name].queryset = Meal.objects.filter(user=self.user)


class AddMealPlanForm(BaseMealPlanForm):
    class Meta(BaseMealPlanForm.Meta):
        exclude = ('user',)


class EditMealPlanForm(BaseMealPlanForm):
    pass


class DeleteMealPlanForm(BaseMealPlanForm):
    pass
