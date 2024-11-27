from django import forms

from FitnessTracker.workouts.models import Workout


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        exclude = ['user']

class AddWorkoutForm(WorkoutForm):
    pass


class EditWorkoutForm(WorkoutForm):
    pass
