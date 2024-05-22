# Generated by Django 5.0.4 on 2024-05-20 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_history_belong_factor'),
        ('searchforcares', '0002_history_search_care'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='Belong_history_search_care',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='belong_history_search_care', to='searchforcares.history_search_care'),
        ),
    ]
