# Generated by Django 3.2.7 on 2021-09-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MultiSearch', '0003_auto_20210924_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='first_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
    ]
