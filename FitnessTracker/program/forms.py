from django import forms

from FitnessTracker.meals.models import Meal
from FitnessTracker.program.models import WeekDay
from FitnessTracker.workouts.models import Workout


class WeekDayForm(forms.ModelForm):
    class Meta:
        model = WeekDay
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['meals'].queryset = Meal.objects.filter(user=user)
        self.fields['workouts'].queryset = Workout.objects.filter(user=user)


class AddWeekDayForm(WeekDayForm):
    class Meta(WeekDayForm.Meta):
        fields = ('name', 'summary')


class WeekDayDetailsForm(WeekDayForm):
    class Meta(WeekDayForm.Meta):
        exclude = ('name', 'user')
