from django.db import models


class Program(models.Model):
    """
        TODO: Program Model with->
            user -> ForeignKey to=UserModel, {exclude in form}
            meals -> ManyToMany field to=Meal,
            workouts -> ManyToMany field to=Workout,
            summary -> TextField(optional),
    """
