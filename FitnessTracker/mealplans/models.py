from django.contrib.auth import get_user_model
from django.db import models

from FitnessTracker.meals.models import Meal


UserModel = get_user_model()


class MealPlan(models.Model):
    plan_name = models.CharField(
        max_length=30,
    )

    plan_type = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='meal_plans',
    )

    breakfast = models.ManyToManyField(
        to=Meal,
        blank=True,
        related_name="breakfast_meal_plans",
    )

    morning_snack = models.ManyToManyField(
        to=Meal,
        blank=True,
        related_name="morning_snack_meal_plans",
    )

    lunch = models.ManyToManyField(
        to=Meal,
        blank=True,
        related_name="lunch_meal_plans",
    )

    afternoon_snack = models.ManyToManyField(
        to=Meal,
        blank=True,
        related_name="afternoon_snack_meal_plans",
    )

    dinner = models.ManyToManyField(
        to=Meal,
        blank=True,
        related_name="dinner_meal_plans",
    )

    desserts = models.ManyToManyField(
        to=Meal,
        blank=True,
        related_name="dessert_meal_plans",
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    make_public = models.BooleanField(
        default=False,
    )

    def total_calories(self):
        categories = [
            self.breakfast,
            self.morning_snack,
            self.lunch,
            self.afternoon_snack,
            self.dinner,
            self.desserts
        ]

        return sum(meal.calories for category in categories for meal in category.all())
