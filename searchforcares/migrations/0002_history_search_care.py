# Generated by Django 5.0.4 on 2024-05-20 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchforcares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='History_search_care',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('F_r', models.CharField(blank=True, max_length=5000, null=True)),
                ('R_f_r', models.CharField(blank=True, max_length=5000, null=True)),
                ('Ms', models.CharField(blank=True, max_length=5000, null=True)),
                ('Ms_r', models.CharField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]
