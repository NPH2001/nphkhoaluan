# Generated by Django 5.0.4 on 2024-05-09 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biologist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biologist',
            options={'permissions': [('special_status', 'Can confirm motifs')]},
        ),
    ]
