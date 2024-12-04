from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Workout(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='workouts',
    )

    name = models.CharField(
        max_length=30,
    )

    exercises = models.TextField()

    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

