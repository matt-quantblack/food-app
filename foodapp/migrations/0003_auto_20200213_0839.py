# Generated by Django 3.0.3 on 2020-02-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0002_recipe_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='co2saved',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='dollarsaved',
            field=models.IntegerField(default=0),
        ),
    ]
