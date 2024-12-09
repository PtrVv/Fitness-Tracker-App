from django import forms
from FitnessTracker.goals.models import Goal
from FitnessTracker.mixins import DisableFieldsMixin


class BaseGoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        exclude = ('user',)

        help_texts = {
            'make_public': 'Must be approved by staff member',
        }


class SetGoalForm(BaseGoalForm):
    class Meta(BaseGoalForm.Meta):
        exclude = ('is_completed', 'user')

    target_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class EditGoalForm(BaseGoalForm):
    pass


class DeleteGoalForm(BaseGoalForm, DisableFieldsMixin):
    disabled_fields = ('__all__',)
