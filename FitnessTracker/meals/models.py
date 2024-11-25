from django.db import models


class Meal(models.Model):
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
    