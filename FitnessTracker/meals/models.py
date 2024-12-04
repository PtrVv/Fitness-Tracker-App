from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Meal(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='meals',
    )

    name = models.CharField(
        max_length=30,
    )

    calories = models.IntegerField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    recipe = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name
    