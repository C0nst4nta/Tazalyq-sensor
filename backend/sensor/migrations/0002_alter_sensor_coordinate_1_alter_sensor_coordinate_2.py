# Generated by Django 5.0.4 on 2024-05-28 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='coordinate_1',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='coordinate_2',
            field=models.FloatField(default=None),
        ),
    ]
