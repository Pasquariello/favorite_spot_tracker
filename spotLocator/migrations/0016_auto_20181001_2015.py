# Generated by Django 2.1 on 2018-10-01 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spotLocator', '0015_auto_20180829_1903'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.AlterField(
            model_name='spot',
            name='name',
            field=models.CharField(default='Name', max_length=50),
        ),
    ]
