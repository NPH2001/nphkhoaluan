# Generated by Django 5.0.4 on 2024-04-20 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Searchforcare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequences', models.CharField(max_length=200)),
                ('location_start', models.CharField(max_length=200)),
                ('location_end', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]