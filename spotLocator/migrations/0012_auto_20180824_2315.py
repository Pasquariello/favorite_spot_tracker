# Generated by Django 2.1 on 2018-08-24 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotLocator', '0011_auto_20180824_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spot',
            name='color',
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity',
            field=models.CharField(choices=[('ROADCYCLE', 'Road-Cycling'), ('MTNBIKE', ' Mountain Biking'), ('HIKE', 'Hiking'), ('FISH', 'FISH'), ('CLIMB', 'CLIMB')], default='FISH', max_length=15),
        ),
        migrations.AlterField(
            model_name='spot',
            name='activity',
            field=models.CharField(choices=[('ROADCYCLE', 'Road-Cycling'), ('MTNBIKE', ' Mountain Biking'), ('HIKE', 'Hiking'), ('FISH', 'Fishing'), ('CLIMB', 'Rock Climbing')], default='FISH', max_length=15),
        ),
    ]
