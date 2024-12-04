from django.contrib.auth import get_user_model
from django.db import models

from FitnessTracker.meals.models import Meal
from FitnessTracker.workouts.models import Workout

UserModel = get_user_model()


class WeekDay(models.Model):
    name = models.CharField(
        max_length=20,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='weekdays',
    )

    meals = models.ManyToManyField(
        to=Meal,
        blank=True,
    )

    workouts = models.ManyToManyField(
        to=Workout,
        blank=True,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )

    def total_calories(self):
        return sum(meal.calories for meal in self.meals.all())
