from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Goal(models.Model):
    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='goals',
    )

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField(
        max_length=200,
    )

    target_date = models.DateField()

    is_completed = models.BooleanField(
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    make_public = models.BooleanField(
        default=False,
    )

    approved = models.BooleanField(
        default=False,
    )

    class Meta:
        permissions = [
            ('can_approve_goals', 'Can approve goals'),
        ]
