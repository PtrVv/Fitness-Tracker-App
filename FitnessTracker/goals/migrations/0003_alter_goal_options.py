# Generated by Django 5.1.3 on 2024-12-09 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0002_goal_approved_goal_created_at_goal_make_public'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={'permissions': [('can_approve_goals', 'Can approve goals')]},
        ),
    ]
