from django import forms

from FitnessTracker.mixins import DisableFieldsMixin
from FitnessTracker.workouts.models import Workout


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ['user']


class AddWorkoutForm(WorkoutForm):
    pass


class EditWorkoutForm(WorkoutForm):
    pass


class DeleteWorkoutForm(WorkoutForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)
