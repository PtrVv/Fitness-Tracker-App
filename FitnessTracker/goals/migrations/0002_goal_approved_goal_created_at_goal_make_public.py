# Generated by Django 5.1.3 on 2024-12-09 08:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='goal',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goal',
            name='make_public',
            field=models.BooleanField(default=False),
        ),
    ]