# Generated by Django 2.1 on 2018-08-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotLocator', '0008_auto_20180824_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity',
            field=models.CharField(choices=[('Road-Cycling', 'ROADCYCLE'), ('Mountain Biking', ' MTNBIKE'), ('Hiking', 'HIKE'), ('Fishing', 'FISH'), ('Climbing', 'CLIMB')], default='Fishing', max_length=15),
        ),
    ]
