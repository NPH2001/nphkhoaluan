# Generated by Django 5.0.4 on 2024-05-20 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('factors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factor',
            name='note',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
