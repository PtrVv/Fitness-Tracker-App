# Generated by Django 5.1.3 on 2024-12-03 11:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meals', '0002_meal_user'),
        ('workouts', '0003_alter_workout_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WeekDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('summary', models.TextField(blank=True, null=True)),
                ('meals', models.ManyToManyField(blank=True, null=True, to='meals.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workouts', models.ManyToManyField(blank=True, null=True, to='workouts.workout')),
            ],
        ),
    ]
